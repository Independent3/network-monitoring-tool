import subprocess
import re
import platform
import csv
import os

def ping(host , ping_count):
    success_count = 0
    failure_count = 0
    timeout_count = 0
    latencies = []
    message = ""

    if platform.system() == "Windows":
        plat = "-n"
    elif platform.system() == "Linux":
        plat = "-c"
    else:
        plat = "-c"  # defensive coding

    for i in range(ping_count):
        try:
            result = subprocess.run(["ping", plat, "1", host], capture_output=True, text=True) #Capturing CompletedProcess in result
            if "could not find host" in result.stdout.lower():
                message = f"\033[91mCheck for a typo, couldn't find the '{host}' on the internet\033[0m"
                failure_count += 1
                break #stop pinging
            if "timed out" in result.stdout.lower():
                timeout_count += 1
                continue #skip
            if result.returncode != 0:
                message = '\033[91mPing Failed\033[0m'
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
            message = f"\033[91mError pinging {host}: {e}\033[0m"
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
    all_results = []
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
                        print(f'\033[91mWrong input. Host name should start with A-Z or 0-9 for, {host}\033[0m')
                        failure += 1
            if hosts:
                for host in hosts:
                    result = ping(host,ping_count)
                    result['total_attempted_pings'] = result['success'] + result['failure'] + result['timeout']
                    if result['avg_latency'] != None:
                        print(f"\033[92m{host}: {result['avg_latency']} ms\033[0m")
                    if result['timeout'] > 0 and result['success'] == 0:
                        print(f"\033[93m{host}: Host is reachable but no responses received, Timeouts: {result['timeout']}\033[0m")
                    if result['message']:
                        print(result['message'])
                    success += result['success']
                    failure += result['failure']
                    timeouts += result['timeout']
                    if result['timeout'] > 0 and result['success'] == 0 and not result['message']:
                        result['message'] = f'Host is reachable but no responses received'
                    all_results.append(result)
            else:
                print("\033[91mNo hosts found\033[0m")

            total_attempted_pings = success + failure + timeouts
            print(f'Total number of attempted pings: {total_attempted_pings}\n\033[92mSuccessful pings: {success}\033[0m \n\033[91mFailed attempts: {failure}\n\033[0m\033[93mTimeouts: {timeouts}\033[0m')
        else:
            print("\033[91mNumber should be a positive\033[0m")
    except ValueError:
        print("\033[91mYou must enter a valid number\033[0m")

    file_name = 'Network_Monitoring_logs.csv'
    file_exists = os.path.isfile(file_name)
    with open('Network_Monitoring_logs.csv' , 'a', newline='') as csvfile:
            fieldnames = ['host', 'total_attempted_pings','success', 'failure', 'timeout' , 'avg_latency', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(all_results)

if __name__ == "__main__": #making importing safe/with no troubles
    main()

