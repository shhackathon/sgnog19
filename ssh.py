import netmiko
from netmiko import ConnectHandler


def login_router():
   ssh_connection = ConnectHandler(
      device_type ='cisco_xr',
      ip='172.16.14.201',
      username='sgnog',
      password='sgnog'
      )

  # result = ssh_connection.find_prompt() + "\n"

  # result += ssh_connection.send_command("show ip int brief", delay_factor=2)

   #result = net_connect.send_config_set(['interface g0/0/0/3', 'no shut'])

   print(ssh_connection)

  # ssh_connection.disconnect()
   return ssh_connection

def main():
        login_router()
if __name__ == '__main__':
        main()
