#!/bin/bash

conda env create -f netCDF4_env.yml
eval "$(conda shell.bash hook)"
conda activate netCDF4_env
python3 Vulcan_v3_US_annual_1km_total_mn_map.py
