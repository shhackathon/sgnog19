import ciscoconfparse
import ipaddress

def get_details(SID):
    #TODO: get
    with open('/home/daniel/sgnog19/data/xrv.cfg') as current_config:
        conf = ciscoconfparse.CiscoConfParse(current_config,comment='!')
        iface = conf.find_objects_w_child(r'interface', 'description {}'.format(SID))[0]
        for d in iface.ioscfg:
            if 'ipv4 address' in d:
                iface_ip = d.split(' ')[-2]
                netmask = d.split(' ')[-1]
                nbr_ip = find_nxthop(iface_ip,netmask)

        bgpcfg = conf.find_objects(r'^router bgp')[0].ioscfg
        bgpcfg = ciscoconfparse.CiscoConfParse(bgpcfg)
        nbr = bgpcfg.find_objects("^ +neighbor {}".format(nbr_ip))[-1]
        #nbr.ioscfg  get route policy
        for i in nbr.ioscfg:
            if 'route_policy' in i:
                rpl = split(" ")[-2]

        rpl_cfg = conf.find_objects(r"^route-policy {}".format(rpl))[-1]
        for l in rpl_cfg.ioscfg:
            if "destination in" in l:
                tmp = l.split(")")[0]
                prefixset_name = tmp.split(" ")[-1]

        prx_set_cfg = config.find_objects("^prefix-set {}".format(prefixset_name))[-1]
        prefixset = [i.lstrip(" ").strip(",") for i in prx_set_cfg.ioscfg[1:]]

    return iface,iface_ip,nbr_ip,rpl,prefixset_name,prefixset

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
