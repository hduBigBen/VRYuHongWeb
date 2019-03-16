import os
import cv2
def  imagetovideo():
	#########################################################################################################
	########################### Change These Values to your specifications ##################################
	imagesInputTypes = 'jpg'  ### For best results use png
	imagesInputPath = './Images'  ### director can be like /home/B8con/images/tempImages
	videoOutputPath = 'VideoSample.mp4'  ### File type should be mp4
	frameRate = 25  ### The higher the fame rate the shorter the film
	#########################################################################################################
	#########################################################################################################

	dir_path = imagesInputPath
	ext = imagesInputTypes
	output = videoOutputPath
	images = []
	for f in os.listdir(dir_path):
		if f.endswith(ext):
			images.append(f)

	###### SETS THE SIZE OF THE VIDEO BASED ON THE SIZE OF THE FIRST IMAGE CAPUTED
	image_path = os.path.join(dir_path, images[0])
	frame = cv2.imread(image_path)
	# cv2.imshow('video',frame)  ###### Enable if you want to see the video being constructed
	height, width, channels = frame.shape

	###### DEFINE CODEC AND CREATE VIDEOWRITER OBJECT
	# fourcc = cv2.CV_FOURCC('m', 'p', '4', 'v') ###### BE SURE TO USE ALL LOWER CASE AND COMAS
	fourcc = cv2.VideoWriter_fourcc(*'XVID')

	out = cv2.VideoWriter(output, fourcc, frameRate,
						  (width, height))  ###### INT VALUE ALLOWS YOU TO ADJUST FRAMES PER SECOND.

	imageCount = 0
	i = 0
	finalImage = images[-75:]
	finalImage += images[-75:]

	for image in finalImage:
		image_path = os.path.join(dir_path, image)
		frame = cv2.imread(image_path)

		out.write(frame)  # Write out frame to video

		imageCount += 1
		i += 1

	out.release()
	cv2.destroyAllWindows()

