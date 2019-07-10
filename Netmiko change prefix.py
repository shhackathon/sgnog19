import netmiko
from netmiko import ConnectHandler

next_hop = input("Enter next_hop: ")
policy_name = input("Enter policy_name: ")
pfx = input("Enter def: ")


def send_config(next_hop,policy_name,session,pfx)

config_add_pfx = ['edit prefix-set policy_name inline add x.x.x.x/x',
                  'show run formal | i nexthop'
                  'show rpl route-policy policy_name']
output_add = net_connect.send_config_set(config_add_pfx)
print(output_add)

config_rmv_pfx = ['edit prefix-set policy_name inline remove x.x.x.x/x',
                  'show run formal | i nexthop'
                  'show rpl route-policy policy_name']
output_rmv = net_connect.send_config_set(config_rmv_pfx)
print(output_rmv)












