#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose

robot_pose = Pose()

def service_callback(request):
    print "Robot's Pose:"
    print robot_pose
    return EmptyResponse

def sub_callback(msg):
    global robot_pose
    robot_pose = msg.pose.pose


rospy.init_node('service_server')
my_service = rospy.Service('/get_pose_service', Empty , service_callback) # create the Service called get_pose_service with the defined callback
sub_pose = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, sub_callback)
rospy.spin() # mantain the service open.