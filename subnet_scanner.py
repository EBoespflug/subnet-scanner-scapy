from scapy.all import *
from Host import *

def resolve_host_name(ip):
    results = ["unknown"]
    try:
        results = socket.gethostbyaddr(ip)
    except socket.herror: pass

    hostname = "unknown"
    if results != "":
        hostname = results[0] # keep only the host name.
    return hostname

def arping(ip_range, timout):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=timout)

    hosts = []
    for req, res in ans:
        ip = res.getlayer(ARP).psrc
        mac = res.getlayer(Ether).src
        name = resolve_host_name(ip)
        hosts.append(Host(ip, mac, name))

    return hosts
