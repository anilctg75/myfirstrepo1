
import time
from datetime import datetime
import winsound

def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")

    print(f"\nAlarm set for {alarm_time}")
    print("Waiting for alarm...")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("\n⏰ WAKE UP! ALARM RINGING!")

            for i in range(10):
                winsound.Beep(1000, 1000)
                time.sleep(0.5)

            break

        time.sleep(1)

set_alarm()
