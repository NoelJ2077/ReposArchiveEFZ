""" Helper methods for the application. """
import os
import datetime

def get_last_updated():
    """ Get the last updated time of any .py file in the project. app.py excluded. """
    time = 0
    try:
        for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    file_time = os.path.getmtime(file_path)
                    if file_time > time:
                        time = file_time

        if time == 0:
            raise FileNotFoundError("No .py files found")

        # convert literal time to datetime in : 14:30:59, 29 November 2024
        timeobj = datetime.datetime.fromtimestamp(time).strftime("%H:%M:%S, %d %B %Y")
        return timeobj
    except Exception as e:
        # log to file!
        return f"Error getting timeobj!" 