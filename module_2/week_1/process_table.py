import pandas as pd
import numpy as np

df = pd.read_csv('advertising.csv')
data = df.to_numpy()

print(data.shape)
print(f'Max: {max(data[:, 3])} - Index: {np.argmax(data[:, 3])}')
print(f'Mean of TV sale: {np.mean(data[:, 0])}')
print(f'Num of TV sale > 20: {np.sum(data[:, 3] >= 20)}')
print(f'Mean of Radio sale where Sales >= 15: {np.mean(data[data[:, 3] >= 15, 1])}')
print(f'Sum of Sales Newspaper sales >= Newspaper mean: {np.sum(data[data[:, 2] >= np.mean(data[:, 2]), 3])}')

# Q20
mean_sales = np.mean(data[:, 3])
scores = np.where(data[:, 3] > mean_sales, 'Good',
          np.where(data[:, 3] < mean_sales, 'Bad', 'Average'))

print(f'Divide Sales into 3 groups ( mean ): {scores[7:10]}')

# Q21
mean_sales_nearest_int = round(np.mean(data[:, 3]))

scores = np.where(data[:, 3] > mean_sales_nearest_int, 'Good',
          np.where(data[:, 3] < mean_sales_nearest_int, 'Bad', 'Average'))

print(f'Divide Sales into 3 groups ( approx into int ): {scores[7:10]}')