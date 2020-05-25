import tensorflow as tf

message = tf.constant('Hello World!')
with tf.Session() as sess:
    print(sess.run(message).decode())
