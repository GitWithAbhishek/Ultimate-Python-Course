# from playsound import playsound

# playsound('Day 47/pikachu.mp3')

import time
from plyer import notification
from playsound import playsound

# Customize the reminder
interval_minutes = 30  # Time between reminders
total_reminders = 8    # Number of times to remind
sound_path = "Day 47/pikachu.mp3"  # Optional: replace with your sound file

for i in range(total_reminders):
    # Show notification
    notification.notify(
        title="💧 Time to Drink Water!",
        message="Stay hydrated! Drink a glass of water now.",
        timeout=10  # seconds
    )

    # Play sound (optional)
    playsound(sound_path)

    print(f"Reminder {i+1}: Drink Water! ✅")
    
    # Wait for the next interval
    time.sleep(interval_minutes * 60)  # convert minutes to seconds

print("✅ All reminders completed for today!")
