import streamlit as st
import random
import time
st.title("Hospital Sensor Live Monitoring")
st.write("SImulating Live Sensor Data : Heart Rate, Temperature, Oxygen Level")

def sensor_data_stream():
    while True:
        yield{
            "heart_rate":random.randint(60,100),
            "temperature":round(random.uniform(97.0,100.0),1),
            "oxygen_level":random.randint(97,100)
        }
        time.sleep(1)

heart_rate_bar=st.progress(0)
temperature_bar=st.progress(0)
oxygen_bar=st.progress(0)

heart_rate_text=st.empty()
temperature_text=st.empty()
oxygen_text=st.empty()

for reading in sensor_data_stream():
    hr=reading["heart_rate"]
    temp=reading["temperature"]
    ox=reading["oxygen_level"]

    heart_rate_bar.progress(min(hr,100))
    temperature_bar.progress(int((temp-97)/3*100))
    oxygen_bar.progress(ox)

    heart_rate_text.text(f"Heart rate:{hr}bpm")
    print(f"Heart rate:{hr}bpm")
    temperature_text.text(f"Temperature:{temp}F")
    print(f"Temperature:{temp}F")
    oxygen_text.text(f"Oxygen Level:{ox}%")
    print(f"Oxygen Level:{ox}%")