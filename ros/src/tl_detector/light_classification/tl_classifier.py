from styx_msgs.msg import TrafficLight
import cv2
import rospy
class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image, keep only the red pixels
        red = cv2.inRange(hsv_image, (0, 100, 100), (5, 255, 255))

        red = cv2.GaussianBlur(red, (9, 9), 2, 2)

        # Use the Hough transform to detect circles in the combined threshold image
        red_circles = cv2.HoughCircles(red, cv2.HOUGH_GRADIENT, 1, image.shape[0] / 8.0, 100, 50, 12, 0)



        if red_circles.shape:
            #print(red_circles.shape)
            #print("red circles ",len(red_circles[0,:]))  
            if(len(red_circles[0,:]) >= 2):
                rospy.loginfo("Red traffic light detected")
                return TrafficLight.RED
            else:
                return TrafficLight.UNKNOWN
                



        

        return TrafficLight.UNKNOWN
