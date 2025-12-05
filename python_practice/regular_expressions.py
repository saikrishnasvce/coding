import re

output = """
msperfect-modular-chassis#show ip int br | ex down
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  up                    up      
Vlan4000               172.18.203.209  YES DHCP   up                    up      
Te1/0/3                unassigned      YES unset  up                    up      
Te1/0/4                unassigned      YES unset  up                    up      
Te1/0/5                5.5.5.2      YES unset  up                    up      
Te1/0/6                180.0.1.2      YES unset  up                    up      
Te1/0/7                unassigned      YES unset  up                    up      
FiftyGigE3/0/16        unassigned      YES unset  up                    up      
FiftyGigE4/0/1         unassigned      YES unset  up                    up      
FiftyGigE4/0/16        4.4.3.5      YES unset  up                    up      
TLS-VIF2               unassigned      NO  unset  up                    up      
"""

d = dict()
# Fixed: proper IPv4 ranges + MULTILINE flag
pattern = re.compile(r'^(\S+)\s+((?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){'
                     r'3})\s+\w+\s+\w+\s+(\w+)', re.MULTILINE)
matches = pattern.finditer(output)

for match in matches:
    interface = match.group(1)
    ip = match.group(2)
    status = match.group(4)
    d[interface] = {'IP-Address': ip, 'Status': status}
    print(f"Interface: {interface}, IP: {ip}, Status: {status}")

print("\nSummary:")
print(d)
