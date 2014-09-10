#!/usr/bin/env python

import roslib
import rospy
import actionlib
from baxter_utils.msg import *

if __name__ == "__main__":
    rospy.init_node("baxter_joint_trajectory_file_playback_action_client")
    client = actionlib.SimpleActionClient('baxter_joint_trajectory_file_playback', PlaybackTrajectoryFileAction)
    client.wait_for_server()

    goal = PlaybackTrajectoryFileGoal()
    goal.trajectory_file_path = rospy.myargv(argv=sys.argv)[1]
    # Fill in the goal here
    client.send_goal(goal)
    client.wait_for_result()