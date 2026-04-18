import plotly.express as px
import pandas as pd

def create_sales_by_region_chart(df: pd.DataFrame):
    """
    Create bar chart for sales by region.
    """

    if "region" not in df.columns or "sales" not in df.columns:
        return None

    chart_df = df.groupby("region", as_index=False)["sales"].sum()

    fig = px.bar(
        chart_df,
        x="region",
        y="sales",
        title="Sales by Region"
    )

    return fig


def create_category_distribution_chart(df: pd.DataFrame):
    """
    Create pie chart for category distribution.
    """

    if "category" not in df.columns or "sales" not in df.columns:
        return None

    chart_df = df.groupby("category", as_index=False)["sales"].sum()

    fig = px.pie(
        chart_df,
        names="category",
        values="sales",
        title="Category Distribution"
    )

    return fig


def create_trend_chart(df: pd.DataFrame):
    """
    Create time-series trend chart.
    """

    if "date" not in df.columns or "sales" not in df.columns:
        return None

    chart_df = (
        df.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        chart_df,
        x="date",
        y="sales",
        title="Sales Trend"
    )

    return fig
