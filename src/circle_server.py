#! /usr/bin/env python
import rospy
import actionlib
import actionlib_msgs
from learning_tf.msg import circleAction, circleFeedback, circleGoal
from geometry_msgs.msg import Twist, Vector3
import turtlesim.msg
class Server():
    def __init__(self):
        self.server = actionlib.SimpleActionServer(name="go_circle", ActionSpec=circleAction, execute_cb=self.execute, auto_start=False)
        self.pub=rospy.Publisher(name="/turtle1/cmd_vel", data_class=Twist, queue_size=10)
        self.sub=rospy.Subscriber(name="turtle1/pose", data_class=turtlesim.msg.Pose, callback=self.getAngle, queue_size=10)
        self.angle=0
        self.pub_vel = Twist()
        x = Vector3(1,0,0)
        ang = Vector3(0,0,1)
        self.pub_vel.angular=ang
        self.pub_vel.linear=x
        self.current_goal = 3.14/2
        self.server.start()

    def execute(self,goal):
        while(self.angle< self.current_goal):
            self.pub.publish(self.pub_vel)
            percent_feedback = self.angle/self.current_goal
            percent_feedback=percent_feedback*100
            self.server.publish_feedback(circleFeedback(percent_feedback))
        self.current_goal = self.angle+3.14/2
        self.server.set_succeeded()

    def getAngle(self, data):
        self.angle =data.theta

if(__name__ == "__main__"):
    rospy.init_node("god",anonymous=False)
    abc =Server()
    rospy.spin()
