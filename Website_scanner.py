import os
import subprocess



print("[1] - Subdomain ")
print("[2] - URL directories ")
print("[3] - 3 steps depth spider ")
print("")

selection = int(input("[+] Pass a Valid number query: "))


if selection == 1:
    subprocess.call("pwd", "/", "python crawler.py", shell=True)

elif selection == 2:
    subprocess.call("python crawler2.py", shell=True)

elif selection == 3:
    subprocess.call("python spider.py", shell=True)

elif selection == 4:
    subprocess.call("python spider.py", shell=True)
else:
    print("Invalid Number ")
