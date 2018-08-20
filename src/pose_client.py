#! /usr/bin/env python
import rospy
from learning_tf.srv import poseRequest, poseResponse, pose
from turtlesim.msg import Pose
import tf2_ros
import tf_conversions
from geometry_msgs.msg import TransformStamped, Vector3
class Client:
    def __init__(self):
        self.client = rospy.ServiceProxy(name="get_pose", service_class=pose)
        self.client.wait_for_service()
        self.br = tf2_ros.TransformBroadcaster()
    def post_transform(self, der):
        temp = TransformStamped()
        temp.child_frame_id="turtle2"
        temp.header.frame_id="world"
        temp.header.stamp = rospy.Time.now()
        temp.transform.translation = Vector3(der.x, der.y, 0)
        q = tf_conversions.transformations.quaternion_from_euler(0,0,der.theta)
        temp.transform.rotation.x = q[0]
        temp.transform.rotation.y = q[1]
        temp.transform.rotation.z = q[2]
        temp.transform.rotation.w = q[3]
        self.br.sendTransform(transform=temp)



if(__name__=="__main__"):
    rospy.init_node("client")
    abc = Client()
    while(not rospy.is_shutdown()):
        der = abc.client.call(poseRequest())
        der = der.pose
        abc.post_transform(der)
