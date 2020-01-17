from typing import List
from datetime import datetime as dt
import time

hosts_temp = r"D:\Python learning projects\Website Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# IP where a user will be directed after browsing a blocked website.
redirect = "127.0.0.1"

# list of websites to block
website_list: List[str] = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

# setting the hours during which we want the script to run
start_time = dt(dt.now().year, dt.now().month, dt.now().day, 9)
end_time = dt(dt.now().year, dt.now().month, dt.now().day, 17)

while True:
    if start_time < dt.now() < end_time:
        print("working hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()               # file.read() does not create a list
            for website in website_list:
                if website in content:
                    pass

                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("fun hours")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()        # to create a list with each line of host file in it
            file.seek(0)                      # to go back to first line after reading lines
            for line in content:
                if not any(website in line for website in website_list):
                                                     # comparing website list with content list or finding websites in content
                    file.write(line)                 # writing only those lines which don't have website to get original host file
            file.truncate()

    time.sleep(5)