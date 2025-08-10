# 🚦 Traffic Data Dashboard

A modern, interactive traffic analytics dashboard built with **Vanilla JavaScript** and **Chart.js**, visualizing hourly vehicle counts, trends, and anomalies from live or sample data.

---

## 📌 Features

- **Live API Integration**  
  Fetches hourly traffic data using a provided API key.
  
- **Offline / Sample Mode**  
  Automatically falls back to local `sample_data.json` if API is unavailable.

- **Overview Cards**  
  Displays key metrics including:
  - Total Vehicles
  - Peak Hours
  - Detected Anomalies

- **Charts & Visualizations**
  - **Line Chart**: Upward & downward trends with optional moving average.
  - **Stacked Bar Chart**: Hourly breakdown of vehicle counts.
  - **Hourly Heatmap**: Quick-glance traffic intensity by hour.

- **Anomaly Detection**  
  Uses standard deviation to detect unusually high/low traffic hours.

- **Peak Hour Highlights**  
  Automatically lists top 3 busiest hours.

---

## 📂 Project Structure

├── index.html # Main dashboard HTML
├── app.js # Core logic: data fetching, processing, visualization
├── sample_data.json # Offline dataset for testing
└── README.md # Project documentation