# The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data.

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

# statistics.mean(data) [Return the sample arithmetic mean of data.]
print('statistics.mean(data):', statistics.mean(data))

# statistics.median(data) [Return the median (middle value) of numeric data.]
print('sorted(data):', sorted(data))
print('statistics.median(data):', statistics.median(data))

# statistics.variance(data) [Return the sample variance of data.]
print('statistics.variance(data):', statistics.variance(data))