# Disaster Prediction System

Welcome to the Disaster Prediction System! This system predicts the occurrence of natural disasters based on weather parameters and the datasets of earlier parameters.

## Overview

The Disaster Prediction System utilizes AI technology, specifically machine learning models, to forecast three types of natural disasters: earthquake, flood, and hurricane. The system analyzes relevant weather parameters and historical data to make predictions about the intensity or likelihood of each disaster.

## Tech Stack

### Programming Language:
- **Python**: 
  - Primary language used for implementing the system's logic, data processing, and machine learning models.

### Machine Learning Libraries:
- **Scikit-learn**:
  - Used for building and training machine learning models for predicting natural disasters based on historical data and weather parameters.
- **TensorFlow**:
  - Employed for more complex machine learning tasks, such as deep learning-based models for disaster prediction.

### Data Processing:
- **Pandas**:
  - Used for data manipulation, preprocessing, and analysis, particularly for handling the historical datasets of earthquake, flood, and hurricane data.
- **NumPy**:
  - Essential for numerical computations and array manipulations, providing efficient data structures and operations for handling large datasets.

### Dependencies:
- **requirements.txt**:
  - A file listing all the required Python packages and their versions, ensuring reproducibility and easy setup of the project environment using pip.

### Other Libraries:
- Various additional libraries may have been used for tasks such as data visualization, user interface development, and handling file I/O.

## Installation

To run the Disaster Prediction System, follow these steps:

1. Clone the repository.
2. Install the required dependencies. ((use <pip install -r requirements.txt>))
3. Run the main script.


## Usage

1. Upon running the main script, you will be prompted with a menu to select the type of disaster you want to predict.

2. Enter the corresponding number for your choice and follow the instructions to provide the necessary input parameters (e.g., latitude, longitude, depth, windspeed, temperature, etc).

3. The system will use the AI model specific to the selected disaster type to predict the intensity or likelihood of the event.

4. The predicted result will be displayed, indicating the severity or category of the disaster.

5. You can continue using the system by selecting another disaster type or enter 0 to exit.

## Data

The Disaster Prediction System relies on datasets of historical earthquake, flood, and hurricane data. These datasets should be stored in separate CSV files named earthquake_data.csv, flood_data.csv, and storms_data.csv, respectively. Ensure that the data files are in the correct format and contain the required columns for training and prediction.

## Contributing

Contributions to the Disaster Prediction System are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue in the project repository.
