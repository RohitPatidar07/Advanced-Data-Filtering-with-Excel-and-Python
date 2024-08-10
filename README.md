# Employee Data Filtering and Excel Export Script

## Overview

This Python script processes employee data, filters it based on various conditions, and exports the filtered data to an Excel file. The script leverages the `pandas` library for data manipulation and `openpyxl` for Excel file operations.

## Features

- **Data Creation**: The script starts by creating a sample dataset containing employee details like EmployeeID, Name, Department, Position, HireDate, Salary, and Location.
  
- **Data Export**: The original dataset is exported to an Excel file named `EmployeeData.xlsx`, under the sheet name `OriginalData`.

- **Data Filtering**: The script applies several filtering techniques to the data:
  - **Basic Filter**: Filters employees from the IT department.
  - **Conditional Filter**: Filters employees with a salary greater than $70,000.
  - **Multi-Condition Filter**: Filters employees from the IT department with a salary greater than $70,000.
  - **GroupBy Filter**: Filters departments that have more than 2 employees.
  - **Regex Filter**: Filters employees whose position title contains the word "Manager".

- **Filtered Data Export**: The filtered datasets are appended to the same Excel file, each under different sheet names:
  - `Basic_Filter`
  - `Conditional_Filter`
  - `Multi_Condition_Filter`
  - `GroupBy_Filter`
  - `Regex_Filter`

## Usage

1. **Install Dependencies**: Ensure that `pandas` and `openpyxl` libraries are installed.
   ```bash
   pip install pandas openpyxl
