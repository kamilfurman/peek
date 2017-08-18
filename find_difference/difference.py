import os
import cv2
import numpy as np

def get_quality_score(img_diff):
	# Normalize: transform domain from [0,255] to [0,1]
	pixel_count = len(img_diff)*len(img_diff[0])
	difference_score = np.sum(img_diff)*1.0 / pixel_count
	return 100 - difference_score


def get_absolute_image_difference(img1, img2):
	return cv2.absdiff(img1, img2)


def get_difference_image(img1, img2, show_images=False):
	cv2.GaussianBlur(img1, (5,5), 10, img1)
	cv2.GaussianBlur(img2, (5,5), 10, img2)

	diff = get_absolute_image_difference(img1, img2)
	retval, thresholded = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
	#cv2.adaptiveThreshold(diff, 255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
	#	thresholdType=cv2.THRESH_BINARY_INV, blockSize=3, C=4, dst=diff) 

	if show_images:
		cv2.imshow("control", img1)
		cv2.imshow("query", img2)
		cv2.imshow("difference", diff)
		cv2.imshow("thresholded", thresholded)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	return diff


if __name__ == "__main__":
	img1_path = "../img/sample_control.jpg"
	img2_path = "../img/sample_aligned_damaged.jpg"
	#img2_path = "../img/sample_aligned_undamaged.jpg"
	img1 = cv2.imread(img1_path, 0);
	img2 = cv2.imread(img2_path, 0);

	img_diff = get_difference_image(img1, img2, True)

	damage_prob = get_quality_score(img_diff)
	print damage_prob

