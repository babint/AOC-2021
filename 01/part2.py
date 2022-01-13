#!/usr/bin/env python3

import sys

numbers = []
increases = 0

# Usage
if len(sys.argv) != 2:
	print("usage: part2.py input.txt")
	exit(1)

# Read File + Get Numbers
with open(sys.argv[1]) as f:
	data = f.read().splitlines()

	for num in data:
		numbers.append(int(num))

# Start 
num_1 = numbers.pop(0)
num_2 = numbers.pop(0)
num_3 = numbers.pop(0)

last_sum = float('inf')
current_sum = 0
for i in range(len(numbers)):
	
	current_sum = num_1 + num_2 + num_3

	if (current_sum > last_sum):
		increases = increases + 1

	num_1 = num_2
	num_2 = num_3
	num_3 = numbers[i]
	last_sum = current_sum

# Last number check
current_sum = num_1 + num_2 + num_3
if (current_sum > last_sum):
	increases = increases + 1

# Answer
print(f"answer: {increases}")