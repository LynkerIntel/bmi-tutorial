import numpy as np
import pandas as pd

# Configure snowPy model options
rs_method = 1         # 1 = single threshold, 2 = dual threshold
rs_thresh = 2.5       # rain-snow temperature threshold when rs_method = 1 (°C)
snow_thresh_max = 1.5 # maximum all-snow temp when rs_method = 2 (°C)
rain_thresh_min = 4.5 # minimum all-rain temp when rs_method = 2 (°C)
ddf_max = 2           # maximum degree day melt factor (mm/day/°C)
ddf_min = 0           # minimum degree day melt factor (mm/day/°C)
tair_melt_thresh = 1  # air temperature threshold above which melt can occur (°C)
swe = 0               # initial snow water equivalent (mm)
melt = 0              # initial melt (mm)

# Initialize time information
time = 0.0            # current simulation time in seconds
time_step = 86400     # time step size in seconds
dayofyear = 274       # Day of year of simulation start (ex: 1 = Jan 1, 274 = Oct 1)
year = 2020           # year of simulation start


# Import the example SNOTEL data
forcing = pd.read_csv("../data/snotel_663_data.csv")
# print(forcing.head(10))

# Make an empty array to store the output data
swe_output = np.zeros(forcing.date.size)

# Loop through the data and run snowBMI
for i in range(forcing.date.size):

    # Get forcing info
    air_temperature = np.full(1, forcing.tair_c[i])
    precip = np.full(1, forcing.ppt_mm[i])

    # Assign precipitation phase
    # 0 = snow, 1 = rain
    if rs_method == 1:
        if air_temperature <= rs_thresh:
            ppt_phase = 0
        else:
            ppt_phase = 1
    elif rs_method == 2:
        if air_temperature <= snow_thresh_max:
            ppt_phase = 0
        elif air_temperature >= rain_thresh_min:
            ppt_phase = 1
        else:
            ppt_phase = (air_temperature - snow_thresh_max) / (rain_thresh_min - snow_thresh_max)
    else:
        raise RuntimeError("Invalid rain-snow partitioning method")

    # Compute snowfall and rainfall
    snowfall_mm = (1 - ppt_phase) * precip
    rainfall_mm = precip - snowfall_mm

    # Add new snowfall to swe
    swe += snowfall_mm

    # Compute degree day factor for melt calcs
    ddf = ((ddf_max + ddf_min) / 2) + (np.sin((dayofyear - 81) / 58.09) * ((ddf_max - ddf_min) / 2))

    # Compute potential melt
    if air_temperature > tair_melt_thresh:
        melt_pot_mm = (air_temperature - tair_melt_thresh) * ddf
    else:
        melt_pot_mm = 0

    # Compute total melt knowing melt can't exceed SWE
    melt = min(swe, melt_pot_mm)

    # Compute SWE taking melt into account
    swe -= melt

    # Add rainfall to melt
    # Yes, rainfall != melt, but this simple model assumes all rain is a land surface water flux
    melt += rainfall_mm

    # Output SWE
    swe_output[i] = swe

    # Advance model clock forward in time
    time += time_step
    if dayofyear == 365:  # check if day of year == 365
        if year % 4 != 0:  # if not leap year then increment to next year
            dayofyear = 1
            year += 1
        else:  # otherwise (ie, it's a leap year) add 1 day
            dayofyear += 1
    elif dayofyear == 366:  # check if end of a leap year and increment to next year
        dayofyear = 1
        year += 1
    else:  # otherwise add one day to clock
        dayofyear += 1

# Save model output
np.savetxt("../data/swe_sim_663.csv", swe_output, delimiter=",", fmt='%.2e', header = 'sim_swe_mm')