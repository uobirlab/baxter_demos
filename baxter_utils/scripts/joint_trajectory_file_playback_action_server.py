#!/usr/bin/env python

import roslib
import rospy
import actionlib
from baxter_utils.msg import *
import os.path
import imp
from control_msgs.msg import FollowJointTrajectoryResult

# Read in the existing code for playing back files so we don't need to rewrite that

playback_file = roslib.packages.get_pkg_dir('baxter_examples') + '/scripts/joint_trajectory_file_playback.py'
jtfp = imp.load_source('joint_trajectory_file_playback', playback_file)

class BaxterJointTrajectoryFilePlaybackActionServer:
  def __init__(self):
    self.server = actionlib.SimpleActionServer('baxter_joint_trajectory_file_playback', PlaybackTrajectoryFileAction, self.execute, False)
    self.server.start()

  def execute(self, goal):
 
    rospy.loginfo('Received goal to run: %s' % goal.trajectory_file_path)
    result = PlaybackTrajectoryFileResult()

    if not os.path.isfile(goal.trajectory_file_path):
        rospy.logerr('Trajectory file not found: %s' % goal.trajectory_file_path)        
        result.result = False
        self.server.set_aborted(result)
        return

    traj = jtfp.Trajectory()
    traj.parse_file(path.expanduser(goal.trajectory_file_path))

    #for safe interrupt handling
    rospy.on_shutdown(traj.stop)

    traj.start()
    result.result = traj.wait()
    self.server.set_succeeded(result)


if __name__ == "__main__":
    rospy.init_node("baxter_joint_trajectory_file_playback_action_server")
    print("Getting robot state... ")
    rs = baxter_interface.RobotEnable()
    print("Enabling robot... ")
    rs.enable()
    print("Running. Ctrl-c to quit")

    server = BaxterJointTrajectoryFilePlaybackActionServer()
    rospy.spin()
