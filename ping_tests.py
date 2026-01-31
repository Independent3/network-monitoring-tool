import subprocess
result = subprocess.run(["ping"  , "-n" ,"1","google.com"], capture_output=True , text=True)
print(result.stdout)