# **LogSentinel: Automated Log Monitoring & Alert System**

## **📌 Project Overview**
**LogSentinel** is an **IT Automation & AI/ML-powered log monitoring system** that automatically detects critical system issues in real-time. By leveraging **event-driven automation** and **intelligent pattern recognition**, LogSentinel eliminates the need for manual log reviews, ensuring rapid incident detection and response.

This project is designed to **showcase IT automation skills** using Python, demonstrating **real-world system monitoring, alerting, and AI-powered log intelligence**.

---

## **🚀 Key Features & Technologies**
| Feature | Technology Used | Purpose |
|----------|----------------|---------|
| **Real-Time Log Monitoring** | `watchdog` | Automatically tracks log file updates |
| **Automated Log Generation** | `logging` | Simulates system events (INFO, WARNING, ERROR, CRITICAL) |
| **Intelligent Log Filtering** | `re (regex)` | Detects and alerts on critical errors |
| **Automated Alert System** | `os, time` | Writes alerts to `alerts.log` for review |
| **Future AI/ML Potential** | `scikit-learn` (optional) | Can be expanded for anomaly detection |

---

## **✅ IT Automation in LogSentinel**
### **1️⃣ Automated Log File Generation**
- `generate_log.py` **simulates system activity** by generating structured log files.
- Logs include events like **INFO (system status), WARNING (potential issues), ERROR (failures), and CRITICAL (urgent alerts).**
- Runs **on a schedule** or manually to **simulate real-time system behavior.**

### **2️⃣ Automated Log Monitoring & Alerting**
- `monitor_logs.py` **automatically scans log updates** without manual intervention.
- Uses **`watchdog`** to monitor the log file **in real-time**.
- When an **ERROR** or **CRITICAL** log entry appears, it:
  ✅ **Prints an alert** in the console.  
  ✅ **Logs the alert** in `alerts.log` (simulating an email notification).  

### **3️⃣ Hands-Free, Event-Driven Execution**
- Runs **continuously** in the background.
- **Event-driven automation** ensures **efficient resource usage** (triggers only on file changes).
- IT teams **no longer need to manually inspect logs**—critical issues are flagged immediately.

---

## **🤖 AI/ML Aspects in LogSentinel**
### **1️⃣ Intelligent Log Analysis (Regex-Based NLP)**
- Instead of a simple "contains error" check, LogSentinel uses **regular expressions (`re`)** to:
  ✅ Detect only meaningful logs (`ERROR`, `CRITICAL`, `FAILURE`).  
  ✅ Ignore normal logs (`INFO`, `WARNING`).  
  ✅ Simulate **natural language processing (NLP) for log filtering**.

### **2️⃣ Future Expansion: Machine Learning for Anomaly Detection**
- LogSentinel can be upgraded with **ML models (Isolation Forest, LSTMs)** to detect **unusual error patterns**.
- Instead of **keyword-based detection**, ML would **identify anomalies** like:
  🚀 **Sudden spikes in error frequency**.
  🚀 **Unusual patterns in system failures**.
- This can predict system failures **before they happen**.

---

## **📂 Folder Structure**
```
LogSentinel/
│── data/                     # Stores generated logs & alerts
│   ├── logfile.log           # Main log file (monitored in real-time)
│   ├── alerts.log            # Simulated email alerts (error notifications)
│
│── scripts/                  # Python automation scripts
│   ├── generate_log.py       # Auto-generates logs (simulating system events)
│   ├── monitor_logs.py       # Monitors logs & triggers alerts
│
│── README.md                 # Project documentation
```

---

## **⚡ How to Run This Project**
### **1️⃣ Install Dependencies**
Ensure you have Python installed. Then, install required packages:
```sh
pip install watchdog
```

### **2️⃣ Generate Logs (Simulate System Events)**
```sh
python scripts/generate_log.py
```
This will create and append logs in `data/logfile.log`.

### **3️⃣ Start Monitoring Logs (Real-Time Alerting)**
```sh
python scripts/monitor_logs.py
```
If an **ERROR** or **CRITICAL** issue is detected, it will **print an alert** and log it to `alerts.log`.

### **4️⃣ Check Alerts**
```sh
type data/alerts.log
```
This file stores all alerts, simulating an email notification system.

---

## **🎯 Why This Project Matters**
✅ **Demonstrates IT Automation** → Hands-free log monitoring & alerting.  
✅ **Showcases AI-like NLP** → Intelligent log filtering via regex pattern recognition.  
✅ **Scalable for AI/ML** → Can be expanded with anomaly detection for predictive analytics.  
✅ **Real-World Application** → Similar techniques are used in **SOC (Security Operations Centers), DevOps monitoring, and cloud log management tools (Splunk, Datadog, AWS CloudWatch).**  

---

## **🚀 Future Enhancements**
🔹 **Email Alerts via SMTP** → Send real emails instead of logging alerts.  
🔹 **Slack Notifications** → Send real-time alerts to a Slack channel.  
🔹 **Machine Learning-Based Log Analysis** → Identify anomalies before failures occur.  

---

## **💡 Final Thoughts**
LogSentinel is a **powerful showcase of IT automation**, with the flexibility to scale into AI-driven monitoring. It’s a perfect **portfolio project** demonstrating hands-free log management, automation, and smart error detection using Python.

👨‍💻 **Built for IT, DevOps, and AI enthusiasts!** 🚀

