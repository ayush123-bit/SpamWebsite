# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:54:59 2024

@author: ayush
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:37:30 2024

@author: ayush
"""

import numpy as np
import pickle
import os
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model using os
model_path = os.path.join(os.path.dirname(__file__), 'spammodel.sav')
model = pickle.load(open(model_path, 'rb'))

# Load the feature extraction model (TfidfVectorizer) using os
vectorizer_path = os.path.join(os.path.dirname(__file__), "tfidf_vectorizer.sav")  # Assume you saved the TfidfVectorizer separately
vectorizer = pickle.load(open(vectorizer_path, 'rb'))

# Define the prediction function
def spam_prediction(input_message):
    # Transform the input message using the TfidfVectorizer
    input_data_tfidf = vectorizer.transform([input_message])
    
    # Make the prediction
    prediction = model.predict(input_data_tfidf)
    
    if prediction[0] == 0:
        return "Spam"
    else:
        return "Not Spam"

# Main function for the Streamlit web app
def main():
    # Set the title of the web app
    st.title("Spam Prediction Web App")
    
    # Get user input message
    input_message = st.text_area("Enter the message to check if it's spam", "")
    
    # Initialize the result variable
    result = ""
    
    # Button for prediction
    if st.button("Check"):
        # Call the prediction function with the message
        result = spam_prediction(input_message)
        
        # Show the result
        st.success(result)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
