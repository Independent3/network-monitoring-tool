import subprocess
import re

def ping(host):
    try:
        result = subprocess.run(["ping"  , "-n" ,"1",host], capture_output=True , text=True)
        if "could not find host" in result.stdout.lower():
            return f"Check for a typo, couldn't find the '{host}' on the internet" , True
        if "timed out" in result.stdout.lower():
            return f" It is there but can't get a response from {host}" , False
        if result.returncode !=0:
            return "None" , True
        match = re.search(r"time=(\d+)ms", result.stdout)
        if match:
            latency_value = match.group(1)
            return f"{latency_value} ms" , False
        else:
            return None , False
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return None , True

print("Give the name of the hosts you want to ping separated with space or comma (Duplicate names will be ignored)")

hosts = set()
failure = 0
success = 0

for host in (input().replace("," , "").split()):  #first i use replace to replace any comma with space and then split with no arguments handles messy spacing
    if host:  #defensive programming
        if host[0].isalpha() or host[0].isdigit():
            if host not in hosts:  #not really needed since i use a set() for this
                hosts.add(host)
        else:
            print(f'Wrong input. Host name should start with A-Z or 0-9 for, {host}')
            failure += 1
if hosts:
    for host in hosts:
        latency , failed = ping(host)
        print(f"{host}: {latency}")
        if failed:
            failure += 1
        else:
            success += 1
else:
    print("No hosts found")

total_attempted_pings = success + failure

print(f'Total number of attempted pings: {total_attempted_pings},\nSuccessful pings: {success} \nFailed attempts: {failure}')