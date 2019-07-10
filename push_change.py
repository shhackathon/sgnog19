from ssh import login_router
from get_details import get_details
import difflib

def push_change(prefixset_name,new_prefix,operation):
    session = login_router()
    
    cmd = "edit prefix-set " + prefixset_name + " inline " + operation + ' "' + new_prefix + '"'
    print(cmd, flush=True)
    output = session.send_command_timing(cmd, max_loops=10)
    #output =  session.send_command(cmd, expect_string="yes", auto_find_prompt=False)
    print(output, flush=True)
    if "yes" in output:
        output =  session.send_command("yes", expect_string="xrv#")
        print(output, flush=True)
    
    return True
    
    
    
def validate(prefixset_name,old_prefixlist):
    session = login_router()
        
    cmd = "show rpl prefix-set " + prefixset_name
    new_prefixlist =  session.send_command(cmd)
    # print(new_prefixlist)
    # print(old_prefixlist)
    # for line in difflib.unified_diff(new_prefixlist.split("\n"), old_prefixlist.split("\n"), n=0):
    #   print(line)
    old_set = set([l.lstrip(" ").strip(",") for l in old_prefixlist.split("\n") if "/" in l])
    new_set = set([l.lstrip(" ").strip(",") for l in new_prefixlist.split("\n") if "/" in l])
    
    old_to_new = old_set - new_set
    new_to_old = new_set - old_set
    #print(old_set, "\n----------------------")
    #print(new_set, "\n----------------------")
    print("Diff from Old to New", old_to_new)
    print("Diff from New to Old", new_to_old)
    return True
    
    
   
    
def main():
    prefixset_name = "Service01_prefix"
    new_prefix = "192.0.0.0/24"
    operation = "remove"
    push_change(prefixset_name, new_prefix, operation)
    
    
if __name__ == '__main__':
    main()



