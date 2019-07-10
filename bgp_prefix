import ciscoconfparse
import ipaddress

def get_details(SID):
    #TODO: get
    with open('C:\\Users\\ipnoc\\PycharmProjects\\PCTN_Ansible\\CPE3.txt') as current_config:
        conf = ciscoconfparse.CiscoConfParse(current_config,comment='!')
        iface = conf.find_objects_w_child(r'interface', 'description {}'.format(SID))[0]

def find_nxthop(int_ip,mask):
    next_hop = []
    ip_list = list(ipaddress.ip_network('{}/{}'.format(int_ip,mask), strict=False).hosts())
    for k in ip_list:
        next_hop.append(str(k))
    if int_ip in next_hop:
        next_hop.remove(int_ip)
        return nxt_hop

def login_device():
    #TODO:

def create_config():
    #TODO:

def push_config():
    #TODO:

def verify_config():
    #TODO:

def main():

SID = input('Enter SID: ')
prefix_add = input('Enter Prefix: ')

if __name__ == '__main__':
    main()
