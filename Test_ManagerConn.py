from rina.manager import RinaManager
from rina.coreManager import RinaCoreManager
from time import sleep


#TESTING CONNECTION TO THE RINA_MANAGER
m1 = RinaManager('/var/run/nmconsole.sock', '/home/terminet/DifTemplates')
m1.connect()
systems = m1.list_systems()
print(systems)
sleep (10)

# Testing create and destroy a DIF
#m1.create_dif('slice1e.ddesc')
#sleep (10)
#m1.destroy_dif('slice2')

#sleep (10)
# Testing create and destroy an I
# PCP
ret = m1.create_ipcp("1","slice.desc")
if ret:
    print("Success: "+str(ret))
#sleep (10)
#m1.destroy_ipcp("1", "3")

#TESTING RINA CORE MANAGER

#cm1 = RinaCoreManager()
#cm1.add_system("http://192.168.40.97:5000", "ma_nuc_10", "slave", "10")
#cm1.add_system("http://192.168.40.126:5000", "ma_nuc_9", "master", "9")
#cm1.list_systems()
#cm1.create_dif("10","112")
#cm1.create_dif("9","112")




