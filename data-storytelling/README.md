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

```
├── index.html           # Main dashboard HTML
├── app.js               # Core logic: data fetching, processing, visualization
├── sample_data.json     # Offline dataset for testing
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/traffic-dashboard.git
cd traffic-dashboard
```

### 2️⃣ Set API Key _(Optional)_

Open `app.js` and set your API key:

```javascript
const API_KEY = "your_api_key_here";
```

If no key is provided or the API fails, the dashboard will automatically load `sample_data.json`.

### 3️⃣ Run Locally

You can use a simple local server:

```bash
# Python 3
python -m http.server 8000

```

Then visit: [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📊 Data Format

Both API and sample data return an array of objects:

```json
[
  {
    "hour": "08:00",
    "upward": 601,
    "downward": 831,
    "vehicleType": "all"
  },
  ...
]
```

---

## 📈 Anomaly Detection Logic

An hour is flagged as anomalous if:

```
| total_vehicles(hour) - mean | > 1.5 × standard_deviation
```

This helps spot unusual spikes or drops in traffic.

---

## 🛠️ Built With

- [Chart.js](https://www.chartjs.org/) — For data visualization
- Vanilla JavaScript — For data processing & DOM updates
- HTML & CSS — Layout and styling

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Prateek Janagouda  
[GitHub Profile](https://github.com/PrateekJanagouda)

---
