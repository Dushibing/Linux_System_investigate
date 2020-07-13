import os
import sys
import platform
import glob
import re

#####################################HOST INFORMATION
OS_flavour = platform.system()
print "\033[1;36;40mOS Flavour \033[0;37;40m : %s\n" % OS_flavour
OS_distribution = platform.linux_distribution()
print "\033[1;36;40mOS Vendor : \033[0;37;40m %s\t\033[1;36;40m Version : \033[0;37;40m %s\t\033[1;36;40mId \033[0;37;40m: %s\n" % OS_distribution
OS_arch = platform.processor()
print "\033[1;36;40mOS Architecture : \033[0;37;40m %s\n" % OS_arch
Network_hostanme = platform.node()
print "\033[1;36;40mServer\'s Network Hostname :\033[0;37;40m %s\n" % Network_hostanme
Linux_kernel = platform.uname()
print "\033[1;36;40mLinux Kernel Version : \033[0;37;40m %s\n" % Linux_kernel[2]

#######DECLARING SYSFS PATH
sysfs = ["/sys/class/scsi_device/", "/sys/class/scsi_host/", "/sys/devices/", "/sys/block/"]
#######Findins Scsi Device
scsi_device = os.listdir(sysfs[0])
pci_scsi = {}
print "\033[1;36;40mAvailable Scsi Device ID : \033[0;37;40m %s\n" % scsi_device

#######FINDING PCI
for i in scsi_device:
    pci_array = os.readlink(sysfs[0] + i).rsplit("/\\")
    pci_scsi[i] = pci_array[3:5]

    print "\033[1;36;40mMapping OS SCSI ID TO PCI ID \033[0;37;40m"
    print "\033[1;32;40m\tSCSI ID\t\tPCI ID \033[0;37;40m \n"

    for n in pci_scsi:
        print "\t%s\t\t%s" % (n, pci_scsi[n])
    print "\n"
    ###Host Adapter and attached Disk information#####
    scsi_host = os.listdir(sysfs[1])
    print "\033[1;36;40mFounded Host adapter :\t \033[0;37;40m %s\n" % scsi_host