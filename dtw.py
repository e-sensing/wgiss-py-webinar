import numpy as np
import pandas as pd


def dtw(a, b, metric=1):
    # dtw main routine starts here
    # prepare parameters
    a = np.asarray(a)
    b = np.asarray(b)
    if a.ndim == 1:
        a.shape = (len(a), -1)
    if b.ndim == 1:
        b.shape = (len(b), -1)
    # compute local cost matrix
    # compute cross differences product
    m = np.abs([np.subtract.outer(a[:,i], b[:,i]) for i in range(a.shape[-1])])
    # sum multi-attribute time series to obtain an cost matrix of scalars
    m = np.sum(m ** metric, axis = 0)
    # dynamic search
    for i in range(0, m.shape[0]):
        for j in range(0, m.shape[1]):
            if i != 0 and j != 0:
                m[i, j] += min(m[i - 1, j - 1],
                               m[i, j - 1], 
                               m[i - 1, j])
            elif i == 0 and j != 0:
                m[i, j] += m[i, j - 1]
            elif i != 0 and j == 0:
                m[i, j] += m[i - 1, j]
    # compute metric and return dtw distance
    return m[-1, -1] ** (metric ** -1)


def classifier_1nn(patterns, samples):
    # create a dtw distance matrix rows = samples, cols = patterns
    samples_dist = [[dtw(p_grp["ndvi"], s_grp["ndvi"]) for p_key, p_grp in patterns.groupby(['id'])] 
                    for s_key, s_grp in samples.groupby(['id'])]
    # get minimum distances indexes
    classification = pd.DataFrame(
        {"id": np.asarray(samples.groupby("id").agg({"id": "first"})["id"]),
         "prediction": np.asarray(patterns.groupby("id").agg({"label": "first"})["label"])[np.argmin(samples_dist, axis = -1)],
         "reference": np.asarray(samples.groupby("id").agg({"label": "first"})["label"])},
        columns = ["id", "reference", "prediction"])
    # add a verification column and returns
    classification["correct"] = classification["reference"] == classification["prediction"]
    return classification

