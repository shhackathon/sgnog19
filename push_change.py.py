from ssh import login_router
from get_details import get_details

def push_change(prefixset_name,new_prefix,operation):
    session = login_router()
    
    cmd = "edit prefix-set " + prefixset_name + " inline " + operation + ' "' + new_prefix + '"'
    print(cmd, flush=True)
    output =  session.send_command(cmd)
    print(output, flush=True)
    if "yes" in output:
        output =  session.send_command("yes")
        print(output, flush=True)
    
    
def validate(prefixset_name,old_prefixset):
    session = login_router()
    
    cmd = "show rpl prefix-set" + prefixset_name
    output =  session.send_command(cmd)
    
   
    
def main():
    prefixset_name = "Service01_prefix"
    new_prefix = "192.0.0.0/24"
    operation = "add"
    push_change(prefixset_name, new_prefix, operation)
    
    
if __name__ == '__main__':
    main()



