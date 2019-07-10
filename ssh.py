import netmiko
from netmiko import ConnectHandler


def add_changes_router(prefixname, action, ipprefix)
ssh_connection = ConnectHandler(
   device_type ='cisco_xr',
   ip='172.16.14.201',
   username='sgnog',
   password='sgnog'
    )

#ssh_connection.find_prompt() + "\n"

#ssh_connection.send_command("config t", delay_factor=2)

result = net_connect.send_config_set(['interface g0/0/0/3', 'no shut'])


print(result)

ssh_connection.disconnect()

