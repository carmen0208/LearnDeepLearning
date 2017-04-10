from sklearn import linear_model

model = LinearRegression()
model.fit(x_values, y_values)
print(model.predict([127], [248]))

