'''
Code for recognition of people and to deliver the sweet selected by the user.
Run using 'python3 recognition.py' 
'''

import cv2
from utils.align_custom import AlignCustom
from utils.face_feature import FaceFeature
from utils.mtcnn_detect import MTCNNDetect
from utils.tf_graph import FaceRecGraph
import argparse
import sys
import json
import numpy as np
import time
import os, sys

count=0

def main():
    camera_recog()
  
def camera_recog():
    count=0
    recog_data=[('', 0)]
    print("Camera sensor warming up...")
    vs = cv2.VideoCapture(0);
    while True:
        _,frame = vs.read();
        rects, landmarks = face_detect.detect_face(frame,80); #Face size is set to 80x80
        aligns = []
        positions = []
        #print(rects)
        for (i, rect) in enumerate(rects):
            aligned_face, face_pos = aligner.align(160,frame,landmarks[i])
            if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
                aligns.append(aligned_face)
                positions.append(face_pos)
            else: 
                print("Align face failed")
            prev_recog = recog_data[0][0]       
            if(len(aligns) == 1 and face_pos=='Center') :
                # print(len(aligns))
                features_arr = extract_feature.get_features(aligns)
                recog_data = findPeople(features_arr,positions);
                cv2.rectangle(frame,(rect[0],rect[1]),(rect[0] + rect[2],rect[1]+rect[3]),(255,0,0))
                cv2.putText(frame,recog_data[0][0]+" - "+str(recog_data[0][1])+"%",(rect[0],rect[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
                per = recog_data[0][0]

                if(per[0]=='l'):
                    if(per != prev_recog):
                        count=0
                    count=count+1
                    print("........>",count)
                    if (count==7):
                        print("FINAL LABEL:",per)
                        count=0
                        time.sleep(0.3)

                if(per[0]=='m'):
                    if(per != prev_recog):
                        count=0
                    count=count+1
                    print("........>",count)
                    if (count==7):
                        print("FINAL LABEL:",per)
                        count=0
                        time.sleep(0.3)

                if(per[0]=='p'):
                    if(per != prev_recog):
                        count=0
                    count=count+1
                    print("........>",count)
                    if (count==10):
                        print("FINAL LABEL:",per)
                        count=0
                        time.sleep(0.3)			
 
        cv2.imshow("Hey there",frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

def findPeople(features_arr, positions, thres = 0.70, percent_thres = 70): 
    ''' Function to check the saved faces in the database.
        Recognition threshold is set to 70% and can be altered according to requirement '''
    
    f = open('./face_database','r')
    data_set = json.loads(f.read());
    returnRes = [];
    for (i,features_128D) in enumerate(features_arr):
        result = "Unknown";
        smallest = sys.maxsize
        for person in data_set.keys():
            person_data = data_set[person][positions[0]];
            for data in person_data:
                distance = np.sqrt(np.sum(np.square(data-features_128D)))
                if(distance < smallest):
                    smallest = distance;
                    result = person;
        percentage =  min(100, 100 * thres / smallest)
        if percentage <= percent_thres :
            result = "Unknown"
        returnRes.append((result,percentage))
        #print(result)
    return returnRes


if __name__ == '__main__':
    FRGraph = FaceRecGraph()
    aligner = AlignCustom()
    extract_feature = FaceFeature(FRGraph)
    face_detect = MTCNNDetect(FRGraph, scale_factor=2); # rescales image for faster detection
    main()
