def check(cim):
    rovidites_sz = 0
    helyes = True

    if len(cim) <= 15:
        ip_elemek = cim.split(".")
        for elem in ip_elemek:
            if not 0 < int(elem) < 256 or len(ip_elemek) != 4:
                helyes = False
    else:
        ip_elemek = cim.split(":")
        for elem in ip_elemek:
            if elem == "":
                rovidites_sz += 1
            elif not -1 < int(elem, 16) < 65536 and (len(ip_elemek) != 8 or rovidites_sz == 1):
                helyes = False
                print(int(elem, 16))
            print(len(ip_elemek))

    print(ip_elemek)
    
    if rovidites_sz <= 1:
        return helyes

cim = input("kérem az ip címet --> ")

print(check(cim))
