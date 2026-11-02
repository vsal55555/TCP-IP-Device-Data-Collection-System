# TCP/IP Device Data Collection System

A real-time Device Monitoring and Data Collection System built using **C#**, **.NET Worker Service**, **TCP/IP Socket Programming**, **SQL Server**, **Entity Framework Core**, **Serilog**, and **Python Streamlit Dashboard**.

The system simulates multiple devices transmitting sensor readings over TCP/IP. Incoming data is collected by a .NET Worker Service, stored in SQL Server, logged using Serilog, monitored through an alert engine, and visualized through a real-time monitoring dashboard.

---

## Project Architecture

```text
+---------------------+
|  Device Simulator   |
|  DEV001             |
|  DEV002             |
|  DEV003             |
+----------+----------+
           |
           | TCP/IP
           v
+---------------------+
| .NET Worker Service |
| TCP Listener        |
+----------+----------+
           |
           +----------------+
           |                |
           v                v
+----------------+   +----------------+
| SQL Server     |   | Serilog Logs   |
| DeviceReadings |   | app-yyyyMMdd   |
+----------------+   +----------------+
           |
           v
+---------------------+
| Streamlit Dashboard |
+---------------------+
```

---

## Features

### Core Features

- TCP/IP Socket Communication
- Multi-Device Simulation
- Real-Time Data Collection
- JSON Message Processing
- Continuous Data Streaming
- SQL Server Storage
- Entity Framework Core Integration

### Monitoring Features

- Device Registry Management
- Device Readings Tracking
- Real-Time Dashboard
- Temperature Monitoring
- Humidity Monitoring
- Database Growth Tracking
- Alert Monitoring

### Reliability Features

- Serilog File Logging
- Error Logging
- Connection Logging
- Data Persistence
- Automatic Refresh Dashboard

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Language | C# |
| Backend Framework | .NET Worker Service |
| Communication Protocol | TCP/IP |
| Socket Programming | TcpListener / TcpClient |
| Database | SQL Server |
| ORM | Entity Framework Core |
| Logging | Serilog |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Language (Dashboard) | Python |
| Version Control | Git |
| Repository Hosting | GitHub |

---

## Database Schema

### Devices

```sql
Devices
-------
Id
DeviceId
DeviceName
IsActive
```

Example:

| DeviceId | DeviceName |
|-----------|------------|
| DEV001 | Temperature Sensor |
| DEV002 | Humidity Sensor |
| DEV003 | Pressure Sensor |

---

### DeviceReadings

```sql
DeviceReadings
--------------
Id
DeviceId
Temperature
Humidity
Timestamp
```

Sample Data:

| DeviceId | Temperature | Humidity |
|-----------|------------|------------|
| DEV001 | 31.91 | 83.59 |
| DEV002 | 26.11 | 79.79 |
| DEV003 | 33.78 | 41.11 |

---

### Alerts

```sql
Alerts
------
Id
DeviceId
Message
CreatedAt
```

Example:

```text
DEV003
High Temperature Detected
```

---

## Folder Structure

```text
TCP-IP-Device-Data-Collection-System
│
├── TcpDataCollector.Worker
│   ├── Data
│   ├── Models
│   ├── Services
│   ├── Migrations
│   ├── logs
│   ├── Program.cs
│   └── Worker.cs
│
├── DeviceSimulator
│   ├── Program.cs
│   └── Models
│
├── Dashboard
│   ├── app.py
│   ├── db.py
│   ├── components
│   │   ├── alerts.py
│   │   ├── database_growth.py
│   │   ├── devices.py
│   │   ├── humidity_trend.py
│   │   ├── kpi_row.py
│   │   ├── latest_readings.py
│   │   └── temperature_trend.py
│   │
│   └── requirements.txt
│
├── docs
│   ├── architecture.png
│   └── screenshots
│
└── README.md
```

---

## Dashboard Features

### KPI Monitoring

- Total Devices
- Total Readings
- Total Alerts
- Latest Data Received Time

### Charts

- Temperature Trend
- Humidity Trend
- Database Growth

### Monitoring Pages

- Devices
- Latest Readings
- Alerts
- Database Statistics

### Auto Refresh

Dashboard refreshes automatically every 5 seconds.

---

## Logging Example

```text
[INF] Client Connected

[INF] Received JSON:
{
  "DeviceId":"DEV001",
  "Temperature":31.91,
  "Humidity":83.59
}

[INF] Reading Saved
Id=120
Device=DEV001
```

---

## How To Run

### Start SQL Server

Make sure SQL Server service is running.

---

### Start Worker Service

```bash
cd TcpDataCollector.Worker

dotnet run
```

Expected:

```text
TCP Server started on port 5000
```

---

### Start Device Simulator

```bash
cd DeviceSimulator

dotnet run
```

Expected:

```text
Connected to server

Sent:
DEV001
```

---

### Start Dashboard

```bash
cd Dashboard

streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Sample Workflow

```text
Device Simulator
      |
      v
Send Sensor Data
      |
      v
Worker Service
      |
      v
Validate Message
      |
      +--> SQL Server
      |
      +--> Serilog
      |
      v
Dashboard Visualization
```

---

## Skills Demonstrated

This project demonstrates:

- C#
- .NET Worker Services
- TCP/IP Communication
- Socket Programming
- SQL Server
- Entity Framework Core
- Asynchronous Programming
- Dependency Injection
- Real-Time Monitoring
- Logging and Diagnostics
- Streamlit Dashboard Development
- Database Design
- System Integration

---

## Future Improvements

- Azure SQL Database
- Azure App Service Deployment

---

## Author

**Bishal Shrestha**

Developed as part of learning and demonstrating practical experience in:

- System Programming
- TCP/IP Communication
- Device Data Collection Systems
- .NET Development
- SQL Server
- Monitoring Platforms
