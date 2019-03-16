import os
import cv2

def  imagetovideo():
	#########################################################################################################
	########################### Change These Values to your specifications ##################################
	imagesInputTypes = 'jpg'  ### For best results use png
	imagesInputPath = './Images'  ### director can be like /home/B8con/images/tempImages
	videoOutputPath = 'VideoSample.mp4'  ### File type should be mp4
	frameRate = 15  ### The higher the fame rate the shorter the film
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
	for image in images:
		image_path = os.path.join(dir_path, image)
		frame = cv2.imread(image_path)

		out.write(frame)  # Write out frame to video

		imageCount += 1
		i += 1

	out.release()
	cv2.destroyAllWindows()

def videoFaceDet():
	global IMAGES_PATH
	global FrameId
	IMAGES_PATH = ".//Images//{:06d}.jpg"
	FrameId = 0
	video = cv2.VideoCapture(0)
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	count = 0
	while True:
		check, frame = video.read()
		# grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=5)
		# t=0

		# for x, y, w, h in faces:
		# 	if t==0:
		# 		videoImag = frame[x-80:x + 220 , y-30:y + 270 ]
		# 		#cv2.imshow("Capturing", videoImag)
		# 		#if count < 100:
		# 		cv2.imwrite(IMAGES_PATH.format(FrameId), videoImag)
		# 		FrameId += 1
		# 	t=t+1
		# cv2.imwrite(IMAGES_PATH.format(FrameId), frame)
		cv2.imwrite(IMAGES_PATH.format(FrameId), frame[0:480, 80:560])
		FrameId += 1
		if FrameId == 74:
			FrameId = 0
		key=cv2.waitKey(1)
		count +=1
		if key == ord(' '):
			cv2.waitKey(0)
			imagetovideo()
		elif key==ord('q'):
			break
	cv2.destroyAllWindows()


global  IMAGES_PATH
global  FrameId
