from plyer import notification
import json

# In the other file, we will make a seperate json file that just has all of the notification times (and possibly data) and then we will push the notifications here.

notification.notify(
    title="HEADING HERE",
    message=" DESCRIPTION HERE",
    # displaying time
    timeout=2,
)
