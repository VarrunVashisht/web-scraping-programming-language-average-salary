# 📊 Web Scraping for Programming Language Trends

## 📌 Project Overview

This project demonstrates how to **collect structured data from websites using Python**.
It focuses on **web scraping fundamentals**, including downloading web pages, extracting information from HTML, and saving the extracted data into a CSV file for further analysis.

The project is designed for **beginners** who want to understand how data analysts collect real-world data from the web.

---

## 🎯 Project Objectives

By completing this project, you will learn how to:

* Download web pages using Python
* Parse HTML content using BeautifulSoup
* Extract:

  * Web links
  * Image URLs
  * Tabular data
    
* Scrape programming language names and average salaries
* Store scraped data into a CSV file
* Practice web scraping in a clean, step-by-step way

---

## 🛠 Tools & Technologies Used

* **Python 3**
* **Requests** – for downloading web pages
* **BeautifulSoup (bs4)** – for parsing HTML
* **CSV module** – for saving data
* **PyCharm** – development environment

---

## 🌐 Data Sources

The data used in this project is scraped from publicly available web pages provided for educational purposes.

### Websites Scraped

* IBM Homepage

  ```
  http://www.ibm.com
  ```

* Programming Languages & Salaries Dataset

  ```
  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html
  ```

---

## 📂 Project Structure

```
web-scraping-project/
│
├── web_scraping.py
├── popular-languages.csv
└── README.md
```

---

## 🚀 How the Project Works

### Step 1: Download the Webpage

The project uses the `requests` library to download HTML content from a webpage.

### Step 2: Parse HTML Content

BeautifulSoup is used to convert raw HTML into a searchable structure.

### Step 3: Extract Data

The script extracts:

* Programming language names
* Average annual salaries

### Step 4: Save Data

The extracted data is stored in a CSV file named:

```
popular-languages.csv
```

---

## 📄 Output Example

The CSV file contains data in the following format:

| Programming Language | Average Annual Salary |
| -------------------- | --------------------- |
| Python               | $114,383              |
| Java                 | $101,013              |
| JavaScript           | $110,981              |

---

## 📈 Why This Project Matters

This project builds **core data analyst skills**, including:

* Data collection
* Web scraping
* Data cleaning
* Data storage

These skills are essential for:

* Job market analysis
* Technology trend analysis
* Data-driven decision-making
* Capstone and real-world projects

---

## 📚 Learning Outcome

After completing this project, you will be able to:

* Scrape structured data from the web
* Understand HTML tables
* Automate data collection
* Prepare datasets for analysis

---

## 🧑‍💻 Author

**Varrun Vashisht**
Aspiring Data Analyst

---

## 📜 License

This project is created for **learning and educational purposes**.

