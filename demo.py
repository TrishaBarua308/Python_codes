# Step 1: Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 2: Prepare dataset (last 7 days temperature)
# দিনগুলো: 1 থেকে 7 → একে আমরা X ধরছি
days = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)

# প্রতিদিনের তাপমাত্রা (Celsius) → এটাকে আমরা Y ধরছি
temperatures = np.array([30, 32, 31, 33, 34, 35, 36])

# Step 3: Create and train the model
model = LinearRegression()
model.fit(days, temperatures)

# Step 4: Predict temperature for next day (Day 8)
next_day = np.array([[8]])
predicted_temp = model.predict(next_day)

print(f"📅 Day 8 এর প্রেডিক্টেড তাপমাত্রা: {predicted_temp[0]:.2f}°C")

# Step 5: Optional: Plot the data and prediction
plt.scatter(days, temperatures, color='blue', label='Actual Temperature')
plt.plot(days, model.predict(days), color='green', label='Regression Line')
plt.scatter(next_day, predicted_temp, color='red', label='Predicted Temp (Day 8)')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Weather Forecasting using Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
