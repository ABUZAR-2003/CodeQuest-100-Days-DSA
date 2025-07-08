import re

print("Alert List:")

lines = []
while True:
    line = input()
    if not line.strip():
        break
    lines.append(line)

# Join all lines into a single string for regex parsing
alert_text = "\n".join(lines)

# Pattern to extract alerts like: "description" with priority X
pattern = r'"(.*?)"\s+with\s+priority\s+(\d+)'
matches = re.findall(pattern, alert_text)

# Build (priority, description) tuples
alerts = [(int(priority), desc) for desc, priority in matches]

# Sort alerts by priority
sorted_alerts = sorted(alerts)

# Output
print("\nProcessing Alerts:")
for i, (priority, desc) in enumerate(sorted_alerts, 1):
    print(f"{i}. {desc} (Priority: {priority})")
    

