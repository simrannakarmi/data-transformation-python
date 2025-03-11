# Data Transformation with Python
 
This project processes raw transaction data from a CSV file, fixes errors, and outputs a cleaned CSV file.  

## Features  
- Fixes 'ERROR' values in **Total Spent** by recalculating **Quantity × Price Per Unit**  
- Replaces missing/unknown values with `"Not Specified"`  
- Standardizes **date format (YYYY-MM-DD)**  
- Ensures numeric consistency in **Total Spent**  

## 🖥️ Technologies Used  
- **Python** (pandas)  

## How to Run  
1. Clone this repo:  
```bash
git clone https://github.com/your-username/data-transformation-python.git
```
2. Install dependencies:
   ```bash
   pip install pandas
   ```
4. Run the script:
   ```bash
   python transform_data.py
   ```
