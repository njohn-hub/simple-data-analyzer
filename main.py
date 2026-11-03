
import pandas as pd
import matplotlib.pyplot as plt


# 1. Load dataset
data = pd.read_csv("students.csv")


# 2. Basic dataset information
def inspect_data(data):
    print("\nDataset Shape:")
    print(data.shape)

    print("\nDataset Columns:")
    print(data.columns.tolist())

    print("\nDataset Information:")
    data.info()

    print("\nFirst Five Rows:")
    print(data.head())

    print("\nMissing Values:")
    print(data.isnull().sum())


# 3. Analyze scores
def analyze_score(data):
    scores = data["score"].dropna()

    print("\nScore Statistics:")
    print(f"Mean: {scores.mean():.2f}")
    print(f"Median: {scores.median():.2f}")
    print(f"Highest: {scores.max():.2f}")
    print(f"Lowest: {scores.min():.2f}")
    print(f"Standard Deviation: {scores.std():.2f}")


# 4. Get top-performing students
def get_top_students(data, minimum_score=90):
    return data.loc[
        data["score"] >= minimum_score,
        ["name", "grade", "score"]
    ].sort_values(by="score", ascending=False)


# 5. Average score by grade
def score_by_grade(data):
    average = data.groupby("grade")["score"].mean().round(2)

    print("\nAverage Score by Grade:")
    print(average)

    average.to_csv("average_scores_by_grade.csv")


# 6. Correlation analysis
def analyze_correlation(data):
    correlation = data["study_hours"].corr(data["score"])

    print(f"\nStudy Hours vs Score: {correlation:.2f}")


# 7. Scatter plot with regression line
def scatter_plot(data):
    clean_data = data.dropna(
        subset=["study_hours", "score"]
    )

    plt.figure(figsize=(9, 6))

    plt.scatter(
        clean_data["study_hours"],
        clean_data["score"],
        alpha=0.7,
        label="Students"
    )

    # Add regression line
    m, b = __import__("numpy").polyfit(
        clean_data["study_hours"],
        clean_data["score"],
        1
    )

    plt.plot(
        clean_data["study_hours"],
        m * clean_data["study_hours"] + b,
        label="Trend line"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Test Score")
    plt.title("Study Hours vs Test Scores")

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.show()


# 8. Run analysis
if __name__ == "__main__":

    inspect_data(data)

    analyze_score(data)

    print("\nTop Students:")
    print(get_top_students(data))

    score_by_grade(data)

    analyze_correlation(data)

    scatter_plot(data)
