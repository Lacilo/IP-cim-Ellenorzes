def ipType(ip):
    if len(ip.split(".")) == 4:
        return "IPv4"
    elif len(ip.split(":")) == 8:
        return "IPv6"
    else:
        return "helytelen"
