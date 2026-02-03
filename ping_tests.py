import subprocess
import re


def ping(host , ping_count):
    success_count = 0
    failure_count = 0
    timeout_count = 0
    latencies = []
    message = ""
    for i in range(ping_count):
        try:
            result = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True)
            if "could not find host" in result.stdout.lower():
                message = f"Check for a typo, couldn't find the '{host}' on the internet"
                failure_count += 1
                break #stop pinging
            if "timed out" in result.stdout.lower():
                timeout_count += 1
                continue #skip
            if result.returncode != 0:
                message = 'Ping Failed'
                failure_count += 1
                break
            match = re.search(r"time=(\d+)ms", result.stdout)
            if match:
                latency_value = int(match.group(1))
                latencies.append(latency_value)
                success_count += 1
            else:
                failure_count += 1
        except Exception as e:
            message = f"Error pinging {host}: {e}"
            failure_count += 1
            break
    if latencies:
        average_latency = sum(latencies) / len(latencies)
    else:
        average_latency = None
    return{"host": host,
           "success": success_count,
           "failure": failure_count,
           "timeout": timeout_count,
           "avg_latency": average_latency,
           "message": message}
def main():
    try:
        print("How many times you want to ping each host?")
        ping_count = int(input())
        if ping_count > 0:
            print("Give the name of the hosts you want to ping separated by space or comma (Duplicates will be ignored)")

            hosts = set()
            failure = 0
            success = 0
            timeouts = 0

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
                    result = ping(host,ping_count)
                    if result['avg_latency'] != None:
                        print(f"{host}: {result['avg_latency']} ms")
                    if result['timeout'] > 0 and result['success'] == 0:
                        print(f"{host}: Host is reachable but no responses received, Timeouts: {result['timeout']}")
                    if result['message']:
                        print(result['message'])
                    success += result['success']
                    failure += result['failure']
                    timeouts += result['timeout']
            else:
                print("No hosts found")

            total_attempted_pings = success + failure + timeouts

            print(f'Total number of attempted pings: {total_attempted_pings},\nSuccessful pings: {success} \nFailed attempts: {failure}\nTimeouts: {timeouts}')
        else:
            print("Number should be a positive")
    except ValueError:
        print("You must enter a valid number")
if __name__ == "__main__": #making importing safe/with no troubles
    main()

