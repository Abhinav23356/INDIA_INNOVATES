import pandas as pd
import random
from datetime import datetime, timedelta

# Major districts with coordinates
districts = [

("Delhi","New Delhi",28.6139,77.2090),
("Delhi","South Delhi",28.5245,77.1855),

("Maharashtra","Mumbai",19.0760,72.8777),
("Maharashtra","Pune",18.5204,73.8567),
("Maharashtra","Nagpur",21.1458,79.0882),
("Maharashtra","Nashik",19.9975,73.7898),

("Karnataka","Bengaluru",12.9716,77.5946),
("Karnataka","Mysuru",12.2958,76.6394),
("Karnataka","Mangaluru",12.9141,74.8560),

("Tamil Nadu","Chennai",13.0827,80.2707),
("Tamil Nadu","Coimbatore",11.0168,76.9558),
("Tamil Nadu","Madurai",9.9252,78.1198),

("Uttar Pradesh","Lucknow",26.8467,80.9462),
("Uttar Pradesh","Kanpur",26.4499,80.3319),
("Uttar Pradesh","Varanasi",25.3176,82.9739),

("Rajasthan","Jaipur",26.9124,75.7873),
("Rajasthan","Jodhpur",26.2389,73.0243),

("Gujarat","Ahmedabad",23.0225,72.5714),
("Gujarat","Surat",21.1702,72.8311),

("West Bengal","Kolkata",22.5726,88.3639),
("West Bengal","Howrah",22.5958,88.2636),

("Telangana","Hyderabad",17.3850,78.4867),
("Andhra Pradesh","Visakhapatnam",17.6868,83.2185),

("Kerala","Kochi",9.9312,76.2673),
("Kerala","Thiruvananthapuram",8.5241,76.9366),

("Bihar","Patna",25.5941,85.1376),

("Madhya Pradesh","Indore",22.7196,75.8577),
("Madhya Pradesh","Bhopal",23.2599,77.4126),

("Punjab","Amritsar",31.6340,74.8723),

("Haryana","Gurgaon",28.4595,77.0266),

("Odisha","Bhubaneswar",20.2961,85.8245),

("Assam","Guwahati",26.1445,91.7362),

("Jharkhand","Ranchi",23.3441,85.3096),

("Chhattisgarh","Raipur",21.2514,81.6296)

]

issue_types = [
"Road Damage",
"Garbage Collection",
"Water Supply Issue",
"Streetlight Failure",
"Sewage Leakage",
"Traffic Congestion",
"Public Transport Issue",
"Electricity Problem"
]

severity_levels = ["Low","Medium","High","Critical"]
status_types = ["Open","In Progress","Resolved"]

complaints = []
complaint_id = 1

for state,district,lat,lon in districts:

    # generate complaints per district
    num_complaints = random.randint(50,120)

    for i in range(num_complaints):

        date = datetime.now() - timedelta(days=random.randint(0,365))

        complaints.append({
            "complaint_id": complaint_id,
            "state": state,
            "district": district,
            "latitude": lat + random.uniform(-0.05,0.05),
            "longitude": lon + random.uniform(-0.05,0.05),
            "issue_type": random.choice(issue_types),
            "severity": random.choice(severity_levels),
            "status": random.choice(status_types),
            "date": date.date()
        })

        complaint_id += 1

df = pd.DataFrame(complaints)

df.to_csv("india_complaints_dataset.csv",index=False)

print("Dataset created:",len(df),"complaints")