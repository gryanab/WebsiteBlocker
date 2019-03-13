import time
from datetime import datetime as dt

# On Windows
# host_path = r'C:\Windows\System32\drivers\etc\hosts'

# working with temporary file while script not complete
host_temp = 'hosts.txt'
# host_path = r'etc/hosts'  # On Linux and Mac
redirect = '127.0.0.1'

# list of all sites you wish to block
blocked_websites = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instagram.com', 'www.netflix.com']


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17) \
            or dt(dt.now().year, dt.now().month, dt.now().day, 22) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 8):
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0) # replacing pointer before first character
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()
        print('Non office nor sleeping hours')
    time.sleep(10)