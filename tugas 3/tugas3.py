import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = (r'D:\unchdeep\smt 4\metnum\tugas 3\Student_Performance.csv')  # Use a raw string (r'...') or double backslashes
data = pd.read_csv(file_path)

# Extract relevant columns for Problem 2
X_questions = data['Sample Question Papers Practiced'].values.reshape(-1, 1)
y_performance = data['Performance Index'].values

# Method 1: Linear Regression
linear_model_q = sm.OLS(y_performance, sm.add_constant(X_questions)).fit()

# Method 3: Exponential Model (log transformation of y)
log_y_performance = np.log(y_performance)
exp_model_q = sm.OLS(log_y_performance, sm.add_constant(X_questions)).fit()

# Plotting the results
plt.figure(figsize=(14, 6))

# Linear Regression Plot
plt.subplot(1, 2, 1)
sns.scatterplot(x=data['Sample Question Papers Practiced'], y=data['Performance Index'], alpha=0.5)
plt.plot(data['Sample Question Papers Practiced'], linear_model_q.predict(sm.add_constant(X_questions)), color='red')
plt.xlabel('Sample Question Papers Practiced')
plt.ylabel('Performance Index')
plt.title('Linear Regression')

# Exponential Model Plot
plt.subplot(1, 2, 2)
sns.scatterplot(x=data['Sample Question Papers Practiced'], y=np.log(data['Performance Index']), alpha=0.5)
plt.plot(data['Sample Question Papers Practiced'], exp_model_q.predict(sm.add_constant(X_questions)), color='green')
plt.xlabel('Sample Question Papers Practiced')
plt.ylabel('Log of Performance Index')
plt.title('Exponential Regression')

plt.tight_layout()
plt.show()

# Print summaries
print(linear_model_q.summary())
print(exp_model_q.summary())
