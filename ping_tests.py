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
hosts = ["google.com", "cisco.com" , "visa.com" , "microsoft.com" , "hi231..comgr" , "test"]
for host in hosts:
    latency = ping(host)
    print(f"{host}: {latency}")
