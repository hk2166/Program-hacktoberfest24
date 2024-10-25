def get_percentile(rank, total_students):
    if rank < 1 or rank > total_students:
        raise ValueError("Rank must be between 1 and the total number of students")

    percentile = (total_students - rank + 1) / total_students * 100
    return round(percentile, 2) 

if __name__ == "__main__":
    try:
        your_rank = int(input("Enter your rank: "))
        total_students = int(input("Enter the total number of students: "))

        percentile = get_percentile(your_rank, total_students)
        print(f"Your percentile is: {percentile}%")
    except ValueError as e:
        print(f"Error: {e}")
