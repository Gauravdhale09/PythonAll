import psutil

def get_running_applications():
    running_apps = []
    for process in psutil.process_iter(['name']):
        try:
            if process.info and process.info['name']:
                running_apps.append(process.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_apps

# Get the list of running applications
apps = get_running_applications()

# Print the list of running applications
print("Running Applications:")
for app in apps:
    print(app)
