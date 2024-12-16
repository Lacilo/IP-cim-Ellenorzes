def ipType(ip):
    if len(ip.split(".")) == 4:
        return "IPv4"
    elif 1 < len(ip.split(":")) <= 8:
        return "IPv6"
    else:
        return "helytelen"
