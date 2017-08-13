import numpy as np

def kalmanfilter(vi, e_mea = None, est_0 = None, e_est_0 = None):
    """!
    Filter a time series using the Kalman filter.
    @param vi      pandas.Series: A time series made of measurements
    @param e_mea   int: The error in the measurements
    @param est_0   int: The estimate of the first measurement
    @param e_est_0 int: The initial error in the estimate
    @return        Return a numpy.ndarray with filtered values for each element in vi.
    """
    est   = np.zeros(len(vi)) # estimation
    e_est = np.zeros(len(vi)) # error in estimation
    kg    = np.zeros(len(vi)) # Kalman gain
    # deal with missing values
    if est_0 is None:
        est[0]   = vi.mean()
    else:
        est[0]   = est_0
    if e_mea is None:
        e_mea = vi.std()
    if e_est_0 is None:
        e_est[0] = 3 * vi.std()
    else:
        e_est[0] = e_est_0
    # do the filtering
    kg[0]    = None
    for i in range(1, len(vi)):
        kg[i] = e_est[i - 1]/(e_est[i - 1] + e_mea)    # compute the Kalman gain
        m = vi[i - 1]
        if(np.isnan(m)):
            m = est[i - 1]                             # use the estimation when a measurement is missing
        est[i] = est[i - 1] + kg[i] * (m - est[i - 1]) # compute the new estimation
        e_est[i] = (1 - kg[i]) * e_est[i - 1]
    return est
