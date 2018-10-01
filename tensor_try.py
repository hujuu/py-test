import tensorflow as tf
tf.enable_eager_execution()
res = tf.add(1, 2)
print(res)

hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy())

zero_tsr = tf.zeros([2, 2])
print(zero_tsr)