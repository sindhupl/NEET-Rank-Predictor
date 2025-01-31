import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
current_quiz_data = pd.read_csv('current_quiz_data.csv')
historical_quiz_data = pd.read_csv('historical_quiz_data.csv')
# Display basic information about the datasets
print("Current Quiz Data Overview:")
print(current_quiz_data.info())
print("\nHistorical Quiz Data Overview:")
print(historical_quiz_data.info())

# Display the first few rows of each dataset
print("\nCurrent Quiz Data Sample:")
print(current_quiz_data.head())
print("\nHistorical Quiz Data Sample:")
print(historical_quiz_data.head())

# Analyze patterns in student performance
# 1. Performance by topics
if 'topic' in current_quiz_data.columns:
    topic_performance = current_quiz_data.groupby('topic')['score'].mean().reset_index()
    print("\nAverage Performance by Topic:")
    print(topic_performance)

    # Visualize performance by topic
    plt.figure(figsize=(10, 6))
    sns.barplot(x='topic', y='score', data=topic_performance, hue='topic', palette='viridis', legend=False)
    plt.title('Average Performance by Topic')
    plt.xticks(rotation=45)
    plt.show()

# 2. Performance by difficulty level
if 'difficulty' in current_quiz_data.columns:
    difficulty_performance = current_quiz_data.groupby('difficulty')['score'].mean().reset_index()
    print("\nAverage Performance by Difficulty Level:")
    print(difficulty_performance)

    # Visualize performance by difficulty level
    plt.figure(figsize=(8, 5))
    sns.barplot(x='difficulty', y='score', data=difficulty_performance, hue='difficulty', palette='viridis', legend=False)
    plt.title('Average Performance by Difficulty Level')
    plt.show()

# 3. Response accuracy analysis
if 'correct' in current_quiz_data.columns:
    accuracy_by_topic = current_quiz_data.groupby('topic')['correct'].mean().reset_index()
    print("\nResponse Accuracy by Topic:")
    print(accuracy_by_topic)

    # Visualize response accuracy by topic
    plt.figure(figsize=(10, 6))
    sns.barplot(x='topic', y='correct', data=accuracy_by_topic, hue='topic', palette='viridis', legend=False)
    plt.title('Response Accuracy by Topic')
    plt.xticks(rotation=45)
    plt.show()

# 4. Historical performance trends
if 'quiz_id' in historical_quiz_data.columns and 'score' in historical_quiz_data.columns:
    historical_performance = historical_quiz_data.groupby('quiz_id')['score'].mean().reset_index()
    print("\nHistorical Performance Trends:")
    print(historical_performance)

    # Visualize historical performance trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='quiz_id', y='score', data=historical_performance, marker='o')
    plt.title('Historical Performance Trends')
    plt.xlabel('Quiz ID')
    plt.ylabel('Average Score')
    plt.show()

# Save insights to a file (optional)
with open('data_insights.txt', 'w') as f:
    f.write("Average Performance by Topic:\n")
    f.write(str(topic_performance) + "\n\n")
    f.write("Average Performance by Difficulty Level:\n")
    f.write(str(difficulty_performance) + "\n\n")
    f.write("Response Accuracy by Topic:\n")
    f.write(str(accuracy_by_topic) + "\n\n")
    f.write("Historical Performance Trends:\n")
    f.write(str(historical_performance) + "\n\n")

print("\nData analysis completed. Insights saved to 'data_insights.txt'.")