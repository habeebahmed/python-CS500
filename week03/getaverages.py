#!/usr/bin/env python3
# getaverages.py

def get_average_while(list):
	sum = 0
	i = 0
	while i < len(list):
		sum += list[i]
		i += 1
	return sum
	
def get_average_for(list):
	sum = 0
	i = 0
	for item in list:
		sum += item
	return sum
	
def main():
	scores = [10, 7, 8, 9, 6]
	print("get_average_while(scores) = ", get_average_while(scores))
	print("get_average_for(scores) = ", get_average_for(scores))
	
	
if __name__ == "__main__":
	main()