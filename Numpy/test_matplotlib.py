from matplotlib import pyplot as plt
import random

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
     'December']
y = [
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random(),
    random.random()
]

plt.plot(x, y)
plt.title('User per month')
plt.xlabel('Month')
plt.ylabel('User')
plt.show()
