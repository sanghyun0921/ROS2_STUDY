import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlesimPublisher(Node):

    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Use W/A/S/D keys to move the turtle. Press Q to quit.")

def main(args=None):
    rclpy.init(args=args)
    node = TurtlesimPublisher()

    try:
        while True:
            key = input("Enter command (w/a/s/d/q): ").lower()
            msg = Twist()

            if key == 'w':

                msg.linear.x = 2.0

            elif key == 'a':
                
                msg.angular.z = 2.0
                
            elif key == 's':

                msg.linear.x = -2.0
                
            
            elif key == 'd':
               
                msg.angular.z = -2.0

            elif key == 'q':
            	
                node.get_logger().info("Shut down")
                break
          

            node.publisher.publish(msg)

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
