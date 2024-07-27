supportedsystemlist = ["Microsoft Windows 10 Pro", "Microsoft Windows 10 Home", "Microsoft Windows 8.1"]
keydict = {"Microsoft Windows 8.1": "M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK",
           "Microsoft Windows 10 Home": "KTNPV-KTRK4-3RRR8-39X6W-W44T3 TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 YTMG3-N6DKC-DKB77-7M9GH-8HVX7 YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY VK7JG-NPHTM-C97JM-9MPGT-3V66T",
           "Microsoft Windows 10 Pro": "W269N-WFGWX-YVC9B-4J6C9-T83GX MH37W-N47XK-V7XM9-C7227-GCQG9 FJT8C-2WNKT-DKPQG-JYHXD-YBFFC X4XQN-VMKJH-7TCVD-TB3QT-KTPKM 3MXN9-Y96QV-RPYHW-RKQQJ-XW3GY"}
kmslist = ["hq1.chinancce.com", "54.223.212.31", "kms.cnlic.com", "kms.chinancce.com", "kms.ddns.net",
           "franklv.ddns.net", "k.zpale.com", "m.zpale.com", "mvg.zpale.com", "kms.shuax.com kensol263.imwork.net:1688",
           "xykz.f3322.org", "kms789.com", "dimanyakms.sytes.net:1688", "kms.03k.org:1688"]


# get the current version of windows
def get_windows_name():
    import subprocess, re
    o = subprocess.Popen('systeminfo', stdout=subprocess.PIPE).communicate()[0]
    try:
        o = str(o, "latin-1")
    except:
        pass
    osver = re.search("OS Name:\s*(.*)", o).group(1).strip()
    return osver


def can_be_activated(current):
    if current in supportedsystemlist:
        return True


def get_key_list_for_windows(key):
    for keys in keydict:
        try:
            values = keydict[key].split(" ")
        except KeyError:
            pass
        return values
