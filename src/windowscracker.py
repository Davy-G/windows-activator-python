import os
import windowscrackerfuncs
import time

osver = windowscrackerfuncs.get_windows_name()
iscrackable = windowscrackerfuncs.can_be_activated(osver)

print("you are running:", osver + "\n")

if iscrackable:
    keys = windowscrackerfuncs.get_key_list_for_windows(osver)
    print("ur version is supported, this program will now start hacking ... please wait...")
    for key in keys:

        print(f"trying to install key {key}" + "\n")
        returnval = os.system(f"slmgr /ipk {key}")
        if returnval == 0:
            print(f"installed product key {key} sucessfully " + "\n")
            Failed = False
            break
        if returnval == -1073418203:
            print("run this program as admin please! exiting in 10 seconds." + "\n")
            Failed = True
            time.sleep(10)
            exit()
        if returnval == -1073422314:
            print(f"product key {key} failed trying other one" + "\n")
            Failed = True

    if not Failed:
        for key in windowscrackerfuncs.kmslist:

            status1 = os.system(f"slmgr /skms {key}")
            if status1 == 0:
                print(f"kms server {key} was set successfully" + "\n")
            else:
                print(f"failed to set {key} server trying other one.." + "\n")
                continue
            status2 = os.system("slmgr /ato")
            if status2 == 0:
                print("\n" + "windows activated! enjoy!")
                time.sleep(3)
                exit()
            elif status2 == -1073418124:
                print(f"kms server {key} couldnt be contacted trying other kms server")


    else:
        print("something went wrong sorry, im exiting in 10 seconds")
        time.sleep(10)
        exit()

else:
    print("your operating system is not supported, sorry.")
