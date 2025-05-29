import os

# for dirpath, dirnames, filenames in os.walk('.'):
#     print(f"Directory: {dirpath}")
#     for dirname in dirnames:
#         print(f"  Subdirectory: {dirname}")
#     for filename in filenames:
#         print(f"  File: {filename}")
for i in os.walk("."):
    print(i)