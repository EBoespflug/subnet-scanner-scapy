from scapy.all import *
from Host import *

def resolve_host_name(ip):
    """Tries to resolve the host name from the specified address.
    @param ip   the ip of the host.
    @return the name of the host if the operation succeed, 'unknown' otherwise."""
    results = []
    try:
        results = socket.gethostbyaddr(ip)
    except socket.herror: pass # ignore. Nothing to do.

    hostname = "unknown" # default host name.
    if results != "":
        hostname = results[0] # keep only the host name.
    return hostname

def arping(ip_range, timeout = 2):
    """Returns a list of alive Host in the specified ip_range.
    @param ip_range an range of ip (ex : 192.168.1.*, 192.168.1.2-254).
    @param timeout  the timeout of the arp paquets.
    @return the list of alive host found in the specified subnet."""
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range), timeout=timeout)

    hosts = []
    for req, res in ans:
        ip = res.getlayer(ARP).psrc
        mac = res.getlayer(Ether).src
        name = resolve_host_name(ip) # try to get the host name.
        hosts.append(Host(ip, mac, name))

    return hosts
