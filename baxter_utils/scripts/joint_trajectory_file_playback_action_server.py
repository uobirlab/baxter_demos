#!/usr/bin/env python

import roslib

import imp

# Read in the existing code for playing back files so we don't need to rewrite that

playback_file = roslib.packages.get_pkg_dir('baxter_examples') + '/scripts/joint_trajectory_file_playback.py'
jtfp = imp.load_source('joint_trajectory_file_playback', playback_file)






def main():
    rospy.init_node("rsdk_joint_trajectory_file_playback_action_server")
    # print("Getting robot state... ")
    # rs = baxter_interface.RobotEnable()
    # print("Enabling robot... ")
    # rs.enable()
    # print("Running. Ctrl-c to quit")


    traj = jtfp.Trajectory()
    traj.parse_file(path.expanduser(args.file))
    #for safe interrupt handling
    rospy.on_shutdown(traj.stop)
    result = True
    loop_cnt = 1
    loopstr = str(args.loops)
    if args.loops == 0:
        args.loops = float('inf')
        loopstr = "forever"
    while (result == True and loop_cnt <= args.loops
           and not rospy.is_shutdown()):
        print("Playback loop %d of %s" % (loop_cnt, loopstr,))
        traj.start()
        result = traj.wait()
        loop_cnt = loop_cnt + 1
    print("Exiting - File Playback Complete")

if __name__ == "__main__":
    main()
