import os
import windowscrackerfuncs
import time



osver=windowscrackerfuncs.get_windows_name()
key=osver
iscrackable=windowscrackerfuncs.determine_if_system_can_be_hacked(osver)

print("you are running:", osver+"\n")



if iscrackable==True:
    keys=windowscrackerfuncs.get_key_list_for_windows(key)
    print("ur version is supported, this program will now start hacking ... please wait...")
    for stuff in keys:
     
     print(f"trying to install key {stuff}"+"\n")
     returnval=os.system(f"slmgr /ipk {stuff}")
     if returnval==0:
         print(f"installed product key {stuff} sucessfully "+"\n")
         Failed=False
         break
     if returnval==-1073418203:
         print("run this program as admin please! exiting in 10 seconds."+"\n")
         Failed=True
         time.sleep(10)
         exit()
     if returnval==-1073422314:
         print(f"product key {stuff} failed trying other one"+"\n")
         Failed=True

    if Failed==False:
        for stuff in windowscrackerfuncs.kmslist:
           
            status1=os.system(f"slmgr /skms {stuff}")
            if status1 == 0:
                print(f"kms server {stuff} was set successfully"+"\n")
            else:
                print(f"failed to set {stuff} server trying other one.."+"\n")
                continue
            status2=os.system("slmgr /ato") 
            if status2==0:
                print("\n"+"windows activated! enjoy!")
                time.sleep(3)
                exit()
            elif status2==-1073418124:
                print(f"kms server {stuff} couldnt be contacted trying other kms server")
            

    else:
        print("something went wrong sorry, im exiting in 10 seconds")
        time.sleep(10)
        exit()
     
else:
    print("ur windows is not supported or ur running this on other os, sorry.")
   

