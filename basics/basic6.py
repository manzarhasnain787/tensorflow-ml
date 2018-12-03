import tensorflow as tf

# graph = tf.Graph()
# with graph.as_default():
# 	variable = tf.Variable(42, name='foo')

# Build the graph
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

# # Launch the graph in session
# sess = tf.Session()
#
# # Evaluate the tensor result or execute and close the session
# print(sess.run(c))
# sess.close()

# or autoclose the above with session
with tf.Session() as sess:
	print(sess.run(c))
