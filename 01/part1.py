#!/usr/bin/env python3

import sys

numbers = []
increases = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part1.py input.txt")
	exit(1)

# Read File + Get Numbers
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for num in data:
		numbers.append(int(num))

# Start 
last_num = float('inf')
for i, current_num in enumerate(numbers):
	if (current_num > last_num):
		increases = increases + 1
		
	last_num = current_num

# Answer
print(f"answer: {increases}")