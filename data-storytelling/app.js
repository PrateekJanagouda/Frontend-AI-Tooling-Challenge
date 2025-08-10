const API_URL = "https://harman.ssi.iviva.cloud/Lucy/Bosch_new_static/getAverageVehicleCount";
// const API_KEY = "SC:hdemo:b7100e5a54712a0e";

// Toggle between live API and sample data
const USE_SAMPLE_DATA = false; // true for offline mode

async function fetchData() {
    if (USE_SAMPLE_DATA) {
        const res = await fetch("sample_data.json");
        return res.json();
    }

    try {
        const res = await fetch(API_URL, {
            headers: { Authorization: `APIKEY ${API_KEY}` }
        });
        if (!res.ok) throw new Error("API request failed");
        return res.json();
    } catch (error) {
        console.error("API failed, loading sample data...", error);
        const res = await fetch("sample_data.json");
        return res.json();
    }
}

function calculateMovingAverage(data, windowSize = 3) {
    const totals = data.map(d => d.upward + d.downward);
    return totals.map((_, idx) => {
        if (idx < windowSize - 1) return null;
        const window = totals.slice(idx - windowSize + 1, idx + 1);
        return Math.round(window.reduce((a, b) => a + b) / window.length);
    });
}

function analyzeData(data) {
    const hours = data.map(d => d.hour);
    const upwardCounts = data.map(d => d.upward);
    const downwardCounts = data.map(d => d.downward);
    const totalCounts = data.map(d => d.upward + d.downward);

    // Moving average
    const movingAvg = calculateMovingAverage(data, 3);

    // Totals
    const totalVehicles = totalCounts.reduce((a, b) => a + b, 0);
    document.getElementById("totalVehicles").textContent = totalVehicles.toLocaleString();

    // Peak hours
    const peakHours = [...data]
        .sort((a, b) => (b.upward + b.downward) - (a.upward + a.downward))
        .slice(0, 3);

    document.getElementById("peakHours").innerHTML = peakHours
        .map(h => `<li>${h.hour} (${h.upward + h.downward} vehicles)</li>`)
        .join("");

    // Anomalies detection
    const mean = totalVehicles / totalCounts.length;
    const stdDev = Math.sqrt(totalCounts.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) / totalCounts.length);

    const anomalies = data.filter(h => Math.abs((h.upward + h.downward) - mean) > 1.5 * stdDev);

    document.getElementById("anomalies").innerHTML = anomalies
        .map(h => {
            const diff = h.upward + h.downward - mean;
            const type = diff > 0 ? "Spike" : "Drop";
            return `<li>${h.hour} (${h.upward + h.downward} vehicles) - ${type}</li>`;
        })
        .join("");

    // Insight text
    document.getElementById("insightText").textContent =
        `Traffic peaks at ${peakHours[0].hour} with ${peakHours[0].upward + peakHours[0].downward} vehicles. 
        Average hourly traffic is about ${Math.round(mean)} vehicles. 
        ${anomalies.length} unusual traffic spikes/drops detected.`;

    // Render charts
    renderCharts(hours, upwardCounts, downwardCounts, totalCounts, movingAvg);
    renderHeatmap(data);
}

function renderCharts(hours, upwardCounts, downwardCounts, totalCounts, movingAvg) {
    // Line Chart
    const ctx1 = document.getElementById("trafficLineChart").getContext("2d");
    new Chart(ctx1, {
        type: "line",
        data: {
            labels: hours,
            datasets: [
                { label: "Upward", data: upwardCounts, borderColor: "blue", fill: false },
                { label: "Downward", data: downwardCounts, borderColor: "red", fill: false },
                { label: "Moving Avg (3h)", data: movingAvg, borderColor: "orange", fill: false, borderDash: [5, 5] }
            ]
        }
    });

    // Stacked Bar Chart
    const ctx2 = document.getElementById("stackedBarChart").getContext("2d");
    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: hours,
            datasets: [
                { label: 'Upward', data: upwardCounts, backgroundColor: 'blue', stack: 'traffic' },
                { label: 'Downward', data: downwardCounts, backgroundColor: 'red', stack: 'traffic' }
            ]
        },
        options: {
            responsive: true,
            scales: { x: { stacked: true }, y: { stacked: true } }
        }
    });
}

function renderHeatmap(data) {
    const container = document.getElementById("heatmap");
    container.innerHTML = "";
    data.forEach(d => {
        const total = d.upward + d.downward;
        const intensity = Math.min(255, Math.round((total / 2000) * 255)); // scale color
        const cell = document.createElement("div");
        cell.className = "heatmap-cell";
        cell.style.backgroundColor = `rgb(255, ${255 - intensity}, ${255 - intensity})`;
        cell.title = `${d.hour}: ${total} vehicles`;
        container.appendChild(cell);
    });
}

// Initial load
fetchData().then(analyzeData);
