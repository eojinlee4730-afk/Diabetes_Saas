import pandas as pd
import plotly.express as px


def create_outcome_distribution_chart(df: pd.DataFrame):
    outcome_df = (
        df["Outcome"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    outcome_df.columns = ["Outcome", "Count"]

    fig = px.bar(
        outcome_df,
        x="Outcome",
        y="Count",
        title="Outcome Distribution"
    )
    return fig


def create_age_distribution_chart(df: pd.DataFrame):
    fig = px.histogram(
        df,
        x="Age",
        color="Outcome",
        barmode="overlay",
        title="Age Distribution by Outcome"
    )
    return fig


def create_glucose_distribution_chart(df: pd.DataFrame):
    fig = px.histogram(
        df,
        x="Glucose",
        color="Outcome",
        barmode="overlay",
        title="Glucose Distribution by Outcome"
    )
    return fig


def create_bmi_box_plot(df: pd.DataFrame):
    fig = px.box(
        df,
        x="Outcome",
        y="BMI",
        title="BMI by Outcome"
    )
    return fig


def create_glucose_bmi_scatter(df: pd.DataFrame):
    fig = px.scatter(
        df,
        x="Glucose",
        y="BMI",
        color="Outcome",
        size="Age",
        title="Glucose vs BMI"
    )
    return fig


def create_correlation_heatmap(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include="number")
    corr_df = numeric_df.corr()

    fig = px.imshow(
        corr_df,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )
    return fig
