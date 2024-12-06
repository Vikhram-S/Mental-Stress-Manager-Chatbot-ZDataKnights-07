# %% [markdown]
# Importing Required Libraries

# %%
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import streamlit as st

# Set page configuration and styling
st.set_page_config(
    page_title="Mental Stress Manager", 
    page_icon="🧠",
    layout="wide"
)

# Custom CSS styling with dark/light mode compatibility
st.markdown("""
    <style>
    .main {
        background-color: transparent;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: var(--text-color);
        border-radius: 10px;
        padding: 10px 20px;
        margin: 5px;
        transition: transform 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .stSelectbox>div>div>select {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .user-message {
        background-color: rgba(76, 175, 80, 0.2);
    }
    .bot-message {
        background-color: rgba(76, 175, 80, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Load and prepare data
df = pd.read_csv("C:/Users/hpsli/Favorites/Downloads/Sleep_health_and_lifestyle_dataset.csv")
df_cleaned = df.drop_duplicates()
df_cleaned = df_cleaned.drop(columns=['Person ID'])

# Convert categorical variables
categorical_columns = ['Gender', 'Occupation', 'BMI Category', 'Blood Pressure', 'Sleep Disorder']
df_cleaned[categorical_columns] = df_cleaned[categorical_columns].astype('category')

# Prepare model data
df_encoded = pd.get_dummies(df_cleaned, drop_first=True)
X = df_encoded.drop(columns=['Stress Level'])
y = df_encoded['Stress Level']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

def main():
    # Title and description
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Mental Stress Manager</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Assess your stress level and get personalized suggestions</p>", unsafe_allow_html=True)

    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.user_data = {}

    # Questions flow
    questions = {
        0: {"text": "What is your gender?", "type": "select", "options": ["Male", "Female"]},
        1: {"text": "What is your age?", "type": "number"},
        2: {"text": "What is your occupation?", "type": "select", "options": list(df_cleaned['Occupation'].unique()) + ["Others"]},
        3: {"text": "How many hours do you sleep per day?", "type": "number"},
        4: {"text": "Rate your sleep quality (1-10):", "type": "slider", "min": 1, "max": 10},
        5: {"text": "Rate your physical activity level (1-10):", "type": "slider", "min": 1, "max": 10},
        6: {"text": "What is your BMI category?", "type": "select", "options": ["Normal", "Overweight", "Obese"]},
        7: {"text": "What is your systolic blood pressure?", "type": "number"},
        8: {"text": "What is your diastolic blood pressure?", "type": "number"},
        9: {"text": "What is your heart rate?", "type": "number"},
        10: {"text": "How many steps do you take daily?", "type": "number"},
        11: {"text": "Do you have any sleep disorders?", "type": "select", "options": ["None", "Sleep Apnea", "Insomnia"]}
    }

    # Display current question
    if st.session_state.step < len(questions):
        q = questions[st.session_state.step]
        st.markdown(f"<h3 style='color: #4CAF50;'>{q['text']}</h3>", unsafe_allow_html=True)
        
        if q['type'] == 'select':
            response = st.selectbox("Select an option", q['options'], key=f"q_{st.session_state.step}")
        elif q['type'] == 'number':
            response = st.number_input("Enter value", key=f"q_{st.session_state.step}")
        elif q['type'] == 'slider':
            response = st.slider("Select value", q['min'], q['max'], key=f"q_{st.session_state.step}")

        if st.button("Next"):
            st.session_state.user_data[st.session_state.step] = response
            st.session_state.step += 1
            st.experimental_rerun()

    # Show results
    elif st.session_state.step == len(questions):
        prediction = predict_stress(st.session_state.user_data)
        st.markdown(f"<div class='chat-message bot-message'>{prediction}</div>", unsafe_allow_html=True)
        
        if st.button("Start Over"):
            st.session_state.step = 0
            st.session_state.user_data = {}
            st.experimental_rerun()

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center;'>
            <p>Made with ❤️ by Team Stress Busters</p>
            <p style='font-size: 18px; font-weight: bold; color: #4CAF50;'>Development Team:</p>
            <p>Lead Developer: Vikhram S</p>
            <p>Co-Developers: Ragul S, Roshan R, Nithesh Kumar B</p>
        </div>
    """, unsafe_allow_html=True)

def predict_stress(user_data):
    # [Previous prediction logic remains the same]
    # Return prediction and suggestions formatted for Streamlit

if __name__ == "__main__":
    main()
