import re, sys

def main(log_name):
    re_pattern = re.compile(r'^.{3},\s(.{11}).*(..:..:..:..:..:..)')
    result = {}
    total = 0

    log = open(log_name)
    for line in log:
        match = re_pattern.match(line)
        if match:
            date, mac_address = match.group(1), match.group(2)
            
            if date in result:
                result[date].add(mac_address)
            else:
                result[date] = set([mac_address])

    # This uses alphabetical sorting so will only work within a month.
    # It also totals all results without regard to month.
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
