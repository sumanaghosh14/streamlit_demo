import streamlit as st

st.title("📊 Embedded Databricks Dashboard")
st.markdown("Below is the published dashboard embedded via iframe:")

dashboard_url = "https://lti-workspace-two.cloud.databricks.com/dashboardsv3/01f00d99b5c5117084b85ba766b28b54/published?o=262867458588239"

st.markdown(f"[🔗 Open Dashboard]({dashboard_url})", unsafe_allow_html=True)
