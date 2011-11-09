#TODO Use ordered dictionary or something more complex for ordering keys.
# like grabbing the keys, ordering them, then iterating over them.

#TODO Add comments.

import re, sys

def main(log_name):
    re_pattern = re.compile(r'^.{3},\s(.{11}).*(..:..:..:..:..:..)')
    result = {}

    log = open(log_name)
    for line in log:
        match = re_pattern.match(line)
        if match:
            date, mac_address = match.group(1), match.group(2)
            
            if date in result:
                result[date].add(mac_address)
            else:
                result[date] = {mac_address}

    for date, mac_address_set in result.iteritems():
        print "%s: %d" % (date, len(mac_address_set))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Usage: python parse_dhcp_log.py <logfile>"
