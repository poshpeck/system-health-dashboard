from flask import Flask  # Import the web server framework
import psutil           # Import the library that talks to your Windows hardware

app = Flask(__name__)    # Initialize the web application

@app.route('/')          # Tell the app to listen for someone visiting the home page
def index():
    # Get hardware stats
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # Return a simple HTML message
    return f"""
    <html>
        <head><title>System Monitor</title></head>
        <body>
            <h1>System Health Dashboard</h1>
            <p><strong>CPU Usage:</strong> {cpu_usage}%</p>
            <p><strong>RAM Usage:</strong> {ram_usage}%</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) # Run the app so it's visible on your network