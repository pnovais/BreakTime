import webbrowser
import time

current_time = time.strftime('%H:%M')
while (current_time > '08:00'  and current_time < '18:00'):
    webbrowser.open('https://www.youtube.com/watch?v=mkoIiJhnXLo')
    time.sleep(2 * 3600)
print('Out of time to break a time :)')
