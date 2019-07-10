import netmiko
from netmiko import ConnectHandler


def login_router():
   ssh_connection = ConnectHandler(
      device_type ='cisco_xr',
      ip='172.16.14.201',
      username='sgnog',
      password='sgnog'
      )

#ssh_connection.find_prompt() + "\n"

   result = ssh_connection.send_command("show ip int brief", delay_factor=2)

   #result = net_connect.send_config_set(['interface g0/0/0/3', 'no shut'])

   print(result)

   #ssh_connection.disconnect()
   return 1
