import threading
import numpy
from pick_and_place import Pick_Place
from move_base_client import Movebase_Client
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

            self.pick_place.send_message("Algorithm is finished")

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

    def set_client(self, movebase_client):
        self.client = movebase_client

    def move_to(self, target_name):
        pose = self.client.get_target_pose(target_name)
        self.client.send_goal_to_client(pose)
        while self.client.get_result_from_client() != True:
            pass
        print(self.pick_place.get_robot_pose())

    def myalgorithm(self):
        ############## Insert your code here ###############
        # Move the robot back to home as a start
        self.pick_place.back_to_home()

        ##### first object
        self.move_to("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home()
        print("robot pose:",self.pick_place.get_robot_pose())

        self.pick_place.spawn_obstacle_rviz("conveyor1")
        self.pick_place.spawn_all_objects()

        object_name = "yellow_ball"
        pose = self.pick_place.get_object_pose(object_name)
        print("object pose:",pose)

        pose.position.z -= 0.01
        self.pick_place.pickup(object_name, pose.position, 0.5)
        self.pick_place.back_to_home(False)

        self.pick_place.clean_all_objects_in_scene()
        self.pick_place.clean_scene("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # move to place
        target_name = "conveyor3"
        self.move_to(target_name)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home(False)
        self.pick_place.spawn_obstacle_rviz(target_name)

        position = self.pick_place.get_target_position(target_name)
        print(position)
        self.pick_place.place(object_name, position)

        self.pick_place.clean_scene(target_name)
        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        ##### second object
        self.move_to("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home()
        print("robot pose:",self.pick_place.get_robot_pose())

        self.pick_place.spawn_obstacle_rviz("conveyor1")
        self.pick_place.spawn_all_objects()

        object_name = "green_cylinder"
        pose = self.pick_place.get_object_pose(object_name)
        print("object pose:",pose)

        pose.position.z -= 0.01
        self.pick_place.pickup(object_name, pose.position, 0.48)
        self.pick_place.back_to_home(False)

        self.pick_place.clean_all_objects_in_scene()
        self.pick_place.clean_scene("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return
        
        # move to place
        target_name = "conveyor2"
        self.move_to(target_name)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home(False)
        self.pick_place.spawn_obstacle_rviz(target_name)

        position = self.pick_place.get_target_position(target_name)
        print(position)
        self.pick_place.place(object_name, position)

        self.pick_place.clean_scene(target_name)
        self.pick_place.back_to_home()

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        ##### third object
        self.move_to("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home()
        print("robot pose:",self.pick_place.get_robot_pose())

        self.pick_place.spawn_obstacle_rviz("conveyor1")
        self.pick_place.spawn_all_objects()

        object_name = "blue_box"
        pose = self.pick_place.get_object_pose(object_name)
        print("object pose:",pose)

        pose.position.z -= 0.01
        self.pick_place.pickup(object_name, pose.position, 0.5)
        self.pick_place.back_to_home(False)

        self.pick_place.clean_all_objects_in_scene()
        self.pick_place.clean_scene("conveyor1")

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        # move to place
        target_name = "conveyor4"
        self.move_to(target_name)

        while (not self.pauseevent.isSet()) or (not self.stopevent.isSet()):
            if not self.stopevent.isSet():
                return

        self.pick_place.move_to_pick_place_home(False)
        self.pick_place.spawn_obstacle_rviz(target_name)

        position = self.pick_place.get_target_position(target_name)
        print(position)
        self.pick_place.place(object_name, position)

        self.pick_place.clean_scene(target_name)
        self.pick_place.back_to_home()


if __name__=="__main__":
    rospy.init_node("pick_place")

    algo = Algorithm()
    algo.set_pick_and_place(Pick_Place())
    algo.set_client(Movebase_Client())
    print("You can start your algorithm with GUI")

    rospy.spin()