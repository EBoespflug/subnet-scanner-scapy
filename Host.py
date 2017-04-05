class Host:
    def __init__(self, ip, mac, name):
        self.ip = str(ip)
        self.mac = str(mac)
        self.name = str(name)

    def __str__(self):
        return "(" + self.ip + " " + self.mac + " " + self.name + ")"
