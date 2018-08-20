#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3
from turtlesim.msg import Pose
from learning_tf.srv import pose, poseRequest, poseResponse
class Service:
    def __init__(self):
        self.services = rospy.Service(name="get_pose", service_class=pose, handler=self.serv )
        self.sub = rospy.Subscriber(name="turtle1/pose", data_class=Pose, callback=self.cb, queue_size=10)
        self.pose = Pose()

    def cb(self, data):
        self.pose = data

    def serv(self, req):
        a = poseResponse(self.pose)
        return a

if(__name__=="__main__"):
    rospy.init_node("pose_provider")
    abc = Service()
    rospy.spin()
