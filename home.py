import streamlit as st
import requests
import tensorflow as tf
import datetime as dt
from apikey import API_KEY

def get_data(CITY):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    response = requests.get(url).json()
    json_data = response

    return json_data  # Return the JSON data directly

def predict():
    page_bg_img=    """

        <style>
        [data-testid="stAppViewContainer"]
           {
                background-image: url('https://www.shutterstock.com/image-photo/rain-clouds-black-sky-textured-600nw-2154906427.jpg');
                background-size: cover;
            }
        </style>
        """
    st.markdown(page_bg_img,
        unsafe_allow_html=True
    )
    st.title('Cloud Burst Prediction ⛈️')
    CITY = st.text_input('Enter city name: ')

    if CITY:  # Check if CITY is not empty
        try:
            result = get_data(CITY)

            if result:
                # Extract relevant features from JSON data
                feature_names = ['coord.lat', 'coord.lon', 'main.temp', 'main.feels_like',
                                'main.pressure', 'main.humidity', 'wind.speed', 'wind.deg']

                extracted_features = [get_nested_value(
                    result, name) for name in feature_names]

                # Load the model outside the function to avoid loading it with every prediction
                if 'model' not in st.session_state:
                    st.session_state.model = tf.keras.models.load_model(
                        'api_model')

                model = st.session_state.model

                # Make the prediction
                pred = model.predict([extracted_features])
                pred[0] /= 3

                # Convert wind speed from m/s to km/h and round off to 2 decimal places
                wind_speed_kmh = round(result["wind"]["speed"] * 3.6, 2)

                # Display prediction result
                st.success(
                    f'Chances of a Cloud Burst in {CITY} is {pred[0][0]:.3f} %')

                # Display additional information using cards
                st.subheader('Additional Information:')
                
                # Temperature and Humidity Visualization
                st.subheader('Temperature and Humidity:')
                st.bar_chart({
                    'Temperature (K)': result["main"]["temp"],
                    'Humidity (%)': result["main"]["humidity"]
                })

                # Wind Speed Visualization
                st.subheader('Wind Speed:')
                st.text(f'Wind Speed: {wind_speed_kmh} km/h')
                st.progress(wind_speed_kmh / 100)  # Assuming max wind speed is 100 km/h

        except:
            st.error("Please enter a valid city name!")

def get_nested_value(obj, key):
    keys = key.split('.')
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            obj = obj[k]
        elif isinstance(obj, list) and len(obj) > 0:
            obj = obj[int(k)]
        else:
            return None
    return obj

if __name__ == '__main__':
    predict()