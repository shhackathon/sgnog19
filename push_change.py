from ssh import login_router
from get_details import get_details

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
    else:
        pass
    
    
    
def validate(prefixset_name,old_prefixset):
    session = login_router()
        
    cmd = "show rpl prefix-set" + prefixset_name
    output =  session.send_command(cmd)
    print(output)
    
   
    
def main():
    prefixset_name = "Service01_prefix"
    new_prefix = "192.0.0.0/24"
    operation = "remove"
    push_change(prefixset_name, new_prefix, operation)
    
    
if __name__ == '__main__':
    main()



