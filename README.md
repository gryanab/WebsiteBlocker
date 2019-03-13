# WebsiteBlocker

This program is tested to work on Windows, Mac and Linux. 

This program is intended to block selected websites during wished period of times. Website given in script `app.py` will be written into the system hosts file. 

For `Windows` : host_path = C:\Windows\System32\drivers\etc\hosts

For `Linux` and `Mac` : host_path = /etc/hosts

No GUI for now.

## Note 

If you want the file to run continuously, several solutions are offered: 

* `PythonAnywhere`:  
    * Sign up for a free account at https://www.pythonanywhere.com.
    * Go to your Dashboard, Files, Upload a File, and upload the Python file you want to schedule for execution.
    * Go to Tasks and set the time of the day you want your script to be executed and type in the name of the Python file you  uploaded (e.g., myscript.py). Note that the time you enter should be in UTC.
    * Click the Create button and you’re done.

* `Cron` for mac and Linux users. https://ole.michelsen.dk/blog/schedule-jobs-with-crontab-on-mac-osx.html

* `TaskScheduler` for Windows users (built in app).

Make sure you make a copy of your hosts file for safety measure.

## Run

App must be run as administrator. 