#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:08:12 2019

@author: christian
"""

# Import cdsapi and create a Client instance
import cdsapi
c = cdsapi.Client()
# More complex request
c.retrieve("reanalysis-era5-single-levels", {
        "product_type":   "reanalysis",
        "format":         "netcdf",
        "area":           "-5/-80/-15/-70",
        "variable":       "all",
        "year":           "2017",
        "month":          "01",
        "day":            ["01","02"],
        "time":           ["00", "01", "02",  "03", "04", "05",
                           "06", "07", "08",  "09", "10", "11",
                           "12", "13", "14",  "15", "16", "17",
                           "18", "19", "20",  "21", "22", "23",
                           ]
    }, "data/era5_single_levels_data.nc")

