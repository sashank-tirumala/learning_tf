#! /usr/bin/env python
import rospy
import actionlib
import actionlib_msgs
from geometry_msgs.msg import Twist, Vector3
from learning_tf.msg import circleGoal, circleAction, circleFeedback
class Client():
    def __init__(self):
        self.client = actionlib.SimpleActionClient(ns="go_circle", ActionSpec=circleAction)
        self.rate= rospy.Rate(10)
        self.per = 0
        self.sub = rospy.Subscriber(name="go_circle/feedback",data_class=circleFeedback, callback=self.cb, queue_size=10)
        self.client.wait_for_server()
        self.client.send_goal(circleGoal(True))
        while(self.client.get_state()<2):
            print(self.per)
            self.rate.sleep()
            self.client.cancel_goal()
        print("done my job")
    def cb(self,data):
        self.per = data.feedback.percent_complete

if(__name__=="__main__"):
    rospy.init_node("what_is_up")
    abc=Client()
    rospy.spin()
