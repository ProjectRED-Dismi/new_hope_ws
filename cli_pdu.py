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
from std_msgs.msg import Empty
from std_msgs.msg import UInt8

BoolNavigation = True   

pub = rospy.Publisher('probe_deployment_unit/drop', Empty, queue_size=10)


def callback(data):
    print("Probes deployed: %s" %data.data)
    if (data.data == 5):
        print("NO PROBES LEFT!")

    
    


def deploy():
    rate = rospy.Rate(5) # 10hz 
    mess = Empty()
    pub.publish(mess)
    rate.sleep()
    print("Probe deployed!")

def probes_left():
    rospy.Subscriber("probe_deployment_unit/probes_dropped", UInt8, callback)
    #rospy.spin()

 
def main():
    print ('')
    print ('Inserire 0 per chiudere il menu science')
    print ('Inserire 1 per RILASCIARE PROVETTA')
    print('Inserire 2 per vedere quante provette sono state rilasciate')
    #Prendo input 
    num = raw_input('Enter a number:')

    if num =='0':
        return
    
    if num =='1':
        deploy()
        probes_left()
        rospy.sleep(0.3)
        
        main()
    if num=='2':
        probes_left()
        main()

   


if __name__ == '__main__':
    rospy.init_node('cli_pdu', anonymous=True) 
    main()