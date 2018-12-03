# each row of tensor => money transaction
# row => [1,2,3,4,5,6,7,8,9,10]
import tensorflow as tf

x = tf.constant([[1, 2]])
neg_x = tf.negative(x)
print(neg_x)
