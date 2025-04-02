# 🧹 Cleanly: CSV Cleaner and EDA Tool

Cleanly is an interactive Streamlit-based tool that allows you to upload, clean, and analyze CSV files easily. It provides functionalities for data cleaning, outlier removal, data visualization, and exploratory data analysis (EDA).

## ✨ Features

- 📂 **CSV File Upload**: Upload CSV files for processing.
- 🧹 **Data Cleaning**:
  - 🗑️ Remove duplicate rows.
  - 🩹 Handle missing values (fill with mean or mode based on data type).
- 🚫 **Outlier Removal**:
  - 📊 Based on Z-Score.
  - 📈 Based on Interquartile Range (IQR).
- 📏 **Data Normalization**: Scale numeric values between 0 and 1.
- 🔢 **Categorical Column Encoding**: Convert categorical columns into numeric values.
- ✏️ **Rename and Delete Columns**: Modify or delete specific columns.
- 🔍 **Row Filtering and Sorting**: Filter rows based on specific values and sort data.
- 📊 **Data Visualization**:
  - 📉 Histograms.
  - 📊 Bar charts.
  - 🟢 Scatter plots.
  - 🔗 Correlation matrix.
- 📚 **Data Grouping**: Group data by columns and apply aggregation functions like mean, sum, count, etc.
- 💾 **Download Processed Data**: Download the cleaned and processed CSV file.

## 🛠️ Requirements

Before running the project, ensure you have the following dependencies installed:

- 🐍 Python 3.7 or higher
- 📦 Streamlit
- 📦 Pandas
- 📦 NumPy
- 📦 Seaborn
- 📦 Matplotlib

Install the dependencies by running:

```bash
pip install -r requirements.txt