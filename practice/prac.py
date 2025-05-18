import time

# Get current time in seconds since epoch
seconds = time.time()
print(f"Seconds since epoch: {seconds}")

# Convert seconds to local time string
local_time_string = time.ctime(seconds)
print(f"Local time: {local_time_string}")

# Pause execution for 2 seconds
time.sleep(2)
print("Slept for 2 seconds")

# Get local time tuple
local_time_tuple = time.localtime()
print(f"Local time tuple: {local_time_tuple}")

# Format time tuple as a string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time_tuple)
print(f"Formatted time: {formatted_time}")

# Parse a time string
time_tuple = time.strptime("2025-05-04 15:30:00", "%Y-%m-%d %H:%M:%S")
print(f"Parsed time tuple: {time_tuple}")