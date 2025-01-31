import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the datasets
current_quiz_data = pd.read_csv('current_quiz_data.csv')
historical_quiz_data = pd.read_csv('historical_quiz_data.csv')

# Function to predict NEET rank for a specific student
def predict_neet_rank(student_id):
    # Filter data for the specific student
    student_current_data = current_quiz_data[current_quiz_data['student_id'] == student_id]
    student_historical_data = historical_quiz_data[historical_quiz_data['student_id'] == student_id]

    # Check if the student exists in the data
    if student_current_data.empty or student_historical_data.empty:
        print(f"No data found for student ID: {student_id}")
        return

    # Prepare data for rank prediction
    # Use historical quiz scores as features and assume a linear relationship with rank
    X = student_historical_data['quiz_id'].values.reshape(-1, 1)  # Quiz ID as feature
    y = student_historical_data['score'].values  # Score as target

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the score for the next quiz (quiz_id = 6)
    next_quiz_id = 6
    predicted_score = model.predict(np.array([[next_quiz_id]]))[0]

    # Assume a linear relationship between score and rank (lower score = higher rank)
    # For simplicity, we'll use a basic formula: Rank = Max Rank - (Score / Scaling Factor)
    max_rank = 100000  # Example: Maximum possible rank
    scaling_factor = 10  # Adjust this based on your data
    predicted_rank = max_rank - (predicted_score / scaling_factor)

    print(f"\nPredicted NEET Rank for Student {student_id}: {int(predicted_rank)}")

# Predict rank for a specific student (change the student_id as needed)
student_id = 1  # Replace with the student ID you want to analyze
predict_neet_rank(student_id)
# Function to predict the most likely college based on rank
def predict_college(predicted_rank):
    # Example college cutoff ranks (replace with actual data)
    college_cutoffs = {
        'AIIMS Delhi': 100,
        'JIPMER Puducherry': 500,
        'Maulana Azad Medical College': 1000,
        'King George’s Medical University': 5000,
        'Other Colleges': 100000
    }

    # Find the most likely college based on the predicted rank
    for college, cutoff in college_cutoffs.items():
        if predicted_rank <= cutoff:
            print(f"Most Likely College: {college}")
            break

# Define the predicted rank (you can replace this with an actual number or get user input)
predicted_rank = 600  # Example predicted rank

# Predict college for the predicted rank
predict_college(predicted_rank)
