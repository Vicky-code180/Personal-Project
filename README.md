# 911 Call Analysis Dashboard
## Overview
This project involves analyzing 911 call data from New York City to uncover patterns and trends in emergency calls. 
The analysis includes visualizing hourly and weekly trends, identifying the most common types of emergencies, and mapping hotspots for 911 calls across NYC boroughs. 
The insights are presented in an interactive Tableau dashboard.

---

### **Features**
- **Hourly Distribution of Calls**: Visualizes the busiest hours for 911 calls.
- **Weekly Trends**: Highlights call volumes by day of the week.
- **Top Emergency Reasons**: Displays the most common reasons for 911 calls.
- **Geospatial Distribution**: Maps call density across NYC boroughs.
- **Borough Distribution**: Shows call percentages across boroughs in a pie chart.
- **Interactive Filters**: Allows users to filter data by borough.
  ---

### **Key Insights**
1. **Hourly Peaks**: 
   - Most 911 calls are made between **4 PM and 7 PM**.
2. **Weekly Patterns**:
   - Wednesdays and Tuesdays have the highest call volumes, while weekends are relatively quieter.
3. **Top Emergency Types**:
   - Calls related to "Visibility Patrols" and "Investigations" dominate the dataset.
4. **Geospatial Hotspots**:
   - Brooklyn and Manhattan have the highest call densities, with noticeable hotspots in downtown areas.

---

### **Technology Used**
- **Tableau Public**: For creating the interactive dashboard.
- **Python (Pandas)**: For preprocessing and aggregating data.
- **Matplotlib**: For initial exploratory visualizations.
- **Dataset**: NYC 911 Call Dataset (Source: [NYC Open Data](https://opendata.cityofnewyork.us/)).

---
### How the Analysis Was Done
- **Data Preprocessing:**
Cleaned the dataset to ensure consistency in datetime formats.
Extracted useful features like hour, day_of_week, and month.
Grouped data for hourly, weekly, and monthly trends.
- **Visualization:**
Created plots for trends, patterns, and distributions using Tableau.
Added interactivity for filtering by time, borough, and emergency type.
- **Batch Processing:**
Handled the 5M+ row dataset by processing data in 200,000-row chunks for memory efficiency.
---
![911Analysis_Tableau](https://github.com/user-attachments/assets/45583752-e907-4a8f-b1c0-122064003026)
