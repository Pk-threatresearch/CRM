import json
from collections import defaultdict

def detect_bruteforce(logs):
    failed_attempts = defaultdict(int)
    alerts = []

    for log in logs:
        if log["action"] == "login_failed":
            failed_attempts[log["user"]] += 1

        if log["action"] == "login_success":
            if failed_attempts[log["user"]] >= 2:
                alerts.append({
                    "type": "Brute Force Detected",
                    "user": log["user"],
                    "ip": log["ip"]
                })

    return alerts


def detect_privilege_escalation(logs):
    alerts = []
    for log in logs:
        if log["action"] == "role_change" and log.get("role") == "admin":
            alerts.append({
                "type": "Privilege Escalation",
                "user": log["user"],
                "ip": log["ip"]
            })
    return alerts


def main():
    with open("log.json", "r") as f:
        logs = json.load(f)

    alerts = []
    alerts.extend(detect_bruteforce(logs))
    alerts.extend(detect_privilege_escalation(logs))

    print("\n[ALERT] Alerts Generated:")
    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    main()
