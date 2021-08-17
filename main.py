# Install pywhatkit -- pip install pywhatkit

import pywhatkit as pwk

# (phone number, message, time hour, time minute)
pwk.sendwhatmsg("+123 456 789 00", "Reminder for meeting ...", 10, 30)


# Run this script and the message will be sent at the time specified 10:30

