# 📊 YouTube Trending Data Pipeline

This project automates the process of downloading, cleaning, and loading YouTube trending data into a SQL Server database using Python.

---

## 🚀 Project Overview

As part of my journey in mastering data engineering skills, I built an end-to-end data pipeline using:
- **Python (with Pandas, Requests, pyodbc)**
- **SQL Server (SSMS)**
- **GitHub for version control**

The project is designed to simulate a real-world data ingestion and preparation process.

---

## 🛠️ What I've Done

- ✅ **Downloaded the dataset** from Google Drive using Python
- ✅ **Cleaned the data** using Pandas (removed duplicates, nulls, bad lines)
- ✅ **Exported** the cleaned data to a new CSV file
- ✅ **Loaded** the cleaned data into a `youtubeTrending` table in SQL Server
- ✅ **Structured** the project for future analysis using Power BI or Excel
- ✅ **Documented** the project and code on GitHub

---

## 🧾 File Descriptions

| File                | Description                                     |
|---------------------|-------------------------------------------------|
| `youtube_pipeline.py` | Downloads and cleans the dataset               |
| `load_data.py`        | Loads the cleaned data into SQL Server         |
| `Trending_Cleaned.csv`| Cleaned dataset (optional, can be regenerated) |
| `requirements.txt`    | Python packages used                           |
