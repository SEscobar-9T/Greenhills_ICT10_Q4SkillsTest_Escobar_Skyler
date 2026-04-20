from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

numby_of_days = np.array([0, 0, 0, 0, 0])
weekdays = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

def attend_track(e):
    document.getElementById('output').innerHTML = ''
    index_grab = int(document.getElementById("absent_day").value)
    absence_value = int(document.getElementById("input").value)

    numby_of_days[index_grab] += absence_value
    print(dict(zip(numby_of_days, weekdays)))

    weekly_attendance = plt.bar(weekdays, numby_of_days)
    plt.show(weekly_attendance)
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel('Number of Absences')
    plt.ylabel('Workday')
    