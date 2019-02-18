'''
Code that captures embeddings of the face and saves them as 128D embedddings
Run using 'python3 input.py' in the terminal

'''
import cv2
from utils.align_custom import AlignCustom
from utils.face_feature import FaceFeature
from utils.mtcnn_detect import MTCNNDetect
from utils.tf_graph import FaceRecGraph
import argparse
import sys
from utils.sound_record import record_to_file
from utils.sound_recognise import label_wav
import json
import numpy as np
import time

count=0

def main():
	create_manual_data();

def create_manual_data():
	count=1
	recval=0
	vs = cv2.VideoCapture(0); #Input taken using webcam

	while True :
		f = open('./face_database.txt','r');
		data_set = json.loads(f.read());
		person_imgs = {"Center": []};
		person_features = {"Center": []};
		while True:
			_,frame = vs.read();
			rects, landmarks = face_detect.detect_face(frame, 80);  # min face size is set to 80x80
			for (i, rect) in enumerate(rects):
				cv2.rectangle(frame,(rect[0],rect[1]),(rect[0] + rect[2],rect[1]+rect[3]),(255,0,0)) #draw bounding box for the face
				aligned_frame, pos = aligner.align(160,frame,landmarks[i]);
				if len(aligned_frame) == 160 and len(aligned_frame[0]) == 160:
					if(pos=="Center"):
						person_imgs[pos].append(aligned_frame)
			cv2.imshow("frame",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				vs.release()
				cv2.destroyAllWindows()
				break

			if rects == []:
				recval=0
				break
			else:
				recval=recval+1

			if (recval>=10):
				for pos in person_imgs:
					person_features[pos] = [np.mean(extract_feature.get_features(person_imgs[pos]),axis=0).tolist()]
				
				print('Speak your sweet of choice')
				record_to_file()
				
				final_name=label_wav()
				while(final_name=='unknown'):
					print('Speak your name')
					record_to_file()
					final_name=label_wav()
					final_name=final_name+str(count)
					print(final_name)

					data_set[final_name] = person_features;
					f = open('./face_database.txt', 'w');
					f.write(json.dumps(data_set))
					print("User",final_name,"added")
					recval=0
					count=count+1
					time.sleep(3)
					break;

if __name__ == '__main__':
	FRGraph = FaceRecGraph();
	aligner = AlignCustom();
	extract_feature = FaceFeature(FRGraph)
	face_detect = MTCNNDetect(FRGraph, scale_factor=2); #Images are rescaled for faster detection
	main();
	cv2.destroyAllWindows()
