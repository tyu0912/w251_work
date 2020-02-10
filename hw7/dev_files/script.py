from PIL import Image

import sys
import os
import urllib
import tensorflow.contrib.tensorrt as trt

import tensorflow as tf
import numpy as np
import time

import cv2

print("\nThings imported successfully\n") 

# Setting variables
FROZEN_GRAPH_NAME = 'data/frozen_inference_graph_face.pb'
IMAGE_PATH = 'data/warriors.jpg'

INPUT_NAME='image_tensor'
BOXES_NAME='detection_boxes'
CLASSES_NAME='detection_classes'
SCORES_NAME='detection_scores'
MASKS_NAME='detection_masks'
NUM_DETECTIONS_NAME='num_detections'
DETECTION_THRESHOLD=0.5

input_names = [INPUT_NAME]
output_names = [BOXES_NAME, CLASSES_NAME, SCORES_NAME, NUM_DETECTIONS_NAME]

# Load the frozen graph

output_dir=''
frozen_graph = tf.GraphDef()
with open(os.path.join(output_dir, FROZEN_GRAPH_NAME), 'rb') as f:
    frozen_graph.ParseFromString(f.read())

# Optimize the frozen graph using TensorRT

trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,
    outputs=output_names,
    max_batch_size=1,
    max_workspace_size_bytes=1 << 25,
    precision_mode='FP16',
    minimum_segment_size=50
)

# Create session and load graph

tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True

tf_sess = tf.Session(config=tf_config)

# use this if you want to try on the optimized TensorRT graph
# Note that this will take a while
# tf.import_graph_def(trt_graph, name='')

# use this if you want to try directly on the frozen TF graph
# this is much faster
tf.import_graph_def(frozen_graph, name='')

tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores:0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes:0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes:0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections:0')

# Load and Preprocess Image

#image = Image.open(IMAGE_PATH)
#plt.imshow(image)

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    img = cv2.resize(img, (300, 300), interpolation = cv2.INTER_AREA)
    cv2.imshow("frame", img)

    # Run network on Image

    #image_np = np.array(img)

    #scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections], feed_dict={
    #    tf_input: image_np[None, ...]
    #})


    #boxes = boxes[0] # index by 0 to remove batch dimension
    #scores = scores[0]
    #classes = classes[0]
    #num_detections = num_detections[0]
           
    #box = boxes * np.array([image_np.shape[0], image_np.shape[1], image_np.shape[0], image_np.shape[1]])
    #img_resized = cv2.rectangle(img_resized, (int(box[1]), int(box[0])), (int(box[3] - box[1]), int(box[2] - box[0])), (255,0,0), 2)

    # cv2.imshow("frame", img_resized)


        # scale box to image coordinates
        # box = boxes[i] * np.array([image.shape[0], image.shape[1], image.shape[0], image.shape[1]])

        # display rectangle
        # patch = patches.Rectangle((box[1], box[0]), box[3] - box[1], box[2] - box[0], color='g', alpha=0.3)

        # display class index and score
        # plt.text(x=box[1] + 10, y=box[2] - 10, s='%d (%0.2f) ' % (classes[i], scores[i]), color='w')
    

    # Benchmark

    #num_samples = 50
    #t0 = time.time()

    #for i in range(num_samples):
    #    scores, boxes, classes, num_detections = tf_sess.run([tf_scores, tf_boxes, tf_classes, tf_num_detections], feed_dict={
    #        tf_input: image_resized[None, ...]
    #    })
    
    #t1 = time.time()
    #print('Average runtime: %f seconds' % (float(t1 - t0) / num_samples))


# Close Session
tf_sess.close()
