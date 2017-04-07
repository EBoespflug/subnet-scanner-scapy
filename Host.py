class Host:
    """The Host class represent an host on the network.
    It is composed by it's name and it's addresses (IP & MAC)."""
    def __init__(self, ip, mac, name):
        """Constructs an Host with the specified IP, MAC and name.
        @param ip   the IP address of the host.
        @param mac  the MAC address of the host.
        @param name the host's name."""
        self.ip = str(ip)
        self.mac = str(mac)
        self.name = str(name)

    def __str__(self):
        """@returns the string representation of the host."""
        return "(" + self.ip + " " + self.mac + " " + self.name + ")"
