import re

# Log Analysis Function
def analyze_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    suspicious_patterns = [
        r"Failed password for",  # Example pattern for failed login attempts
        r"error",                # Example pattern for error messages
        r"unauthorized access",  # Example pattern for unauthorized access
    ]

    suspicious_logs = []

    for log in logs:
        for pattern in suspicious_patterns:
            if re.search(pattern, log, re.IGNORECASE):
                suspicious_logs.append(log)
                break

    return suspicious_logs

# Function to Display Results
def display_results(suspicious_logs):
    if suspicious_logs:
        print("Suspicious activity found:")
        for log in suspicious_logs:
            print(log.strip())
    else:
        print("No suspicious activity found.")

# Test the Functions
if __name__ == "__main__":
    log_file_path = input("Enter the path to the log file: ")
    suspicious_logs = analyze_log(log_file_path)
    display_results(suspicious_logs)
