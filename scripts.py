import numpy as np
import tensorflow as tf
import os


graph_def = tf.GraphDef()
labels = ["0","1","2"]

# Import the TF graph
with tf.gfile.FastGFile("model.pb", 'rb') as f:
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Create a list of labels.
with open("labels.txt", 'rt') as lf:
    for l in lf:
        labels.append(l.strip())
