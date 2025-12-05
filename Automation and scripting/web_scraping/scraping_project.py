# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
import requests
from bs4 import BeautifulSoup

#url = "http://127.0.0.1:5500/baseball_stats.html"
#response = requests.get(url)
with open("baseball_stats.html","r") as f:
    response = f.read()
#soup = BeautifulSoup(response.text, "html.parser")
soup = BeautifulSoup(response, "html.parser")

#print(soup.prettify())

# Step 3.2: Extract the Required Data
table = soup.find("table")
print(table.prettify())

# Step 4.1: Convert to a DataFrame
import pandas as pd
df = pd.read_html(str(table))[0]
print(df)

# Convert the game data into a pandas DataFrame
print(df.columns)

# Inspect the DataFrame
print(df.values)
print(df)

# Save and print the shaped data
### YOUR CODE HERE ###

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
df.to_csv("sports_statistics.csv",index=False)