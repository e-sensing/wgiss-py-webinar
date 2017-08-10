import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from wtss import wtss
import json


def wtss_get_time_series(samples):
    
    # get wtss object
    w = wtss("http://www.dpi.inpe.br/tws")
    # get time series for each sample
    # create an empty data frame to store all time series
    data = pd.DataFrame()
    # traverse points, get data from wtss server and stores it
    for i in range(len(samples)):
        # request wtss
        ts = w.time_series("mod13q1_512", ("ndvi", "evi"), 
                           latitude=samples["latitude"][i], 
                           longitude=samples["longitude"][i], 
                           start_date=samples["start_date"][i],
                           end_date=samples["end_date"][i])
        # concatenate samples' time series
        data = pd.concat([data, 
                                pd.DataFrame({"id": i, 
                                              "label": samples["label"][i],
                                              "start_date": samples["start_date"][i],
                                              "latitude": samples["latitude"][i], 
                                              "longitude": samples["longitude"][i], 
                                              "timeline": pd.to_datetime(ts.timeline), 
                                              "ndvi": ts["ndvi"], 
                                              "evi": ts["evi"]},
                                             columns=["id", "label", "start_date", "latitude", "longitude", 
                                                      "timeline", "ndvi", "evi"])])
    return data


def plot_time_series(data):
    
    # get colors according to label
    labels, index_labels = np.unique(data.groupby("id").agg({"label": "first"})["label"], 
                                     return_inverse=True)
    colors = plt.cm.jet(plt.Normalize()(np.arange(len(labels))))
    
    # plot time series
    matplotlib.style.use("ggplot")
    fig, ax = plt.subplots(1)
    fig.subplots_adjust(bottom=0.2)

    # multiline plot with group by time serie id
    # compute days after the time series start date as x axis values
    for i, (key, grp) in enumerate(data.groupby(["id"])): 
        ax.plot((grp["timeline"] - pd.to_datetime(grp["start_date"])) / pd.Timedelta('1 days'), 
                grp["ndvi"], color=colors[index_labels][i])

    # plot legends
    plt.legend(handles=[matplotlib.lines.Line2D([], [], color=colors[i], 
                                                label=labels[i]) for i in range(len(colors))], 
               loc="upper center", ncol = 2, bbox_to_anchor=(0.5, -0.2))

    # plot axis labels 
    plt.xlabel("days after time series start date")
    plt.ylabel("ndvi")

    plt.show()

