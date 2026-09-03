from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv('data.csv')
x=df[['distance']]
y=df[["fare"]]
model=LinearRegression()
model.fit(x,y)
print(f"Coefficient:/slope/m {model.coef_[0]}")
print(f"Intercept/constant: {model.intercept_}")
prediction=model.predict(pd.DataFrame({'distance':[6]}))
print(f"Predicted fare for 6 miles: {prediction[0]}")

plt.scatter(x,y,label='Data points')
plt.plot(x,model.predict(x),color='red',label='Regression line')
plt.xlabel('Distance (miles)')
plt.ylabel('Fare ($)')
plt.title('Distance vs Fare')
plt.legend()
plt.show()