import pandas as pd
import numpy as np

# Generate mock Current Quiz Data
np.random.seed(42)  # For reproducibility
num_students = 100
topics = ['Biology', 'Chemistry', 'Physics']
difficulties = ['Easy', 'Medium', 'Hard']
g
# Create mock data for current quiz
current_quiz_data = pd.DataFrame({
    'student_id': np.arange(1, num_students + 1),
    'topic': np.random.choice(topics, num_students),
    'difficulty': np.random.choice(difficulties, num_students),
    'score': np.random.randint(40, 100, num_students),  # Wider range of scores
    'correct': np.random.choice([0, 1], num_students)  # 0 = Incorrect, 1 = Correct
})
# Generate mock Historical Quiz Data
num_quizzes = 5
historical_quiz_data = pd.DataFrame({
    'student_id': np.repeat(np.arange(1, num_students + 1), num_quizzes),
    'quiz_id': np.tile(np.arange(1, num_quizzes + 1), num_students),
    'score': np.random.randint(30, 100, num_students * num_quizzes)  # Wider range of scores
})

# Save the mock datasets to CSV files
current_quiz_data.to_csv('current_quiz_data.csv', index=False)
historical_quiz_data.to_csv('historical_quiz_data.csv', index=False)

print("Mock data generated and saved as 'current_quiz_data.csv' and 'historical_quiz_data.csv'.")