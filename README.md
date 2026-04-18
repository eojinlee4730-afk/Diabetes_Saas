# Portfolio Dashboard

## Overview
This project is a multi-page data dashboard built with Streamlit.  
It provides interactive data exploration, filtering, and visualization, and is designed as a portfolio project demonstrating data engineering and analytics capabilities.

---

## Features
- Multi-page dashboard structure
- Interactive sidebar filters
- Summary metrics (row count, total values, unique categories)
- Data visualization using Plotly
- Raw data inspection and CSV download
- Modular code structure (data loading, filtering, chart generation)
- Optional database integration (SQLAlchemy)
- Automated data pipeline using GitHub Actions

---

## Project Structure

```
repo/
├── app/
│   ├── __init__.py
│   ├── streamlit_app.py
│   ├── data_loader.py
│   ├── db.py
│   ├── queries.py
│   ├── filters.py
│   ├── charts.py
│   └── pages/
│       ├── 1_Dashboard.py
│       ├── 2_Region_Analysis.py
│       └── 3_Raw_Data.py
├── scripts/
│   └── push_realtime.py
├── data/
│   ├── raw_diabetes_data.csv
│   └── processed_diabetes_data.csv
├── requirements.txt
└── README.md
```
---

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- SQLAlchemy (optional)
- GitHub Actions

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the application
streamlit run app/streamlit_app.py

---

## Deployment
This project can be deployed using Streamlit Community Cloud.

- Main file: app/streamlit_app.py
- requirements.txt must be in the root directory

---

## Data
- Data is stored in the `data/` directory
- Raw and processed datasets are separated
- Replaceable with any structured dataset

---

## Automation (Optional)
A GitHub Actions workflow is included to simulate a realtime data pipeline.

- Runs on a schedule
- Executes scripts/push_realtime.py
- Can be extended to:
  - Fetch external data
  - Update database
  - Trigger analytics

---

## Notes
- Application code is in `app/`
- Pipeline scripts are in `scripts/`
- Modular structure for scalability

---

## Future Improvements
- Add advanced visualizations
- Connect to production database
- Implement authentication
- Optimize caching
- Improve UI/UX

---

## Author
This project is created as part of a data analytics portfolio.

---

## Data Source & License
This project uses publicly available datasets from Kaggle.

- License: CC0 (Public Domain)
- This means the data can be used, modified, and distributed without restriction.

Dataset source:
- https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset/data

All data usage in this project complies with the original license terms.

---

## AI Usage Disclosure
This project was developed with the assistance of AI tools (e.g., ChatGPT).

AI was used for:
- Code structuring and refactoring
- Documentation drafting
- General development support

All final implementation, validation, and design decisions were reviewed and adjusted manually.

---

## Disclaimer
This project is for educational and portfolio purposes only.
