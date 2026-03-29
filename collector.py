import json
import time

def fetch_logs():
    with open("log.json", "r") as f:
        logs = json.load(f)
    return logs

def main():
    print("[*] Fetching logs from CRM API...")
    logs = fetch_logs()

    for log in logs:
        print(f"[LOG] {log}")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
