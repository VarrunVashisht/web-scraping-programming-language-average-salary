import requests
import csv
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

response =requests.get(url)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

data = []

for row in rows[1:]:  # skip header row
    cols = row.find_all('td')

    language = cols[1].getText().strip()
    salary = cols[3].getText().strip()

    data.append([language, salary])

for item in data:
    print(item)


# Save Data to CSV File

with open('popular-languages.csv',mode='w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Language", "Salary"])
    writer.writerows(data)

print("\n")
print("✅✅: Data saved successfully to popular-languages.csv")


