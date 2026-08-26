import bluetooth
import time

print("🔵 MD Cyber Bluetooth Scanner 2026")
print("Scanning for nearby Bluetooth devices... 10 seconds\n")

nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True, flush_cache=True)

if len(nearby_devices) == 0:
    print("No devices found.")
else:
    print(f"Found {len(nearby_devices)} devices:")
    for addr, name in nearby_devices:
        print(f"\n[+] Device Name: {name}")
        print(f"    Address: {addr}")
        print(f"    Class: {bluetooth.lookup_class(addr)}")
        
        # Try to get services - basic service scan
        try:
            services = bluetooth.find_service(address=addr)
            if services:
                print("    Open Services:")
                for svc in services:
                    print(f"      - {svc['name']} on port {svc['port']}")
        except:
            print("    Services: Could not scan - device may not be pairable")

print("\n✅ Scan Complete")
print("Note: Only test on devices you own")