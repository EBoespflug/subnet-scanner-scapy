#!/urs/bin/python
from scapy.all import *
import subnet_scanner
from Host import Host
import time, datetime, argparse

banner = "Subnet scanner v1.0"

def set_configs():
    """Returns a dictionnary corresponding to the configuration of the program depending on the specified arguments.
    An argument parser is created to handle the different option and parameters."""
    arg_parser = argparse.ArgumentParser(description=banner)

    arg_parser.add_argument("ip_ranges", nargs="+", help="The list of range of ip address to scan.")
    arg_parser.add_argument("-t", "--timeout", type=int, default=2, help="Timeout for each port scan. Default = 2.")
    arg_parser.add_argument("-v", "--verbose", action='store_true', help="Set the verbosity level to 'verbose'. In verbose mode, all scapy output are activated.")
    arg_parser.add_argument("-q", "--quiet", action='store_true', help="Set the verbosity level to 'quiet'. In quiet mode, only the result are displayed.")
    arg_parser.add_argument("-T", "--table-results", action='store_true', help="The result are printed as a table.")
    arg_parser.add_argument("-nS", "--no-sort", action='store_true', help="The host are not sorted by ip address.")
    args = arg_parser.parse_args()

    if args.quiet and args.verbose:
        print "warning : both --verbose and --quiet specified. --quiet will be ignored."

    timeout = args.timeout

    if len(args.ip_ranges) == 0:
        print "error : no subnet specified."
        return None

    verbosity = 1
    if args.verbose:
        verbosity = 2
    if args.quiet and (not args.verbose):
        verbosity = 0
    return {
        'ip_ranges'     : args.ip_ranges,
        'verbosity'     : verbosity,
        'timeout'       : timeout,
        'table-results' : args.table_results,
        'no-sort'       : args.no_sort
    }

def main():
    """Main function of the subnet scanner. Parse the argument, launches the scans and print the results."""
    config = set_configs()

    if config is None :
        return

    if config['verbosity'] < 2:
        conf.verb = 0
    start_time = time.time()
    if config['verbosity'] > 0:
        print "Starting subnet scan at " + datetime.datetime.fromtimestamp(int(start_time)).strftime('%Y-%m-%d %H:%M:%S')

    hosts = []
    for ip_range in config['ip_ranges']:
        host_list = subnet_scanner.arping(ip_range, config['timeout'])
        hosts.extend(host_list) # |= set(host_list)

    hosts = remove_duplicates(hosts)
    if not config['no-sort']:
        hosts = sorted(hosts, key=lambda h: h.ip)

    elapsed = time.time() - start_time
    print "Subnet scan done on [" + ", ".join(config['ip_ranges']) + "] in %.2f seconds." % elapsed

    if config['table-results']:
        prettyprint_hosts(hosts)
    else:
        print_hosts(hosts, config)

def remove_duplicates(hosts):
    """Remove the duplicate of an hosts list. The hosts correspond to a list of Host."""
    dic = {}
    for host in hosts:
        if not host.ip in dic:
            dic[host.ip] = host

    new_hosts = []
    for host in dic.values():
        new_hosts.append(host)

    return new_hosts

def print_hosts(hosts, config):
    """Print the detected alive hosts."""
    print "Hosts : "
    max_ipstr_len = 15
    max_macstr_len = 17

    for host in hosts:
        missing_ip_size = max_ipstr_len - len(host.ip)
        missing_mac_size = max_macstr_len - len(host.mac)

        line = " - " + host.ip + " " * missing_ip_size + " "
        line += host.mac + " " * missing_mac_size + "    "
        line += "[" + host.name + "]"

        print line

def prettyprint_hosts(hosts):
    """Print a list of Hosts using a table."""
    max_ipstr_len = 15
    max_macstr_len = 17
    max_namestr_len = 25
    print "/----------------------------------------------------------------\\"
    print "|-----------------------[ Subnet scan result]--------------------|"
    print "|----------------------------------------------------------------|"
    print "|   ip address    |    mac address    |         host name        |"
    print "|----------------------------------------------------------------|"
    for host in hosts:
        missing_ip_size = max_ipstr_len - len(host.ip)
        missing_mac_size = max_macstr_len - len(host.mac)

        line = "| " + host.ip + " " * missing_ip_size + " | "
        line += host.mac + " " * missing_mac_size + " | "
        line += host.name

        if len(host.name) <= max_namestr_len :
            missing_name_size = max_namestr_len - len(host.name)
            line += " " * missing_name_size + "|"

        print line

    print "\\----------------------------------------------------------------/"

if __name__ == "__main__":
    main()
