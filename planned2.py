#!/usr/bin/env python

import rospy
from visualization_msgs.msg import  Marker
from geometry_msgs.msg import Point
import math

rospy.init_node('points_and_lines', anonymous=True)
marker_pub = rospy.Publisher("pl_publisher", Marker, queue_size=10)
marker_pub_green = rospy.Publisher("pl_publisher_green", Marker, queue_size=10)
rate = rospy.Rate(30)
points = Marker()
line_strip = Marker()
line_strip_green = Marker()

######### POINT LIST ######
points_list = [0.0, 0.0, -0.26, -3.59, -0.26, -3.59, -0.19, -5.37, -0.19, -5.37, 8.35, -4.03, 8.35, -4.03, 8.37, -6.26, 8.37, -6.26, 5.31, -4.75, 5.31, -4.75, -1.05, -5.32, -1.05, -5.32, -0.27, -9.04, -0.27, -9.04, 4.18, -12.83, 4.18, -12.83, 10.06, -14.79, 10.06, -14.79, 16.88, -11.26, 16.88, -11.26, 24.2, -3.76, 24.2, -3.76, 23.46, 1.94, 23.46, 1.94, 26.39, 4.35, 26.39, 4.35, 22.73, 4.89, 22.73, 4.89, 22.40, -2.45, 22.40, -2.45, 16.56,5.61, 16.56,5.61, 15.58, 0.094, 15.58, 0.094, 7.71, 0.81, 7.71, 0.81, 0.0, 0.0]
# points_list_green = [0.0, 0.0, -0.26, -3.59, -0.26, -3.59, -0.19, -5.37, -0.19, -5.37, 8.35, -4.03, 8.35, -4.03, 8.37, -6.26]

# x1 = 0.59
# y1 = -6.20

# x1 = 4.18
# y1 = -13.46

# x1 = 11.63
# y1 = -16.85

# x1 = 15.5
# y1 = -11.18

# x1 = 18.08
# y1 = -5.9

# x1 = 28.62
# y1 = -6.17

# x1 = 29.16
# y1 = 0.0

# x1 = 25.04
# y1 = 4.36

def main():


    points.header.frame_id = line_strip.header.frame_id = line_strip_green.header.frame_id =  'map'
    points.header.stamp = line_strip.header.stamp = line_strip_green.header.stamp = rospy.Time.now()
    points.ns = line_strip.ns = line_strip_green.ns = "points_and_lines"
    points.action = line_strip.action = line_strip_green.action = Marker.ADD
    points.pose.orientation.w = line_strip.pose.orientation.w = line_strip_green.pose.orientation.w = 1.0

    points.id = 0
    line_strip.id = 1
    line_strip_green.id = 1

    points.type = Marker.POINTS
    line_strip.type = Marker.LINE_LIST
    line_strip_green.type = Marker.LINE_LIST

    # POINTS: x and y for width and height
    points.scale.x = 0.2
    points.scale.y = 0.2

    # LINE_LIST: only x for width
    line_strip.scale.x = 0.1
    line_strip_green.scale.x = 0.1

    # Points are green
    points.color.g = 1.0
    points.color.a = 1.0

    # Linestrip 1 is blue
    line_strip.color.b = 1.0
    line_strip.color.a = 1.0

    # Linestrip 2 is green
    line_strip_green.color.g = 1.0
    line_strip_green.color.a = 1.0

    # print(len(points_list))

    while not rospy.is_shutdown():
        for i in xrange(0,len(points_list),2):
            p = Point()
            p.x = points_list[i]
            p.y = points_list[i+1]

            # points.points.append(p)
            line_strip.points.append(p)

        # for j in xrange(0,len(points_list_green),2):
        #     q = Point()
        #     q.x = points_list_green[j]
        #     q.y = points_list_green[j+1]

        #     #points.points.append(q)
        #     line_strip_green.points.append(q)
            


        
        #marker_pub.publish(points)
        marker_pub.publish(line_strip)
        # marker_pub_green.publish(line_strip_green)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except:
        pass


    


