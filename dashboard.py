import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load dataset
df = pd.read_csv("india_projects_dataset.csv")

st.title("India Development Projects Dashboard")

# State selector
states = sorted(df["state"].unique())
selected_state = st.selectbox("Select State", states)

# Filter dataset
state_data = df[df["state"] == selected_state]

# Calculate center of selected state
center_lat = state_data["latitude"].mean()
center_lon = state_data["longitude"].mean()

# Create map centered on selected state
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=7,
    tiles="cartodbpositron"
)

# Cluster for markers
cluster = MarkerCluster().add_to(m)

# Add project markers
for _, row in state_data.iterrows():

    popup_text = f"""
    State: {row['state']}<br>
    District: {row['district']}<br>
    Project: {row['project_type']}<br>
    Budget: ₹{row['budget_crore']} Cr<br>
    Progress: {row['progress_percent']}%
    """

    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_text
    ).add_to(cluster)

# Display map
st.subheader(f"Projects in {selected_state}")
st_folium(m, width=900, height=500)

# Written details
st.subheader("Project Details")

st.dataframe(
    state_data[
        [
            "district",
            "project_type",
            "budget_crore",
            "progress_percent",
            "status"
        ]
    ],
    use_container_width=True
)