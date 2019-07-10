from push_change import push_change
from get_details import get_details


def update_prefix(prefixset_name, prefix, operation):
    result = push_change(
        prefixset_name,
        prefix,
        operation,
    )

    if result is True:
        print("GOOD")
    else:
        print("BAD")



def main():
    sid = "Service01"
    prefix = "10.0.0.0/24"
    operation = "add"

    info = get_details(sid)
    prefixset_name, current_prefixes = info[-2:]
    print("{} / {} / {}".format(
        sid,
        prefixset_name,
        current_prefixes,
    ))

    if prefixset_name:
        update_prefix(prefixset_name, prefix, operation)

if __name__ == "__main__":
    main()
