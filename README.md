# 🇮🇳 AI Governance Co-Pilot Dashboard

## Overview

The **AI Governance Co-Pilot Dashboard** is an interactive data visualization platform designed to help public administrators and policy makers monitor **development projects and citizen complaints** across India.

The dashboard provides geographic insights, project monitoring tools, and analytics that support **data-driven governance and faster decision-making**.

It is built using:

* **Streamlit** – interactive dashboard framework
* **Folium** – geographic visualization
* **Pandas** – data processing
* **Plotly** – analytics and visualizations

The platform demonstrates how an **AI-assisted governance system** can help leaders understand problems at a district level and prioritize development actions.

---

# 🚀 Key Features

## 1. Interactive India Map

* Displays **development projects and citizen complaints geographically**
* Users can **select a state and zoom into it**
* Clustered markers improve map readability
* Popups show detailed information for each entry

Example information displayed:

* District
* Project type
* Budget
* Progress percentage
* Complaint issue type
* Severity level

---

## 2. Development Project Monitoring

Tracks infrastructure projects such as:

* Road Construction
* Bridge Development
* Hospital Infrastructure
* Water Supply Projects
* Smart City Infrastructure
* Renewable Energy Projects

Each project includes:

* District location
* Budget allocation
* Progress percentage
* Completion status

Projects are color-coded to easily identify progress.

---

## 3. Complaint Tracking System

The dashboard visualizes **citizen complaints across districts**.

Complaint attributes include:

* Issue type
* Severity level
* Current status
* Geographic location

Common complaint categories:

* Road damage
* Garbage collection
* Water supply
* Streetlight failure
* Traffic congestion
* Sewage leakage

---

## 4. Data Visualization & Analytics

The dashboard includes multiple analytical views such as:

* Complaint distribution by state
* Issue type analysis
* Project progress distribution
* Complaints vs projects comparison
* Severity analysis

These visualizations help identify:

* High-complaint districts
* Infrastructure gaps
* Development priorities

---

## 5. Project Status Tracking

Projects are categorized into three states:

| Status          | Meaning                    |
| --------------- | -------------------------- |
| Completed       | Infrastructure finished    |
| Near Completion | Project almost finished    |
| Ongoing         | Work currently in progress |

This helps decision makers monitor project implementation efficiency.

---

# 🗂 Dataset Information

Two synthetic datasets were generated to simulate real governance data.

### Development Projects Dataset

Contains information such as:

* State
* District
* Latitude & Longitude
* Project Type
* Budget (₹ Crore)
* Progress Percentage
* Project Status

### Complaints Dataset

Includes:

* Complaint ID
* State
* District
* Latitude & Longitude
* Issue Type
* Severity Level
* Status
* Date

These datasets simulate **real-world civic data used by government monitoring systems**.

---

# 🖥 Dashboard Screenshots

### Main Dashboard
```
<img width="946" height="824" alt="image" src="https://github.com/user-attachments/assets/5b7de8e9-f897-4dab-9520-4a5ce4db4d64" />
<img width="765" height="699" alt="image" src="https://github.com/user-attachments/assets/b25a3b36-10c4-4b40-a9d4-cbb7564b7796" />
```


### Map Visualization
```
<img width="843" height="697" alt="image" src="https://github.com/user-attachments/assets/df1c0194-ef4b-4b8c-b8bb-bbe9a06a4cbe" />
<img width="786" height="676" alt="image" src="https://github.com/user-attachments/assets/3e96fa9a-4e49-4a6f-a7bb-75a9a397ebdc" />
<img width="783" height="676" alt="image" src="https://github.com/user-attachments/assets/d272ed48-22b5-47b9-9506-5d93fa27a433" />
```




### Data Analytics
```
<img width="760" height="517" alt="image" src="https://github.com/user-attachments/assets/9cdce5b1-d875-4517-9b9f-fb0694a199de" />
<img width="739" height="457" alt="image" src="https://github.com/user-attachments/assets/5af19581-3c15-4bb5-832e-e8d224f97a66" />
<img width="733" height="494" alt="image" src="https://github.com/user-attachments/assets/e720e656-00aa-4d24-9fcb-3a07b07063a5" />
<img width="766" height="506" alt="image" src="https://github.com/user-attachments/assets/74ee6665-33c9-46b7-9994-61650bd72426" />
```





---

# 🧠 AI Governance Co-Pilot (Future Features)

The current dashboard represents the **foundation of an AI governance assistant**. Future versions will include advanced AI capabilities.

## AI Decision Support

* Automatic identification of **districts needing urgent attention**
* Infrastructure gap detection using complaint patterns
* Priority recommendations for policy makers

## AI Complaint Analysis

* NLP analysis of citizen complaints
* Automated categorization of issues
* Sentiment analysis for public feedback

## Predictive Governance

* Predict future complaint trends
* Detect districts likely to face infrastructure problems
* Forecast development needs

## Real-Time Data Integration

Integration with:

* municipal complaint portals
* smart city data streams
* IoT infrastructure sensors
* traffic monitoring systems

## Smart Alert System

AI-generated alerts such as:

⚠ Rising complaints in a district
⚠ Delayed development projects
⚠ Infrastructure risk detection

---

# 🌐 Long-Term Vision

The AI Co-Pilot aims to evolve into a **smart governance decision platform** that can assist:

* Public administrators
* Urban planners
* Policy makers
* Smart city command centers

The system will help governments transition toward **data-driven governance and intelligent public administration**.

---

# ⚙ Installation

Clone the repository:

```
git clone https://github.com/Abhinav23356/INDIA_INNOVATES.git
```

Install dependencies:

```
pip install streamlit pandas folium plotly streamlit-folium
```

Run the dashboard:

```
streamlit run dashboard.py
```

The application will launch in your browser.

---

# 📌 Future Work

Planned enhancements include:

* District-level heatmaps
* AI-driven project risk prediction
* Complaint resolution tracking
* Mobile-friendly dashboard interface
* Integration with real government datasets
* AI summarization of governance insights

---

