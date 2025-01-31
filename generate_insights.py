import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
current_quiz_data = pd.read_csv('current_quiz_data.csv')
historical_quiz_data = pd.read_csv('historical_quiz_data.csv')

# Function to generate insights for a specific student
def generate_student_insights(student_id):
    # Filter data for the specific student
    student_current_data = current_quiz_data[current_quiz_data['student_id'] == student_id]
    student_historical_data = historical_quiz_data[historical_quiz_data['student_id'] == student_id]

    # Check if the student exists in the data
    if student_current_data.empty or student_historical_data.empty:
        print(f"No data found for student ID: {student_id}")
        return

    # 1. Weak Areas: Topics with the lowest scores
    weak_areas = student_current_data.groupby('topic')['score'].mean().sort_values().reset_index()
    print(f"\nWeak Areas for Student {student_id}:")
    print(weak_areas)

    # Visualize weak areas
    plt.figure(figsize=(10, 6))
    sns.barplot(x='topic', y='score', data=weak_areas, hue='topic', palette='viridis', legend=False)
    plt.title(f'Weak Areas for Student {student_id}')
    plt.xlabel('Topic')
    plt.ylabel('Average Score')
    plt.xticks(rotation=45)
    plt.show()

    # 2. Improvement Trends: Historical performance over quizzes
    improvement_trends = student_historical_data.groupby('quiz_id')['score'].mean().reset_index()
    print(f"\nImprovement Trends for Student {student_id}:")
    print(improvement_trends)

    # Visualize improvement trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='quiz_id', y='score', data=improvement_trends, marker='o')
    plt.title(f'Improvement Trends for Student {student_id}')
    plt.xlabel('Quiz ID')
    plt.ylabel('Average Score')
    plt.grid(True)
    plt.show()

    # 3. Performance Gaps: Compare student's performance with overall average
    overall_avg_score = current_quiz_data.groupby('topic')['score'].mean().reset_index()
    student_avg_score = student_current_data.groupby('topic')['score'].mean().reset_index()
    performance_gaps = pd.merge(overall_avg_score, student_avg_score, on='topic', suffixes=('_overall', '_student'))
    performance_gaps['gap'] = performance_gaps['score_overall'] - performance_gaps['score_student']
    print(f"\nPerformance Gaps for Student {student_id}:")
    print(performance_gaps)

    # Visualize performance gaps
    plt.figure(figsize=(10, 6))
    sns.barplot(x='topic', y='gap', data=performance_gaps, hue='topic', palette='coolwarm', legend=False)
    plt.title(f'Performance Gaps for Student {student_id}')
    plt.xlabel('Topic')
    plt.ylabel('Score Gap (Overall - Student)')
    plt.xticks(rotation=45)
    plt.show()

# Generate insights for a specific student (change the student_id as needed)
student_id = 1  # Replace with the student ID you want to analyze
generate_student_insights(student_id)