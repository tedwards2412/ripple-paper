import jax.numpy as jnp
import jax.scipy.optimize as jopt
import scipy.optimize as opt
import jax
from jax.config import config
config.update("jax_enable_x64", True)

# from tqdm.auto import tqdm, trange
from typing import Tuple
from ripple.waveforms import IMRPhenomD
from ripple import ms_to_Mc_eta
import timeit


Array = jnp.ndarray

def get_eff_pads(fs: Array) -> Tuple[Array, Array]:
    r"""
    Gets arrays of zeros to pad a function evaluated on a frequency grid so the
    function values can be passed to ``jax.numpy.fft.ifft``.
    Args:
        fs: uniformly-spaced grid of frequencies. It is assumed that the first
            element in the grid must be an integer multiple of the grid spacing
            (i.e., ``fs[0] % df == 0``, where ``df`` is the grid spacing).
    Returns:
        The padding arrays of zeros. The first is of length ``fs[0] / df`` and
        the second is of length ``fs[-1] / df - 2``.
    """
    df = fs[1] - fs[0]
    N = 2 * jnp.array(fs[-1] / df - 1).astype(int)
    pad_low = jnp.zeros(jnp.array(fs[0] / df).astype(int))
    pad_high = jnp.zeros(N - jnp.array(fs[-1] / df).astype(int))
    return pad_low, pad_high

@jax.jit
def get_match_arr(
    h1: Array, h2: Array, Sns: Array, pad_low: Array, pad_high: Array
) -> Array:
    """
    Calculates the match between two frequency-domain complex strains. The maximizations
    over the difference in time and phase at coalescence are performed by taking
    the absolute value of the inverse Fourier transform.
    Args:
        h1: the first set of strains
        h2: the second set of strains
        Sns: the noise power spectral densities
        fs: frequencies at which the strains and noise PSDs were evaluated
        pad_low: array of zeros to pad the left side of the integrand before it
            is passed to ``jax.numpy.fft.ifft``
        pad_right: array of zeros to pad the right side of the integrand before
            it is passed to ``jax.numpy.fft.ifft``
    Returns:
        The match.
    """
    # Factors of 4 and df drop out due to linearity
    norm1 = jnp.sqrt(jnp.sum(jnp.abs(h1) ** 2 / Sns))
    norm2 = jnp.sqrt(jnp.sum(jnp.abs(h2) ** 2 / Sns))

    # Use IFFT trick to maximize over t_c. Ref: Maggiore's book, eq. 7.171.
    integrand_padded = jnp.concatenate((pad_low, h1.conj() * h2 / Sns, pad_high))
    # print(low_padding, high_padding, len(fs), N)
    return jnp.abs(len(integrand_padded) * jnp.fft.ifft(integrand_padded)).max() / (
        norm1 * norm2
    )

def check_effectualness():
    # Define the frequencies at which to evaluate the strain
    f_l = 16
    f_u = 512
    df = 0.0125
    fs = jnp.linspace(f_l, f_u, int((f_u - f_l) / df) + 1)

    low_padding, high_padding = get_eff_pads(fs)

    Sns = jnp.ones_like(fs)

    # Generate the test waveform
    m1_msun = 20.0 # In solar masses
    m2_msun = 19.0
    chi1 = 0.5 # Dimensionless spin
    chi2 = -0.5
    tc = 0.0 # Time of coalescence in seconds
    phic = 0.0 # Time of coalescence
    dist_mpc = 1000 # Distance to source in Mpc

    Mc, eta = ms_to_Mc_eta(jnp.array([m1_msun, m2_msun]))
    theta_test = jnp.array([Mc, eta, chi1, chi2, dist_mpc, tc, phic])
    h_test = IMRPhenomD.gen_IMRPhenomD(fs, theta_test)


    def opt_func(theta):
        theta_full = jnp.concatenate((theta, jnp.array([dist_mpc, tc, phic])))
        h_ref = IMRPhenomD.gen_IMRPhenomD(fs, theta_full)
        match = get_match_arr(h_test, h_ref, Sns, low_padding, high_padding)
        return -match

    # Calculate the effectualness between the test and reference waveforms
    # starttime = timeit.default_timer()
    # print("The start time is :",starttime)

    x0 = jnp.array([20., 0.22, 0.1, -0.1])
    bnds = ((10., 30.), (0.18, 0.25), (-1.0, 1.0), (-1.0, 1.0))
    # res = opt.minimize(opt_func, x0, bounds=bnds, tol=1e-6)
    res = opt.differential_evolution(opt_func, bnds, tol=1e-6)
 
    # # print("The time difference is ", timeit.default_timer() - starttime, "seconds")
    print(res.x, res.fun)
    # theta_final = jnp.concatenate((res.x, jnp.array([dist_mpc, tc, phic])))
    # h_ref = IMRPhenomD.gen_IMRPhenomD(fs, theta_final)
    # match = get_match_arr(h_test, h_ref, Sns, low_padding, high_padding)

    # theta_true = jnp.array([Mc, eta, chi1, chi2])
    # match = opt_func(x0)
    # print(match)

    return None



if __name__ == "__main__":
    check_effectualness()