def check(cim):
    rovidites_sz = 0
    helyes = True

    if "." in cim:
        ip_elemek = cim.split(".")
        for elem in ip_elemek:
            try:
                if elem[0] == "0" and len(elem) > 1:
                    helyes = False
                elem = int(elem)

                if not -1 < elem < 256 or len(ip_elemek) != 4:
                    helyes = False
            except:
                helyes = False
            
    elif ":" in cim:
        ip_elemek = cim.split(":")
        for elem in ip_elemek:
            try:
                if len(elem) > 4:
                    helyes = False
                if ip_elemek[0] == "" and ip_elemek[1] == "":
                    ip_elemek[0] = "0"
                    ip_elemek[1] = "0"
                    ip_elemek[2] = "0"
                if elem == "":
                    rovidites_sz += 1
                    elem = "0"
                elem = int(elem, 16)
                ip_elemek = cim.split(":")
                if not -1 < elem < 65536 and (len(ip_elemek) != 8 and rovidites_sz == 1) or len(ip_elemek) > 8:
                    helyes = False
                elif ip_elemek[-1] == "" and ip_elemek[-2] != "":
                    helyes = False
                
            except ValueError:
                helyes = False

    else:
        return False
            
    if rovidites_sz <= 1:
        return helyes
