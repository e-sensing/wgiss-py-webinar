import numpy as np
import pandas as pd
from linearmodel import *

# Fourier decomposition
def fourierfilter(vi, fq_keep):
    """!
    Filter a time series using Fourier decomposition.
    @param vi      pandas.Series: A time series
    @param fq_keep int: The number of low frequencies to keep
    @return        Return a numpy.ndarray with filtered values for each element in vi.
    """
    vi = pd.Series(vi.values, index = range(len(vi.values)))               # re-build the series
    fdf = pd.DataFrame({'vi': vi})
    ## de-trend the time series by fitting a trend line
    fdf['vi_lm'] = fitline(fdf['vi'])
    fdf['residual'] = fdf['vi'] - fdf['vi_lm']
    # compute the discrete Fourier Transform
    vi_fft = np.fft.fft(fdf['residual'].values).real
    # remove the frequencies from index fq_keep to the last one
    vi_fft[fq_keep:] = 0
    # compute the inverse discrete Fourier Transform
    vi_ifft = np.fft.ifft(vi_fft).real
    # add the residuals back
    return(vi_ifft + fdf['vi_lm'].values)
