import os
print(os.path.basename('path/to/file/001015io.png'))


filename = '001015io.png'

x = filename[0:3]
y = filename[3:6]
status = filename[6:8]

print(x, y, status)