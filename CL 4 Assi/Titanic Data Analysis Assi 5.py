import pandas as pd

# Load Titanic dataset
data = pd.read_csv("/content/Titanic-Dataset.csv")

# Lists and dictionary to collect values
male_ages = []
female_deaths_by_class = {}

# Loop through each row
for index, row in data.iterrows():
    # Count male deaths and their ages
    if row["Sex"] == "male" and row["Survived"] == 0:
        if pd.notnull(row["Age"]):  # skip if Age is missing
            male_ages.append(row["Age"])

    # Count female deaths by class
    if row["Sex"] == "female" and row["Survived"] == 0:
        pclass = row["Pclass"]
        if pclass not in female_deaths_by_class:
            female_deaths_by_class[pclass] = 0
        female_deaths_by_class[pclass] += 1

# Calculate average age of dead males
if male_ages:
    avg_age = sum(male_ages) / len(male_ages)
else:
    avg_age = 0

# Show the results
print(f"Average age of males who died: {avg_age:.2f}")

print("Female deaths by class:")
for cls, count in female_deaths_by_class.items():
    print(f"  Class {cls}: {count} deaths")
