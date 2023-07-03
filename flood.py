import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def main():
    
    data = pd.read_csv("flood_data.csv")

    data = np.array(data)
    X = data[:, 0:-1]
    y = data[:, -1]
    X = X.astype('float')
    y = y.astype('int')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    pickle.dump(model, open('flood_model.pkl', 'wb'))

    model = pickle.load(open('flood_model.pkl', 'rb'))

    max_temp = float(input("Enter the maximum temperature (in Celsius): "))
    min_temp = float(input("Enter the minimum temperature (in Celsius): "))
    rainfall = float(input("Enter the rainfall amount (in mm): "))
    humidity = float(input("Enter the humidity (in percentage): "))
    wind_speed = float(input("Enter the wind speed (in km/h): "))

    input_data = np.array([[max_temp, min_temp, rainfall, humidity, wind_speed]])

    prediction = model.predict(input_data)


    if prediction == 1:
        print("\nFlood is predicted.")
    else:
        print("\nNo flood is predicted.")
 
          
    print("\nKeep yourself updated with the flood warnings from the National Disaster Management Authority (NDMA) and the National Disaster Response Force (NDRF).\nStay safe!")
    
    print("\nPlease note that flood prediction based solely on weather parameters may not be accurate. Other factors, such as local topography and infrastructure, can significantly impact flood occurrences.")

if __name__ == "__main__":
    main()
