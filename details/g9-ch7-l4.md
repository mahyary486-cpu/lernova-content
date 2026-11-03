# Measures of Center and Spread

A single number can describe where data is centered, and another can describe how spread out it is.

## Measures of center
- **Mean:** the sum of the values divided by how many there are.
- **Median:** the middle value of the ordered data. With an even count, average the two middle values.
- **Mode:** the value that occurs most often. A set can have no mode or more than one.

## Measures of spread
- **Range** = maximum - minimum.
- **Interquartile range (IQR)** = Q3 - Q1. It measures the spread of the middle half of the data.
- **Mean absolute deviation (MAD):** the mean of the distances of the values from the mean.
- **Standard deviation:** a typical distance from the mean. A larger value means more spread.

## Example 1: center and range
Data: 4, 6, 6, 8, 11.
1. Mean = (4 + 6 + 6 + 8 + 11) / 5 = 35 / 5 = 7.
2. Median = 6 (the middle of five ordered values).
3. Mode = 6.
4. Range = 11 - 4 = 7.

## Example 2: even number of values
Data: 3, 5, 9, 15.
1. Median = (5 + 9) / 2 = 7.
2. Lower half 3, 5 gives Q1 = 4. Upper half 9, 15 gives Q3 = 12.
3. IQR = 12 - 4 = 8.

## Example 3: mean absolute deviation
Data: 2, 4, 6, 8. The mean is 5.
1. Distances from 5: 3, 1, 1, 3.
2. Sum = 8.
3. MAD = 8 / 4 = 2.

## Effect of outliers
Add the value 100 to 4, 6, 6, 8, 11. The mean jumps from 7 to 135 / 6 = 22.5, but the median only moves from 6 to 7. The mean and range are sensitive to outliers. The median and IQR are resistant. So for skewed data or data with outliers, the median and IQR describe the data better. For symmetric data, the mean and standard deviation work well.

A common rule marks a value as an outlier if it is below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR.

## Common mistakes
- Finding the median without ordering the data first.
- Dividing by the wrong count when computing the mean.
- Thinking the mode is the number of times a value occurs rather than the value itself.
- Using the mean to describe a heavily skewed data set.
