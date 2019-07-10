import sys
from push_change import push_change, validate
from get_details import get_details


def update_prefix(prefixset_name, prefix, operation):
    result = push_change(
        prefixset_name,
        prefix,
        operation,
    )

    if result is True:
        print("DONE - Prefix {} has been {}ed to {} successfully".format(
            prefix,
            operation,
            prefixset_name,
        ))
        return True
    else:
        print("FAILED - Unable to {} {} to {}".format(
            operation,
            prefix,
            prefixset_name,
        ))
        return False


def main():
    if len(sys.argv) == 4:
        sid = sys.argv[1]
        operation = sys.argv[2]
        prefix = sys.argv[3]

    info = get_details(sid)
    prefixset_name, current_prefixes = info[-2:]
    print("{} / {} / {}".format(
        sid,
        prefixset_name,
        current_prefixes,
    ))

    if prefixset_name:
        if update_prefix(prefixset_name, prefix, operation):
            result = validate(prefixset_name, current_prefixes)
            

if __name__ == "__main__":
    main()
