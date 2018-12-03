import tensorflow as tf

# computation A
x = tf.constant([[1., 2,]])
neg_op = tf.negative(x)

# run with session and execute and then close session
with tf.Session() as sess:
	result = sess.run(neg_op)
	print(result)
