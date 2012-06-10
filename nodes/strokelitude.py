#!/usr/bin/env python

# roschart_feeder/strokelitude.py
# send data from a strokelitude stream to roschart
# JAB 6/9/12

import roslib; roslib.load_manifest( 'roschart_feeder' )
import rospy

from roschart.msg import Point
from strokelitude_ros.msg import FlyWingEstimate

class StrokelitudeFeeder:
    def __init__( self ):
        """Initialize a strokelitude subscriber and a roschart publisher."""
        rospy.init_node( 'roschart_feeder', anonymous=True )

        rospy.Subscriber( 'strokelitude', FlyWingEstimate, self.wingstroke_callback )

        self.publisher = rospy.Publisher( 'roschart', Point )

        rospy.spin()

    def wingstroke_callback( self, wingstroke_data ):
        """Extract data from a wingstroke data message and republish for roschart."""
        pt = Point( wingstroke_data.left_wing_angle_radians,
                    float( wingstroke_data.header.stamp.secs +
                           wingstroke_data.header.stamp.nsecs/1e9 ) )
        self.publisher.publish( pt )

if __name__ == '__main__':
    feeder = StrokelitudeFeeder()
