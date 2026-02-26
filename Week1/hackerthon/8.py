#8.Local "Web-Hook" Trigger
from flask import Flask
import os

app = Flask(__name__)

TRIGGER_PATH = "/run-maintenance"

def run_maintenance():
    log_file = "app.log"
    
    if os.path.exists(log_file):
        with open(log_file, "w") as f:
            pass
        print("Cleared log file!")
    else:
        print("Log file not found!")

    print("Maintenance is done.")

@app.route(TRIGGER_PATH, methods=["GET"])
def local_webhook_trigger():
    run_maintenance()
    return "Maintenance is going to happen.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)