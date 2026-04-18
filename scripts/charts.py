import streamlit as st
import pandas as pd

def show_outcome_distribution(df: pd.DataFrame):
    if "Outcome" in df.columns:
        st.subheader("Outcome Distribution")
        counts = df["Outcome"].value_counts().sort_index()
        st.bar_chart(counts)

def show_glucose_trend(df: pd.DataFrame):
    if "Glucose" in df.columns:
        st.subheader("Glucose Trend")
        st.line_chart(df["Glucose"])

def show_bmi_trend(df: pd.DataFrame):
    if "BMI" in df.columns:
        st.subheader("BMI Trend")
        st.line_chart(df["BMI"])

def show_age_distribution(df: pd.DataFrame):
    if "Age" in df.columns:
        st.subheader("Age Distribution")
        counts = df["Age"].value_counts().sort_index()
        st.bar_chart(counts)

def show_blood_pressure_trend(df: pd.DataFrame):
    if "BloodPressure" in df.columns:
        st.subheader("Blood Pressure Trend")
        st.line_chart(df["BloodPressure"])
