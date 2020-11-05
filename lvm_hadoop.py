import os
import getpass
print("\t\t welcome to my menu")
print("\t\t ..................")
passwd=getpass.getpass("Enter ur password: ")
if passwd!="hello":
   print("Invalid Password")
   exit()
while True:
   #os.system("clear")
   print("""
   Press 1 to check the status of attached hard disk
   Press 2 to check all the mounted storage
   Press 3 to create logical volume
   Press 4 to check the size contributed by slave
   Press 5 to extend the size of logical volume
   Press 6 to extend volume group
   """)
   ch=input("Enter your choice:")
   if int(ch)==1:
      os.system("fdisk -l")
   elif int(ch)==2:
      os.system("df -h")
   elif int(ch)==3:
      hn=input("enter hard disk name:")
      print("Creating Physical Volume.....")
      os.system("pvcreate {}".format(hn));
      vgn=input("provide volume group name:")
      print("Creating Volume Group.....")
      os.system("vgcreate {} {}".format(vgn,hn))
      lvn=input("provide logical volume name:")
      lvs=input("provide logical volume size:")
      print("creating logical volume.....")
      os.system("lvcreate --size {} --name {} {}       	           ".format(lvs,lvn,vgn))
      lvp="/dev"+"/"+vgn+"/"+lvn
      print("formatting logical volume.......")
      os.system("mkfs.ext4 {}".format(lvp))
      print("mounting the logical volume with directory of 	   data node......");
      os.system("mount {} /dn".format(lvp))
   elif int(ch)==4:
      os.system("hadoop dfsadmin -report")
   
   elif int(ch)==5:
      es=input("Enter the size you want  to increase:")
      vgn=input("provide volume group name:")
      lvn=input("provide logical volume name:")
      lvp="/dev"+"/"+vgn+"/"+lvn
      print("increasing logical volume........")
      os.system("lvextend --size +{} {}".format(es,lvp))
      os.system("resize2fs {}".format(lvp))
   elif int(ch)==6:
      hn1=input("enter hard disk name:")
      print("Creating Physical Volume.....")
      os.system("pvcreate {}".format(hn1));
      print("increasing volume group.....")
      os.system("vgextend {} {}".format(vgn,hn1))
      es=input("Enter the size you want  to increase:")
      vgn=input("provide volume group name:")
      lvn=input("provide logical volume name:")
      print("increasing logical volume........")
      lvp="/dev"+"/"+vgn+"/"+lvn
      os.system("lvextend --size +{} {}".format(es,lvp))
      os.system("resize2fs {}".format(lvp))
      
     
      
     
 
   
   
