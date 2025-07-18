<<<<<<< HEAD


print("hello world")
print("Testing Git push")
=======
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


>>>>>>> 8fac6914946ae906c85146939a143c54f58c8d93
