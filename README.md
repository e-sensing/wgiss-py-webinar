# WGISS Tech Webinar - Python for Data Science in Earth Observation Analysis

Click on *launch* to visit the live version of this notebook!
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/e-sensing/wgiss-py-webinar/master)


## Setup in Mac OS X

```bash
conda update conda
conda create --name geospatial python=2.7
source activate geospatial
conda install -c conda-forge scipy matplotlib pandas folium
conda install -c damianavila82 rise
conda install ipykernel
conda install nb_conda
python -m ipykernel install --user --name geospatial --display-name "Python [geospatial]"
pip install wtss
git clone https://github.com/e-sensing/wgiss-py-webinar.git
jupyter notebook
```


## Setup in Ubuntu 14

```bash
conda update conda
conda create --name geospatial python=2.7
source activate geospatial
conda install ipykernel nb_conda matplotlib scipy
conda install -c conda-forge folium
conda install -c damianavila82 rise
pip install wtss
python -m ipykernel install --user --name geospatial --display-name "Python [geospatial]"
git clone https://github.com/e-sensing/wgiss-py-webinar.git
cd wgiss-py-webinar
jupyter notebook
```

