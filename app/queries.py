SELECT_ALL_RECORDS = """
SELECT *
FROM diabetes_data
"""

SELECT_SUMMARY_BY_REGION = """
SELECT
    region,
    COUNT(*) AS record_count,
    SUM(sales) AS total_sales,
    AVG(sales) AS average_sales
FROM diabetes_data
GROUP BY region
ORDER BY total_sales DESC
"""

SELECT_DAILY_TREND = """
SELECT
    date,
    SUM(sales) AS total_sales
FROM diabetes_data
GROUP BY date
ORDER BY date
"""
