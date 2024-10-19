Personalized Relationship Stress Manager
Project Overview
This project is part of the IBM Z Datathon 2024, created to address social issues through technology under the 'Tech for Good' theme. The Personalized Relationship Stress Manager is a machine learning-based tool designed to help individuals manage relationship stress and resolve conflicts. The solution includes a Gradio-based chatbot that interacts with users and provides personalized stress management advice based on machine learning predictions.

Features
Chatbot Interface: A Gradio chatbot that interacts with users, gathering data and offering personalized stress management solutions.
Stress Prediction: Utilizes the RandomForestRegressor for stress level predictions based on input data.
Cross-validation: Employs StratifiedKFold cross-validation for robust model performance.
Conflict Resolution: Offers personalized strategies to resolve relationship stress based on predictions.
Dataset
The dataset includes multiple factors influencing relationship stress. The model is trained on this data to predict stress levels and provide relevant advice.

Installation and Setup
Requirements
Python 3.x
Gradio
Jupyter Notebook
Libraries:
scikit-learn
pandas
numpy
matplotlib
Steps
Install the required libraries:
bash
Copy code
pip install -r requirements.txt
Launch the Gradio chatbot:
bash
Copy code
python chatbot.py
Usage
Chatbot Interface: The Gradio chatbot will ask users questions to assess their stress levels. Based on the responses, it will provide personalized stress management strategies.
Notebook: Open the Jupyter Notebook to explore the model development process, including data preprocessing, training, and evaluation.
Model Performance
The model has been evaluated using StratifiedKFold cross-validation to ensure balanced training. Key performance metrics include:

Accuracy: XX%
RMSE: XX
MAE: XX
Future Work
Implement deep learning models for improved prediction accuracy.
Expand the dataset to include a broader range of stress-related factors.
Extend the chatbot for real-time stress tracking and proactive management.
Contributing
Contributions are welcome! Fork the repository and create a pull request to contribute.

License
This project is licensed under the MIT License - see the LICENSE file for details.