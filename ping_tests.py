import subprocess
import re

def ping(host):
    try:
        result = subprocess.run(["ping"  , "-n" ,"1",host], capture_output=True , text=True)
        if "could not find host" in result.stdout.lower():
            return f"Check for a typo, couldn't find the '{host}' on the internet"
        if "timed out" in result.stdout.lower():
            return f" It is there but can't get a response from {host}"
        if result.returncode !=0:
            return "None"
        match = re.search(r"time=(\d+)ms", result.stdout)
        if match:
            latency_value = match.group(1)
            return f"{latency_value} ms"
        else:
            return None
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return None

print("Give the name of the companies you want to ping separated with space")

companies = []
for host in (input().split()):
    companies.append(host)

if companies:
    for host in companies:
        latency = ping(host)
        print(f"{host}: {latency}")
else:
    print("No companies found")