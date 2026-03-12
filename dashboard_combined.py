import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import plotly.express as px


# Load datasets
projects_df = pd.read_csv("india_projects_dataset.csv")
complaints_df = pd.read_csv("india_complaints_dataset.csv")

st.title("India Governance Dashboard")
col1, col2, col3 = st.columns(3)

col1.metric("Total Projects", len(projects_df))
col2.metric("Total Complaints", len(complaints_df))
col3.metric("Active Issues", len(complaints_df[complaints_df["status"]=="Open"]))
# State selector
states = sorted(projects_df["state"].unique())
selected_state = st.selectbox("Select State", states)

# Filter data
state_projects = projects_df[projects_df["state"] == selected_state]
state_complaints = complaints_df[complaints_df["state"] == selected_state]

# Calculate map center
center_lat = state_projects["latitude"].mean()
center_lon = state_projects["longitude"].mean()

# Create map
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=7,
    tiles="cartodbpositron"
)

# Clusters
project_cluster = MarkerCluster(name="Projects").add_to(m)
complaint_cluster = MarkerCluster(name="Complaints").add_to(m)

# -------------------------
# Add Project Markers
# -------------------------
for _, row in state_projects.iterrows():

    popup_text = f"""
    <b>Project</b><br>
    District: {row['district']}<br>
    Type: {row['project_type']}<br>
    Budget: ₹{row['budget_crore']} Cr<br>
    Progress: {row['progress_percent']}%
    """

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_text,
        icon=folium.Icon(color="blue", icon="building")
    ).add_to(project_cluster)

# -------------------------
# Add Complaint Markers
# -------------------------
for _, row in state_complaints.iterrows():

    popup_text = f"""
    <b>Complaint</b><br>
    District: {row['district']}<br>
    Issue: {row['issue_type']}<br>
    Severity: {row['severity']}<br>
    Status: {row['status']}
    """

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_text,
        icon=folium.Icon(color="red", icon="exclamation-sign")
    ).add_to(complaint_cluster)

# Layer toggle
folium.LayerControl().add_to(m)



# Display map
st.subheader(f"Map View: {selected_state}")
st_folium(m, width=900, height=500)

# -------------------------
# Complaints Table
# -------------------------
st.subheader("Complaints")
def color_status_complaints(val):
    if val == "Resolved":
        return "background-color:#1b5e20; color:white"
    elif val == "In Progress":
        return "background-color:#ff8f00; color:white"
    else:
        return "background-color:#b71c1c; color:white"


styled_df = state_complaints[
    [
        "district",
        "issue_type",
        "severity",
        "status"
    ]
].style.applymap(color_status_complaints, subset=["status"])
st.dataframe(styled_df, use_container_width=True)

# Projects Table
# -------------------------
st.subheader("Development Projects")
def color_status_projects(val):
    if val == "Completed":
        return "background-color:#1b5e20; color:white"
    elif val == "Near Completion":
        return "background-color:#ff8f00; color:white"
    else:
        return "background-color:#b71c1c; color:white"
styled_df = state_projects[
    [
        "district",
        "project_type",
        "budget_crore",
        "progress_percent",
        "status"
    ]
].style.applymap(color_status_projects, subset=["status"])

st.dataframe(styled_df, use_container_width=True)




st.subheader("Complaints by State")

complaints_state = complaints_df.groupby("state").size().reset_index(name="count")

fig = px.bar(
    complaints_state,
    x="state",
    y="count",
    color="count",
    title="Complaint Distribution Across States"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("Most Common Issues")

issue_counts = complaints_df.groupby("issue_type").size().reset_index(name="count")

fig = px.pie(
    issue_counts,
    values="count",
    names="issue_type",
    title="Complaint Type Distribution"
)

st.plotly_chart(fig)
st.subheader("Project Status Distribution")

status_counts = projects_df.groupby("status").size().reset_index(name="count")

fig = px.bar(
    status_counts,
    x="status",
    y="count",
    color="status",
    title="Development Project Status"
)

st.plotly_chart(fig)
st.subheader("Complaint Severity")

severity_counts = complaints_df.groupby("severity").size().reset_index(name="count")

fig = px.bar(
    severity_counts,
    x="severity",
    y="count",
    color="severity",
    title="Severity Distribution"
)

st.plotly_chart(fig)
alerts = complaints_df.groupby("district").size().sort_values(ascending=False).head(5)

st.warning("⚠ High Priority Districts")

st.write(alerts)