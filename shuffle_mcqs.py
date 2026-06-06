import pandas as pd
import random

# Read original CSV file
df = pd.read_csv(r"C:\Users\dhaks\Downloads\600_Biology_MCQs sheets.csv")

shuffled_questions = []

for index, row in df.iterrows():

    # Skip rows with missing options
    if pd.isna(row["Option_A"]) or pd.isna(row["Option_B"]) or pd.isna(row["Option_C"]) or pd.isna(row["Option_D"]):
        print(f"Skipping row {index+1}: Missing option")
        continue

    # Skip rows with missing answer
    if pd.isna(row["Answer"]):
        print(f"Skipping row {index+1}: Missing answer")
        continue

    # Store original options
    options = [
        str(row["Option_A"]).strip(),
        str(row["Option_B"]).strip(),
        str(row["Option_C"]).strip(),
        str(row["Option_D"]).strip()
    ]

    # Correct answer text from CSV
    correct_answer_text = str(row["Answer"]).strip()

    print(f"Row {index+1} Answer = {correct_answer_text}")

    # Shuffle options
    random.shuffle(options)

    # Find new answer position
    if options[0] == correct_answer_text:
        new_answer = "A"
    elif options[1] == correct_answer_text:
        new_answer = "B"
    elif options[2] == correct_answer_text:
        new_answer = "C"
    elif options[3] == correct_answer_text:
        new_answer = "D"
    else:
        print(f"Row {index+1}: Answer not found in options")
        continue

    shuffled_questions.append({
        "Question": row["Question"],
        "Option_A": options[0],
        "Option_B": options[1],
        "Option_C": options[2],
        "Option_D": options[3],
        "Answer": new_answer
    })

# Create new dataframe
shuffled_df = pd.DataFrame(shuffled_questions)

# Save shuffled CSV
shuffled_df.to_csv(
    "biology_mcqs_shuffled.csv",
    index=False,
    encoding="utf-8-sig"
)

print("===================================")
print("MCQ Shuffling Completed Successfully")
print("Output File: biology_mcqs_shuffled.csv")
print("Total Questions:", len(shuffled_df))
print("===================================")