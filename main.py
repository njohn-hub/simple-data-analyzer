import pandas as pd
import matplotlib.pyplot as plt

# load the dataset 
data = pd.read_csv('students.csv')

# basic information 
print("Dataset Shape: ")
print(data.shape)
print(data.columns)

print("\nFirst five rows: ")
print(data.head())

# score statistics 
def analyze_score(data):
    average = data['score'].mean()
    median = data['score'].median()
    highest = data['score'].max()
    lowest = data['score'].min()
    
    print(f"Average score: {average:.2f}")
    print(f"Median score: {median:.2f}")
    print(f"Highest score: {highest:.2f}")
    print(f"Lowest score: {lowest:.2f}")
    
analyze_score(data)

# students with scores of 90 or higher 
def get_top_students(data, minimum_score=90):
    return data[data['score'] >= minimum_score][
        ['name', 'grade', 'score']
    ]

print(get_top_students(data, 90))


# average score by grade 
def score_by_grade(data):
    average_by_grade = (data.groupby('grade')['score'].mean().round(2))
    print('\nAverage Score by Grade: ')
    print(average_by_grade)
    
    average_by_grade.to_csv("average_scores_by_grade.csv")

score_by_grade(data)


# study hours and score correlation
correlation = data['study_hours'].corr(data["score"])

print(f"\nStudy Hours Vs. Score Correlation: {correlation:.2f}")


# scatter plot 

def scatter_plot(data):
    plt.scatter(data["study_hours"], data['score'])
    
    plt.xlabel("Study Hours")
    plt.ylabel("Test Score")
    plt.title("Study Hours Vs Test Scores ")
    
    plt.show()
    
scatter_plot(data)

print(data.isnull().sum())











