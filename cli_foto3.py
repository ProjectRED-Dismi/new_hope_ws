#! /usr/bin/env python

#Informazioni importanti: 
#Versione XLRD 1.0.0 (legge sia xls, sia xlsx)
#Versione Pandas 0.24.2
import os
import sys
import subprocess
import rospy
import roslib
from std_msgs.msg import String
#from rospy_tutorials.msg import Floats
from std_msgs.msg import Int32
from geometry_msgs.msg import Pose
from std_msgs.msg import Bool
from std_srvs.srv import Empty, EmptyRequest



#args = rospy.myargv(argv=sys.argv)

#sender = args[1]
#receiver = args[2]
#password = args[3]
# file_path = args[4]

#print("Sender: %s" %sender)
#print("Receiver: %s" %receiver)
#print("password: **********")
# print("Path to file: %s" %file_path)


def menu ():
    print ('')
    print ('Inserire 0 per chiudere il menu')
    print ('Inserire 1 per SCATTARE UNA FOTOGRAFIA')
    
    #Prendo input 
    num = raw_input('Enter a number:')
    i = 0

    if num =='0':
        return
    
    if num == '1':
        BoolFunction = True
        print(i)

        while BoolFunction:
            rospy.wait_for_service('/image_saver/save')                             # wait for service to be running
            saveimg_service = rospy.ServiceProxy('/image_saver/save', Empty)        # create connection to service
            emp_req = EmptyRequest()                                                # create request
            saveimg_service(emp_req)                                                # send request through connection
            print("Immagine scattata!")
            rospy.sleep(0.5)

            BoolFunction = False
            break

        
        menu()




def main():
    rospy.init_node('cli_foto', anonymous=True) 
    menu()
   


if __name__ == '__main__':
    main()