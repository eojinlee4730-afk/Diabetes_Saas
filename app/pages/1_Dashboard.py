from data_loader import load_data
from filters import render_sidebar_filters, apply_filters
from charts import (
    create_outcome_distribution_chart,
    create_age_distribution_chart,
    create_glucose_distribution_chart,
    create_bmi_box_plot,
    create_glucose_bmi_scatter,
)
st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Diabetes Dashboard")

df = load_data()
filters = render_sidebar_filters(df)
filtered_df = apply_filters(df, filters)

total_records = len(filtered_df)
positive_rate = filtered_df["Outcome"].mean() * 100 if len(filtered_df) > 0 else 0
average_glucose = filtered_df["Glucose"].mean() if len(filtered_df) > 0 else 0
average_bmi = filtered_df["BMI"].mean() if len(filtered_df) > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", f"{total_records:,}")
col2.metric("Positive Outcome Rate", f"{positive_rate:.1f}%")
col3.metric("Average Glucose", f"{average_glucose:.1f}")
col4.metric("Average BMI", f"{average_bmi:.1f}")

fig1 = create_outcome_distribution_chart(filtered_df)
fig2 = create_age_distribution_chart(filtered_df)
fig3 = create_glucose_distribution_chart(filtered_df)
fig4 = create_bmi_box_plot(filtered_df)
fig5 = create_glucose_bmi_scatter(filtered_df)

st.plotly_chart(fig1, use_container_width=True)

col5, col6 = st.columns(2)
col5.plotly_chart(fig2, use_container_width=True)
col6.plotly_chart(fig3, use_container_width=True)

col7, col8 = st.columns(2)
col7.plotly_chart(fig4, use_container_width=True)
col8.plotly_chart(fig5, use_container_width=True)
