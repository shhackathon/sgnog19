import ciscoconfparse
import ipaddress

def get_details(SID):
    #TODO: get
    with open('/home/daniel/sgnog19/data/xrv.cfg') as current_config:
        conf = ciscoconfparse.CiscoConfParse(current_config,comment='!')
        iface_conf = conf.find_objects_w_child(r'interface', 'description {}'.format(SID))[0]
        for d in iface_conf.ioscfg:
            if 'interface' in d:
                iface = d.split(' ')[-1]
            if 'ipv4 address' in d:
                iface_ip = d.split(' ')[-2]
                netmask = d.split(' ')[-1]
                nbr_ip = find_nxthop(iface_ip,netmask.split('\n')[0])

        bgpcfg = conf.find_objects(r'^router bgp')[0].ioscfg
        bgpcfg = ciscoconfparse.CiscoConfParse(bgpcfg)
        nbr = bgpcfg.find_objects("^ +neighbor {}".format(nbr_ip))[-1]
#        print(nbr)
        #nbr.ioscfg  get route policy
        for i in nbr.ioscfg:
            if 'route-policy' and 'in' in i:
                rpl = i.split(" ")[-2]
                print(rpl)
        rpl_cfg = conf.find_objects(r"^route-policy {}".format(rpl))[-1]
#        print(rpl_cfg)
        for l in rpl_cfg.ioscfg:
            if "destination in" in l:
                tmp = l.split(")")[0]
                prefixset_name = tmp.split(" ")[-1]

        prx_set_cfg = conf.find_objects("^prefix-set {}".format(prefixset_name))[-1]
#        prefixset = [i.lstrip(" ").strip(",") for i in prx_set_cfg.ioscfg[1:]]
#        prefixset_new = []
#        for j in prefixset:
#            if ',\n' in j:
#                prefixset_new.append(j.split(',\n')[0])
#            elif '\n' in j:
#                prefixset_new.append(j.split('\n')[0])
    diff_libinput = ('').join(prx_set_cfg.ioscfg) + ' end set\n'
    return iface,iface_ip,nbr_ip,rpl,prefixset_name,diff_libinput


def find_nxthop(int_ip,mask):
    next_hop = []
    ip_list = list(ipaddress.ip_network('{}/{}'.format(int_ip,mask), strict=False).hosts())
    for k in ip_list:
        next_hop.append(str(k))
    if int_ip in next_hop:
        next_hop.remove(int_ip)
        return next_hop[0]

def main():

    SID = input('Enter SID: ')
    prefix_add = input('Enter Prefix: ')
    print(get_details(SID))

if __name__ == '__main__':
    main()
