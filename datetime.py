import datetime

# Get the current date and time
x = datetime.datetime.now()

# Calculate the months and days since January 1
months_passed = x.month - 1  # January is month 1, so subtract 1
days_passed = x.day

# Print the output
print(f"It has been {months_passed} months and {days_passed} days since your New Year's resolution. How are you doing?")
