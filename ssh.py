import netmiko
from netmiko import ConnectHandler


ssh_connection = ConnectHandler(
   device_type ='cisco_xr',
   ip='172.16.14.201',
   username='sgnog',
   password='sgnog'
    )

result = ssh_connection.find_prompt() + "\n"

result += ssh_connection.send_command("show version", delay_factor=2)

print(result)

ssh_connection.disconnect()

