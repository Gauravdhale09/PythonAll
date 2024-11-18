import threading

print("let us find the current thread")

print("currently running thread: " + threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Current thread is the main thread")
else:
    print("Current thread is not the main thread")
