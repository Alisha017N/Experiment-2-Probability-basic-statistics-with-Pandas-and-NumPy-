
import numpy as np
import pandas as pd

# Create an array of heights
heights = np.array([160, 165, 170, 175, 180, 155, 168, 172, 169, 158])

# Convert array into a Pandas Series
s = pd.Series(heights)

# Calculate mean
print("Mean:", s.mean())

# Calculate median
print("Median:", s.median())

# Calculate standard deviation
print("Std dev:", round(s.std(), 3))

# Calculate variance
print("Variance:", round(s.var(), 3))

# Calculate probability of height greater than 170
print("P(height > 170):", (s > 170).mean())

# Generate 10 random values from a normal distribution
sample = np.random.normal(
    loc=s.mean(),
    scale=s.std(),
    size=10
)

print("Random sample (10) from normal around mean:", np.round(sample, 2))
