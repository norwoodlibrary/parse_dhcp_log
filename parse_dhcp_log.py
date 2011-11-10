import re, sys

def main(log_name):
    re_pattern = re.compile(r'^.{3},\s(.{11}).*(..:..:..:..:..:..)')
    result = {}
    total = 0

    # Parse the logfile into a dictionary consisting of 
    # {string date: set MAC_addresses} pairs.
    log = open(log_name)
    for line in log:
        match = re_pattern.match(line)
        if match:
            date, mac_address = match.group(1), match.group(2)
            
            # If the date is already in the dictionary, add the MAC address to the set. 
            if date in result:
                result[date].add(mac_address)
            # Otherwise, create a new date with a set containing this MAC address.
            else:
                result[date] = set([mac_address])

    # TODO Use dates rather than strings so script works if multiple months are in log.
    dates = result.keys()
    dates.sort()
    for date in dates:
        day_subtotal = len(result[date])
        total += day_subtotal
        print "%s: %s" % (date, day_subtotal)
    print "\nTotal = %d" % total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print "Usage: python parse_dhcp_log.py <logfile>"
