import numpy as np 
import array

fk_pos = [12, 45, 67]
ik_pos = [45, 67, 34]
motorPos = np.tile(np.float32(90.01293), 6)

str_output = ','.join(map(str, motorPos)) + ","
str_output += ','.join(map(str, fk_pos)) + ","
str_output += ','.join(map(str, ik_pos))

print(str_output)