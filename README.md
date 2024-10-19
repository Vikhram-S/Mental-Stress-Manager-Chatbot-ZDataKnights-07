# Mental Stress Manager Chatbot - Team Z Data Knights - SAV07
This project is designed to help users assess their stress levels and provide personalized suggestions for managing stress. The chatbot collects user data such as age, gender, sleep quality, physical activity, and health metrics, and uses a RandomForestRegressor model to predict the user's stress level.

# Features
Interactive chatbot powered by Gradio.
Gathers information such as age, gender, occupation, health stats, and lifestyle habits.
Predicts stress level using a trained RandomForestRegressor model.
Provides tailored suggestions based on the predicted stress level (High, Medium, Low).
Includes an intuitive UI, suitable for non-technical users.

# Model Performance
The model was trained on a Public dataset from Kaggle, and performance was evaluated using the following metrics:

Root Mean Squared Error (RMSE): 0.1515
Mean Squared Error (MSE): 0.0229
Mean Absolute Error (MAE): 0.0427
R-squared (R²): 0.9927
Cross-validation was also performed using Stratified K-Fold:

Average RMSE: 0.2101
Average MAE: 0.0546
Average R-squared: 0.9859
# Installation and Usage

2. Install the required packages:
pip install -r requirements.txt

# Access the chatbot:
The chatbot will launch a local server, which you can access via your browser to interact with the bot.

# How It Works
1. Data Collection:
The chatbot collects data from the user interactively, such as:

Gender
Age
Occupation
Sleep Duration and Quality
Physical Activity Level
Health Metrics (BMI, Blood Pressure, Heart Rate, etc.)
2. Stress Prediction:
The collected data is fed into the trained RandomForest model, which predicts the user's stress level based on these inputs.

3. Suggestions:
The chatbot provides personalized recommendations to help manage stress, depending on whether the predicted stress level is low, medium, or high.

# Gradio Interface
The chatbot uses the Gradio library for a simple and effective web-based interface. The chatbot can be used to:

Start conversations
Assess stress levels
Provide stress management tips
Dataset
The dataset includes various factors that contribute to stress levels, such as age, gender, occupation, health statistics, and lifestyle habits. The data is one-hot encoded and split into training and test sets for the model.

# Model Details
The RandomForestRegressor is used to predict the stress level based on the following features:

Age
Sleep Duration
Quality of Sleep
Physical Activity Level
Heart Rate
Blood Pressure
Occupation
BMI Category
Sleep Disorders
Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

# Team 
1.Vikhram S
2.Nitesh Kumar B
3.Ragul S
4.Roshan R
# License
This project is licensed under the MIT License.





