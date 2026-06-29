import datetime
import os
import time

print("=== Advanced Python Native Alarm Clock ===")

# Feature 1: Loop to validate time input (Prevents crashes from invalid values)
while True:
    alarm_hour = int(input("Enter hour (1-12): "))
    alarm_minute = int(input("Enter minute (0-59): "))
    am_pm = input("AM or PM? ").strip().upper()
    
    if (1 <= alarm_hour <= 12) and (0 <= alarm_minute <= 59) and (am_pm in ["AM", "PM"]):
        break
    print("❌ Invalid time details entered! Please try again.\n")

# Convert 12-hour format to 24-hour format for system tracking
if am_pm == "PM" and alarm_hour != 12:
    alarm_hour += 12
elif am_pm == "AM" and alarm_hour == 12:
    alarm_hour = 0

print(f"\n🔔 Alarm is been successfully set for {alarm_hour:02d}:{alarm_minute:02d} {am_pm}")

# The Monitoring Loop
while True:
    now = datetime.datetime.now()
    
    # Check if target time is reached
    if now.hour == alarm_hour and now.minute == alarm_minute:
        print("\n💥 WAKE UP! ALARM IS RINGING! 💥")
        
        # Ring 10 times natively using the system bell character
        for _ in range(10):
            print("\a", end="", flush=True)  # Native beep without external files
            time.sleep(0.5)
        break
        
    # Feature 2: Dynamic Live Display showing remaining time inside the console
    target_today = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)
    if target_today < now:
        target_today += datetime.timedelta(days=1)
        
    time_remaining = target_today - now
    hours_left, remainder = divmod(time_remaining.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)
    
    # Print dynamic updating clock status bar
    print(f"🕒 Status: Waiting... [Time Remaining: {hours_left:02d}h {minutes_left:02d}m {seconds_left:02d}s]", end="\r")
    
    time.sleep(1)