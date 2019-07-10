import sys
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
        update_prefix(prefixset_name, prefix, operation)

if __name__ == "__main__":
    main()
