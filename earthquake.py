import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv("earthquake_data.csv")
    data = np.array(data)
    X = data[:, 0:-1]
    y = data[:, -1]
    X = X.astype('float')
    y = y.astype('float')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    pickle.dump(model, open('earthquake_model.pkl', 'wb'))

    model = pickle.load(open('earthquake_model.pkl', 'rb'))

    latitude = float(input("Enter the latitude: (The range is -90 to 90)\n"))
    longitude = float(input("Enter the longitude: (The range is -180 to 180)\n"))
    depth = float(input("Enter the depth (in kilometers):\n"))

    input_data = np.array([[latitude, longitude, depth]])

    prediction = model.predict(input_data)

    print("\nPredicted magnitude of the earthquake:", prediction[0])

    if prediction < 4:
        print("\nThe earthquake is of low intensity")
    elif 4 <= prediction < 6:
        print("\nThe earthquake is of moderate intensity")
    elif 6 <= prediction < 8:
        print("\nThe earthquake is of high intensity")
    elif prediction >= 9:
        print("\nThe earthquake is of very high intensity")
    else:
        print("\nUndefined")
        
    print("\nKeep yourself updated with the Earthquake warnings from the National Disaster Management Authority (NDMA) and the National Disaster Response Force (NDRF).\nStay safe!")    
    print("\nPlease note that this prediction is based solely on weather parameters and may not be entirely accurate. Other factors can significantly impact storm occurrences.")

if __name__ == "__main__":
    main()
