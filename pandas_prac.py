print("hello world")
print("Testing Git push")

"""
print("Testing Git push")
print("Final test from correct file")
print("Pushing pandas_prac to GitHub")
"""

#pandas

import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [60000, 70000, 80000, 75000]
}

df = pd.DataFrame(data)
#display 

print("full data frame ")
print(df)
print("\n")  
 
print(df[['Name', 'Salary']])   

print("\n")
      
print(df[df['Salary'] > 70000])  

#Topic: read_csv, adding, renaming, and dropping columns

# ADDING THE CSV Column using pandas

print("\n")

# Step 4: Add Bonus and Total_pay
df["Bonus"] = df["Salary"] * 0.10
df["Total_pay"] = df["Bonus"] + df["Salary"]

print(" the df before step 5 ")
print(df)

# Step 5: Rename column
df.rename(columns={"Salary": "Base_Salary"}, inplace=True) # this is to rename 

# Drop Bonus column
df.drop("Bonus", axis=1, inplace=True) # this is to drop 

# Save to CSV
df.to_csv("cleaned_data.csv", index=False)

# Load back the cleaned CSV
df_new = pd.read_csv("cleaned_data.csv")

# Display head
print("Loaded Data from cleaned_data.csv:")
print(df_new.head())# its  like a print first few lines , like .head(3)  -> first 3 lines 
print("Ended task -2")

#task 3 

print("\nTask 3: Dropping 'Bonus' column")
if "Bonus" in df.columns:
    df.drop("Bonus", axis=1, inplace=True)
    print("Updated DataFrame after dropping 'Bonus':")
    print(df)
else:
    print("Bonus column not found.")


print(df)






