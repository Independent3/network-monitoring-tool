## :satellite: Network Monitoring Tool

A simple Python-based network monitoring tool that pings multiple hosts, displays colored console output, and logs detailed results to a CSV file for later analysis.

## 💥 Features

✅Ping multiple hosts in one run

✅Configure number of ping attempts per host

✅Cross-platform support (Windows & Linux)

✅ Colored console output for better readability:

  &nbsp;&nbsp;&nbsp;&nbsp; 🟢 Successful pings (average latency)  
  &nbsp;&nbsp;&nbsp;&nbsp; 🟡 Hosts reachable but not responding (timeouts)  
  &nbsp;&nbsp;&nbsp;&nbsp; 🔴 Errors, invalid input, or unreachable hosts

✅CSV logging with per-host statistics (like average latency , timeouts , messages)  

✅CSV file appends results instead of overwriting previous runs

✅Duplicate hosts are automatically ignored


## 📊 CSV Logging

- Results are saved to: **Network_Monitoring_logs.csv**

Each run **appends** new rows while keeping file intact


## 🛠️ Requirements

 -**Python 3.x***

 - **Works on:**

   - **&nbsp;&nbsp;&nbsp;&nbsp; Windows**
  
   - **&nbsp;&nbsp;&nbsp;&nbsp; Linux**
  
No external Libraries required

## 🚀 How to Run 

    python main.py

You will be prompted to:

   - &nbsp;&nbsp;&nbsp;&nbsp;  Enter how many times to ping each host
  
   - &nbsp;&nbsp;&nbsp;&nbsp;  Enter one or more hostnames (space or comma separated)

## 🖥️ Example Console Output
- &nbsp;&nbsp;&nbsp;&nbsp; Green latency for successful responses  
- &nbsp;&nbsp;&nbsp;&nbsp; Yellow warning when a host is reachable but does not reply  
- &nbsp;&nbsp;&nbsp;&nbsp; Red messages for errors, invalid input, or unreachable hosts  

**Example Inputs** 

<img width="1286" height="221" alt="image" src="https://github.com/user-attachments/assets/dbb315c8-edfb-425e-a01f-8605f5b3d95c" />


**Example Outputs**  

<img width="1275" height="217" alt="image" src="https://github.com/user-attachments/assets/873d0312-0bbe-4df5-8903-d9b392cd533b" />

<img width="1279" height="216" alt="image" src="https://github.com/user-attachments/assets/4e12e1bc-495c-4d3b-8aad-5fd98ce30f34" />

<img width="1065" height="315" alt="image" src="https://github.com/user-attachments/assets/c2802ce5-9fdd-4647-96dd-a62cd68ad117" />



## ⚠️ Notes

- Some hosts(e.g microsoft.com) may be reachable but not respond to ICMP pings - this is handled and reported

- Invalid hostnames are detected early and reported to console

- Platform-specific ping flags are detected once per run for efficiency

## 🎓 What I Learned

- **Cross-Platform Logic:** Handled OS-specific command-line arguments for Windows and Linux.

- **Error Handling:** Implemented robust validation to prevent script crashes from invalid hostnames or restricted IPs.

- **Data Management:** Learned to structure real-time network logs into a readable CSV format for long-term tracking.

- **Regex Pattern Matching:** Utilized Regular Expressions to validate hostnames and IP addresses, ensuring user input follows standard networking protocols before processing.

## 🔧 Possible Improvements

- Parallel pings using threading or asyncio

- Export results to JSON

- Summary statistics per run

## 👤 Author

**Nikolaos Vasilakopoulos**  

- 🌍 **Portfolio:** (https://github.com/Independent3 , https://www.linkedin.com/in/nikolaos-vasilakopoulos-85714b3b0/)
  
- 📧 **Email:** nickvasilakopoulos@rocketmail.com
