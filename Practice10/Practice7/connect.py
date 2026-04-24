# Example 1: Simulate connecting to a service
def connect_to_service(name):
    print(f"Connecting to {name}...")
    return True

service_status = connect_to_service("Phone API")
print("Connection successful:", service_status)

# Example 2: Disconnect function
def disconnect_service(name):
    print(f"Disconnecting from {name}...")
    return False

service_status = disconnect_service("Phone API")
print("Disconnected:", not service_status)

# Example 3: Check connection status
def status(service_name):
    connected = True
    if connected:
        print(f"{service_name} is connected")
    else:
        print(f"{service_name} is not connected")

status("Phone API")