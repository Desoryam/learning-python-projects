import threading

# Thread-local storage
local_data = threading.local()

def show_local():
    local_data.value = 0  # Each thread has its own "value"
    for _ in range(100):
        local_data.value += 1
    print(f"Thread {threading.get_ident()}: {local_data.value}")  # Always 100 ✅

thread1 = threading.Thread(target=show_local)
thread2 = threading.Thread(target=show_local)

thread1.start()
thread2.start()
thread1.join()
thread2.join()