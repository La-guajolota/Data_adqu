import nidaqmx
import nidaqmx.system

system = nidaqmx.system.System.local()
print(system.driver_version)

for device in system.devices:
    print("Connected device",device)