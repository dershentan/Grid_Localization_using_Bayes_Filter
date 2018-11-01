import rosbag
from nav_msgs.msg import Odometry

def transformTagsToRobotFrame(tags):
    result = []
    for t in tags:
        camera_x, camera_y, camera_z = t.pose.pose.position.x, t.pose.pose.position.y, t.pose.pose.position.z
        robot_x, robot_y, robot_z = camera2Robot(camera_x, camera_y, camera_z)
        result.append((t.id, robot_x, robot_y, robot_z))
    return result

def camera2Robot(camera_x, camera_y, camera_z):
    robot_x = camera_z
    robot_y = -1 * camera_x
    robot_z = camera_y
    return robot_x, robot_y, robot_z

def main():
    with rosbag.Bag('lab4.bag') as bag:
        for topic, msg, t in bag.read_messages(['/tag_detections']):
            tags = transformTagsToRobotFrame(msg.detections)
            print(tags)

if __name__ == '__main__':
    main()
