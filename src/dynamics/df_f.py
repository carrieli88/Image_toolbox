"""
This is df/f calculation based on the paper: Nature protocols, 6, 28–35, 2011
Created by Dan on 08/18/16
Last update: 06/19/17
"""

import numpy as np
from src.shared_funcs.numeric_funcs import smooth_lpf
from scipy.signal import exponential, fftconvolve
import matplotlib.pyplot as plt

def min_window(shit_data, wd_width):
    """
    Calculate the baseline
    Very awkward
    update on 09/13: this allows for the multiple cell-processing.  The module "Dynamics" should be updated accordingly.
    """
    f0 = np.zeros_like(shit_data)
    f0[:wd_width] = np.amin(shit_data[:wd_width], axis = 0)

    N = len(f0)
    for ii in np.arange(wd_width, N-wd_width):
        f0[ii] = np.amin(shit_data[ii-wd_width:ii+wd_width], axis = 0)

    f0[N-wd_width:] = np.amin(shit_data[N-wd_width:], axis = 0)

    return f0
# this is a good baseline calculation.


def dff_raw(shit_data, ft_width, ntruncate = 20):
    """
    calculate df_f for shit_sig.
    ft_width: the time scale of features in the raw f(t). Unit: 1 (not in seconds)
    ntruncate: the number of datapoits to be discarded.
    Get both F0 and df_f.
    """
    s_filt = smooth_lpf(shit_data[ntruncate:], ft_width)[1]

    f_base = min_window(s_filt, 6*ft_width)
    dff_r = (shit_data[ntruncate:]-f_base)/f_base

    return dff_r, f_base
    # done with dff_raw

def dff_expfilt(dff_r, dt, t_width = 2.0):
    """
    Exponentially weighted moving average filter
    OK this also works.
    """
    M = int(t_width/dt+1)*8 + 1 # the number of window
    wd = exponential(M, center=None, tau = t_width) # Symmetric = True

    NT, NP = dff_r.shape
    dff_expf = np.zeros([NT, NP])
    tt = np.arange(1,NT+1)*dt
    denom_filter = (1-np.exp(-tt/t_width))*t_width # the denominator
    for cp in range(NP):
        numer_filter = fftconvolve(dff_r[:,cp], wd, mode='same')*dt
        dff_expf[:,cp] = numer_filter/denom_filter

    return dff_expf, wd
    # done with dff_expf


# ------------------------------------Test the main functions--------------------------------------
def main():
    print('Tested!')



if __name__ == '__main__':
    main()
