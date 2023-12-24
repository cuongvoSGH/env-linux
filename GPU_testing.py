import torch as to 
import tensorflow as tf

print(f'Testing Pytorch GPU .... ')
print(to.cuda.is_available())
print(f'Testing Pytorch GPU done')
print(f'----------------------------------------------')
print(f'----------------------------------------------')
print(f'----------------------------------------------')
print(f'Testing Tensorflow GPU ...')
print(tf.config.list_physical_devices('GPU'))
print(f'Testing Tensorflow GPU done')
