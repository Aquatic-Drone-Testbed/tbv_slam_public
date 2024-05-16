#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import socket

def udp_receiver():
    rospy.init_node('udp_receiver_node', anonymous=True)
    pub = rospy.Publisher('udp_messages', String, queue_size=10)
    
    udp_ip = "0.0.0.0"
    udp_port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))

    rospy.loginfo("UDP receiver node started on port %d", udp_port)

    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        rospy.loginfo("Received message: %s", data)
        pub.publish(data)

    sock.close()

if __name__ == '__main__':
    try:
        udp_receiver()
    except rospy.ROSInterruptException:
        pass
