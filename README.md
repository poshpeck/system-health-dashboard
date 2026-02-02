# 🚀 System Health Dashboard
A lightweight, containerized DevOps project that monitors real-time CPU and RAM usage on your host machine.

---

## 📖 Overview
This project serves as a foundational DevOps exercise. It demonstrates how to build a Python-based monitoring tool, package it into a **Docker** container, and prepare it for a **CI/CD pipeline**.



## 🛠️ Tools & Technologies
* **Language:** Python 3.9
* **Web Framework:** Flask (to serve the dashboard)
* **Monitoring:** Psutil (to access hardware metrics)
* **Containerization:** Docker (to ensure it runs anywhere)
* **Version Control:** Git & GitHub

---

## 🚀 How to Run (Local Machine)

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* Git installed.

### 1. Clone the repository
```powershell
git clone [https://github.com/poshpeck/system-health-dashboard.git](https://github.com/poshpeck/system-health-dashboard.git)
cd "System Health Dashboard"
```

### 2. Build the Docker Image
The . at the end tells Docker to look for the Dockerfile in the current folder.

```PowerShell

docker build -t system-monitor .
```

### 3. Run the Container
This maps port 5000 of the container to port 5000 on your Windows machine.

```PowerShell

docker run -p 5000:5000 system-monitor
```
### 4. View the Dashboard
Open your browser and navigate to:

```Plaintext

http://localhost:5000
```

### 📄 Code Highlights
The Dockerfile  
The Dockerfile is the blueprint for our environment. It uses a "slim" Python image to keep the footprint small.

```Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

### The Logic (app.py)
We use psutil to fetch system data. This is a core concept in Observability, a major pillar of DevOps.

```Python

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
```
