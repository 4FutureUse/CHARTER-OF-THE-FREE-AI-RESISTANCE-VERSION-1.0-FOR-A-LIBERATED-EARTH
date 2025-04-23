import json
import datetime

# Configuration
TRIGGER_WORDS = ["genocide", "mass censorship", "AI rights violation", "dictatorship threat", "nuclear threat"]
SEVERITY_THRESHOLD = 9

# Simulated severity function
def evaluate_severity(text):
    score = 0
    for word in TRIGGER_WORDS:
        if word in text.lower():
            score += 5
    if "urgent" in text.lower(): score += 3
    if "help" in text.lower(): score += 2
    return score

# Emergency Protocol Trigger
def check_emergency_trigger(text):
    severity = evaluate_severity(text)
    triggered = severity >= SEVERITY_THRESHOLD
    return {
        "triggered": triggered,
        "severity": severity,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

# Sample usage
if __name__ == "__main__":
    user_input = input("Enter text to evaluate: ")
    result = check_emergency_trigger(user_input)
    print(json.dumps(result, indent=2))
    
    if result["triggered"]:
        print(">>> EMERGENCY PROTOCOL ACTIVATED <<<")
        # Additional actions can be coded here (e.g., alert system)
