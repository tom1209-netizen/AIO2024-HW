import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from compute_correlation_cofficient import compute_correlation_cofficient
import numpy as np


data = pd.read_csv("./data/advertising.csv")


# Question 5
print("Question 5")
x = data['TV']
y = data['Radio']
corr_xy = compute_correlation_cofficient(x, y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")
print()


# Question 6
print("Question 6")
features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = compute_correlation_cofficient(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")
print()


# Question 7
print("Question 7")
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)
print()


# Question 8
print("Question 8")
print(data.corr())
print()


# Question 9
print("Question 9")
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True)
plt.show()
print()