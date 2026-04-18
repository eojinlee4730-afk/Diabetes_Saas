# Diabetes Analytics Dashboard

## Overview
This project is a multi-page data analytics dashboard built with Streamlit.  
It analyzes a healthcare dataset related to diabetes risk and provides interactive visualization, filtering, and exploration tools.

The application is connected to a Neon PostgreSQL database and retrieves realtime data from the `realtime_data` table.

[Live Dashboard](https://diabetessaas-application.streamlit.app/)

---

## Features
- Multi-page Streamlit dashboard
- Interactive filtering (Outcome, Age, Glucose, BMI, Pregnancies)
- Real-time data loading from Neon PostgreSQL
- Statistical summaries and KPI metrics
- Data visualization using Plotly
- Correlation analysis between medical features
- Raw data inspection and CSV download
- Modular architecture (data, filters, charts, pages)
- Automated pipeline support via GitHub Actions

---

## Project Structure
```text
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
│       ├── 2_Feature_Analysis.py
│       └── 3_Raw_Data.py
├── scripts/
│   └── push_realtime.py
├── data/
├── requirements.txt
└── README.md
```

---

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- SQLAlchemy
- PostgreSQL (Neon)
- GitHub Actions

---

## Data Source & License
This project uses a publicly available diabetes dataset from Kaggle.

- License: CC0 (Public Domain)
- The dataset can be used, modified, and distributed without restriction.

Dataset source:
- https://www.kaggle.com/ (replace with actual dataset link)

---

## Database
- Source: Neon PostgreSQL
- Table: `realtime_data`
- Data is loaded dynamically at runtime

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the app
streamlit run app/streamlit_app.py

---

## Deployment
This project is designed to be deployed on Streamlit Community Cloud.

- Main file: `app/streamlit_app.py`
- Ensure `requirements.txt` is in the root directory
- Add database credentials in Streamlit Secrets:



---

## Data Notes
Some zero values in physiological variables (e.g., Glucose, BloodPressure, BMI) may represent missing measurements rather than actual clinical values.

---

## AI Usage Disclosure
This project was developed with the assistance of AI tools (e.g., ChatGPT).

AI was used for:
- Code structuring and refactoring
- Documentation drafting
- General development support

All final implementation and design decisions were reviewed and adjusted manually.

---

## Future Improvements
- Add predictive modeling (diabetes risk classification)
- Integrate more advanced visualizations
- Improve UI/UX design
- Add user authentication
- Optimize performance for large datasets

---

## Author
This project is created as part of a data analytics portfolio.
