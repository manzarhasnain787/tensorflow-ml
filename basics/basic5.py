import tensorflow as tf

norm = tf.random_normal([2,3], mean=-1, stddev=4)
print(norm)

c = tf.constant([[1,2], [3,4], [5,6]])
stuff = tc.random_shuffle(c)
