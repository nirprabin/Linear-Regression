# -*- coding: utf-8 -*-
"""

@author: Pravin Bhandari (1001401535)
"""

#Import tools and Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_excel('JavaSalary.xlsx') #- Read the file)
##data.head()   - Display first 5 data


#Create arrays
X= data.iloc[:, 0].values.reshape(-1, 1)
Y= data.iloc[:, 1].values.reshape(-1, 1)

#Perform Linear Regression
regressor = LinearRegression()
regressor.fit(X, Y)
Y_pred = regressor.predict(X)

#Data Visualtization
plt.scatter(X, Y, color='blue')
plt.xlabel('Years of Experience') #Title for X axis
plt.ylabel('Annual Salary') #title for Y Axis
plt.title('Average Salary of Java Contractor\n') #Title of the whole plot
plt.plot(X, Y_pred, color='green') #plot the new prediction and years of experience
plt.show()

