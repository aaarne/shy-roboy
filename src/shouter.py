#!/usr/bin/env python

import rclpy
from std_msgs.msg import Int8
from roboy_cognition_msgs.srv import Talk

shout_node = None
last_state = 0
current_state = 0

def process_state(data):
    global current_state
    global last_state
    current_state = data.data
    if current_state == 2 and last_state != 2:
        shout()
    if current_state == 0 and last_state == 3:
        thank()
    last_state = current_state

def shout():
    global shout_node
    client = shout_node.create_client(Talk,'roboy/cognition/speech/synthesis/talk')
    request = Talk.Request()
    request.text = "Please don't touch me"
    print("Trying to shout. Hope someone hears me")
    future = client.call_async(request) 
    #rclpy.spin_until_future_complete(shout_node, future)
    
def thank()
    global shout_node
    client = shout_node.create_client(Talk,'roboy/cognition/speech/synthesis/talk')
    request = Talk.Request()
    request.text = "Thanks for leaving me alone"
    print("Trying to thank. Hope someone hears me")
    future = client.call_async(request) 
    
rclpy.init()
shout_node = rclpy.create_node('shouter')
shout_node.create_subscription(Int8, 'shy_roboy/state',  process_state)
while rclpy.ok():
    rclpy.spin_once(shout_node)
shout_node.destroy_node()
rclpy.shutdown()

