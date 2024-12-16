import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data from the current directory
file_path = "stockholm_updated.csv"

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    
    # Display the first few rows of the dataframe
    st.write(data.head())
    
    # Check if 'TG' column exists
    if 'TG' in data.columns:
        # Create a histogram of the 'TG' column
        fig, ax = plt.subplots()
        ax.hist(data['TG'], bins=30, edgecolor='black')
        ax.set_title('Histogram of TG (Temperature Observations)')
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Frequency')
        
        # Display the histogram
        st.pyplot(fig)
    else:
        st.write("The 'TG' column does not exist in the provided CSV file.")
else:
    st.write("The file 'stockholm_updated.csv' was not found in the current directory.")
