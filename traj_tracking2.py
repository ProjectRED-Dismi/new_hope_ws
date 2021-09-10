#!/usr/bin/env python 
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseWithCovariance,Point
from nav_msgs.msg import Odometry

def callback(data):
    add_point = Point()
    add_point.x = data.pose.pose.position.x
    add_point.y = data.pose.pose.position.y
    add_point.z = 0
    rospy.loginfo('Publishing Marker Point')
    marker.points.append(add_point)
    # Publish the Marker
    pub_point.publish(marker)


marker = Marker()
marker.header.frame_id = "/map"
marker.type = marker.LINE_STRIP
marker.action = marker.ADD

# marker scale
marker.scale.x = 0.03
marker.scale.y = 0.03
marker.scale.z = 0.03

# marker color
marker.color.a = 1.0
marker.color.r = 1.0
marker.color.g = 0.0
marker.color.b = 0.0

# marker orientaiton
marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 1.0

# marker line points
marker.points = []
rospy.loginfo('Marker created')

rospy.init_node('tracking_path')

pub_point = rospy.Publisher('realpoints_marker', Marker, queue_size=1)
print "Publisher created...."

rospy.Subscriber("/odometry/filtered",Odometry, callback)
print "Subcriber created...."
rospy.spin()
#!/usr/bin/env python
# import rospy
# from nav_msgs.msg import Path
# from nav_msgs.msg import Odometry
# from geometry_msgs.msg import PoseStamped
# path = Path()
# def odom_cb(data):
#     global path
#     path.header = data.header
#     pose = PoseStamped()
#     pose.header = data.header
#     pose.pose = data.pose.pose
#     path.poses.append(pose)
#     path_pub.publish(path)
# rospy.init_node('path_node')
# odom_sub = rospy.Subscriber('/odom_filtered', Odometry, odom_cb)
# path_pub = rospy.Publisher('/path', Path, queue_size=10)
# if __name__ == '__main__':
#     rospy.spin()
