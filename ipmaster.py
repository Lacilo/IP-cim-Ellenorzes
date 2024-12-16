from modules import iptype
from modules import ipvalid

ip = input("Adjon meg egy IP-címet: ")
if iptype.ipType(ip) == "IPv4":
    if ipvalid.check(ip):
        print("Ez egy IPv4-es cím.")
    else:
        print("Ez hasonlít egy IPv4-es címre, de nem helyes formátumú!")
elif iptype.ipType(ip) == "IPv6":
    if ipvalid.check(ip):
        print("Ez egy IPv6-os cím.")
    else:
        print("Ez hasonlít egy IPv6-os címre, de nem helyes formátumú!")
else:
    print("Ez még nem is hasonlít IPv4-es vagy IPv6-os címhez!")
