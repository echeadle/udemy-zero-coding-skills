import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Load the data from the current directory
file_path = "stockholm_updated.csv"

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    
    # Display the first few rows of the dataframe
    st.write(data.head())
    
    # Check if 'TG' and 'DATE' columns exist
    if 'TG' in data.columns and 'DATE' in data.columns:
        # Convert 'DATE' column to datetime format
        data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
        
        # Extract year from 'DATE' column
        data['Year'] = data['DATE'].dt.year
        
        # Aggregate temperatures by year
        yearly_data = data.groupby('Year')['TG'].mean().reset_index()
        
        # Dropdown for selecting temperature unit
        unit = st.selectbox('Select temperature unit', ['Celsius', 'Fahrenheit'])
        
        # Convert temperatures if Fahrenheit is selected
        if unit == 'Fahrenheit':
            yearly_data['TG'] = yearly_data['TG'].apply(celsius_to_fahrenheit)
            ylabel = 'Average Temperature (°F)'
        else:
            ylabel = 'Average Temperature (°C)'
        
        # Plot the yearly temperatures as a bar graph
        fig, ax = plt.subplots()
        ax.bar(yearly_data['Year'], yearly_data['TG'], color='skyblue')
        ax.set_title('Yearly Average Temperatures')
        ax.set_xlabel('Year')
        ax.set_ylabel(ylabel)
        plt.xticks(rotation=45)
        
        # Display the bar graph
        st.pyplot(fig)
    else:
        st.write("The 'TG' and/or 'DATE' columns do not exist in the provided CSV file.")
else:
    st.write("The file 'stockholm_updated.csv' was not found in the current directory.")
