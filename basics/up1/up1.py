import tensorflow as tf
sess = tf.InteractiveSession()

raw_data = [1., 2., 8., 4., -5., 6., 7.4, 3.6, 9.]
spike = tf.Variable(False) # Create a boolean variable caled spike
spike.initializer.run()

for i in range(1, len(raw_data)):
	if raw_data[i] - raw_data[i - 1] > 5:
		tf.assign(spike, True).eval()
	else:
		tf.assign(spike, False).eval()
	print("Spike", spike.eval())

sess.close()
