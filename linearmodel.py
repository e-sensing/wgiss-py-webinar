import numpy
import pandas as pd
from scipy import stats

# fit a line to a time series
def fitline(vi):
    """!
    Fit a line to a time series.
    @param vi pandas.Series: A time series
    @return   Return a numpy.ndarray with the values of the fitted line for each element in vi.
    """

    vi = pd.Series(vi.values, index = range(len(vi.values)))                       # re-build the series
    obid = pd.Series(range(len(vi.values)), index = range(len(vi.values)))         # add an index to the series
    sl, it, r, p, sde = stats.linregress(x = range(len(vi.values)), y = vi.values) # fit the line
    lmdf = pd.DataFrame({'obid': obid, 'vi': vi})                                  # build a data frame
    lmdf['vi_lm'] = lmdf['obid'] * sl + it                                         # compute the line's points
    return(lmdf['vi_lm'].values)
