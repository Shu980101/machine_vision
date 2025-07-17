import threading
import numpy
# from interfaces.robot_wrapper import RobotWrapper
from pick_and_place import Pick_Place
from std_msgs.msg import Bool
import os, rospkg, yaml
import rospy


class Algorithm:
    def __init__(self):
        self.is_on = False

        self.stopevent = threading.Event()
        self.pauseevent = threading.Event()

        self.startalgorithm_sub = rospy.Subscriber("/start_algorithm", Bool, self.start_callback)
        self.stopalgorithm_sub = rospy.Subscriber("/stop_algorithm", Bool, self.stop_callback)
        self.pausealgorithm_sub = rospy.Subscriber("/pause_algorithm", Bool, self.pause_callback)
        self.stopalgorithm_pub = rospy.Publisher("/stop_algorithm", Bool, queue_size=0)

    def start_callback(self, msg):
        if msg.data == True:
            self.stopevent.set()
            self.pauseevent.set()
            self.myalgorithm()

            msg = Bool()
            msg.data = True
            self.stopalgorithm_pub.publish(msg)        

    def stop_callback(self, msg):
        if msg.data == True:
            self.pauseevent.clear()
            self.stopevent.clear()

    def pause_callback(self, msg):
        if msg.data == True:
            self.pauseevent.clear()
        else:
            self.pauseevent.set()

    def set_pick_and_place(self, pick_place):
        self.pick_place = pick_place

    def myalgorithm(self):
        self.pick_place.back_to_home()

        # insert following two lines where you want to stop the algorithm 
        # with the stop button in GUI
        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick blue ball
        object_name = "blue_ball"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)

        grasp = self.pick_place.generate_grasp(object_name, "vertical", pose.position, 0.27, length=0.145)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("blue_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick yellow box
        object_name = "yellow_box"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)

        grasp = self.pick_place.generate_grasp(object_name, "vertical", pose.position, 0.55, yaw = 90, length=0.16)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("yellow_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick red box
        object_name = "red_box"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)

        grasp = self.pick_place.generate_grasp(object_name, "vertical", pose.position, length=0.16)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("red_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick yellow ball
        object_name = "yellow_ball"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)

        grasp = self.pick_place.generate_grasp(object_name, "vertical", pose.position, 0.55, length = 0.155)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("yellow_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick green cylinder
        object_name = "green_cylinder"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)
        pose.position.z += 0.02

        grasp = self.pick_place.generate_grasp(object_name, "horizontal", pose.position, 0.3, length = 0.13)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("green_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick red cylinder
        object_name = "red_cylinder"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)
        pose.position.z += 0.01

        grasp = self.pick_place.generate_grasp(object_name, "horizontal", pose.position, 0.45, length=0.14)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("red_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # pick blue box
        object_name = "blue_box"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)
        pose.position.x -= 0.02

        grasp = self.pick_place.generate_grasp(object_name, "horizontal", pose.position, 0.4, pitch = 60, length = 0.16)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("blue_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        # pick green ball
        object_name = "green_ball"
        pose = self.pick_place.get_object_pose(object_name)
        print(pose.position)

        grasp = self.pick_place.generate_grasp(object_name, "horizontal", pose.position, 0.37, pitch = 80, length=0.145)
        self.pick_place.pickup(object_name, [grasp])

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        goal_position = self.pick_place.get_target_position("green_target")
        x = goal_position.x
        y = goal_position.y
        z = goal_position.z+0.15
        place_pose = self.pick_place.pose2msg(0,0,0, x, y, z)
        print(place_pose.position)
        self.pick_place.place("vertical", place_pose.position)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.back_to_home()

        self.pick_place.send_message("Algorithm finished")



if __name__=="__main__":
    rospy.init_node("pick_place_basic")

    algo = Algorithm()
    algo.set_pick_and_place(Pick_Place())
    print("You can start your algorithm with GUI")

    rospy.spin()