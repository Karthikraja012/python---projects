"""import time
from  plyer import notification

if __name__ == "__drink_water_notfi_project__":
 notification._notify(
  title = "Drink some water",
  message =" Time to hydrate! Don't forget to drink a glass of water to stay refreshed and energized. ",
  app_icon = "C:\newprojects_python\waterglass.png",
  timeout = 5
 )
print(dir(notification))"""


import time
from plyer import notification

while True:
    notification.notify(
        title="Drink some water",
        message="Time to hydrate! Don't forget to drink a glass of water to stay refreshed and energized.",
        app_icon=r"C:\newprojects_python\waterglass.png",
        timeout=5
    )
    time.sleep(1800)  # waits 30 minutes before showing again
