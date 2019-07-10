import json
import os
import webbrowser
import sys
import textfsm
from netmiko import ConnectHandler


def get_router_infomation(ip, username, password):

   ssh_connection = ConnectHandler(
      device_type ='cisco_xr',
      ip=ip,
      username=username,
      password=password
    )

   result = ssh_connection.find_prompt() + "\n"

   result += ssh_connection.send_command("show version", delay_factor=2)

   ssh_connection.disconnect()
   print (result)

   return result
