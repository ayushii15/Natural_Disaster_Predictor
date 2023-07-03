import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def main():
    
    data = pd.read_csv("storms_data.csv")
    X = data[['Latitude', 'Longitude', 'Wind', 'Pressure']].values
    y = data['Storm_Type'].values
    X = X.astype('float')
    y = y.astype('object')  

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)


    pickle.dump(model, open('storm_model.pkl', 'wb'))


    model = pickle.load(open('storm_model.pkl', 'rb'))


    latitude = float(input("Enter the latitude: "))
    longitude = float(input("Enter the longitude: "))
    wind_speed = float(input("Enter the wind speed (in km/h): "))
    pressure = float(input("Enter the pressure: "))

    input_data = np.array([[latitude, longitude, wind_speed, pressure]])


    prediction = model.predict(input_data)

    if prediction == 'tropical depression':
        print("\nA tropical depression is predicted.")
    elif prediction == 'tropical storm':
        print("\nA tropical storm is predicted.")
    elif prediction == 'hurricane':
        print("\nA hurricane is predicted.")
    else:
        print("\nNo storm prediction.")
    print("\nKeep yourself updated with the storm warnings from the National Disaster Management Authority (NDMA) and the National Disaster Response Force (NDRF).\nStay safe!")
    print("\nPlease note that this prediction is based solely on weather parameters and may not be entirely accurate. Other factors can significantly impact storm occurrences.")

if __name__ == "__main__":
    main()
