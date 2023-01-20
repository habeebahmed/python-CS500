import random
import copy     # deep_copy()

scores = [2, 4, 2, 6, 7, 8, 10, 2]
print('Original scores =', scores)

# demonstrate the count()
print('scores.count(2) =', scores.count(2))
print('scores.count(5) =', scores.count(5))

# demonstrate the reverse()
scores.reverse()
print('Reversed scores = ', scores)

# demonstrate the sort()
scores.sort()
print('Sorted scores = ', scores)

# demonstrate the sort(key)
fruits = ['Orange', 'pear', 'Apple', 'banana', 'Watermelon']
fruits.sort()
print('fruits.sort() = ', fruits)
fruits.sort(key=str.lower)
print('fruits.sort(key=str.lower) = ', fruits)

# demonstrate the sorted(list)
numbers = [6, 5, 3, 2, 7, 1]
numbers2 = sorted(numbers)
print('numbers =', numbers)
print('mumbers2 =', numbers2)

# demonstrate the min(), max(), choice(), shuffle()
print('min(numbers) =', min(numbers))
print('max(numbers) =', max(numbers))
print('random.choice(numbers) =', random.choice(numbers))
random.shuffle(numbers)
print('random.shuffle(numbers) =', numbers)

# demonstrate the deep_copy
num = [6, 5, 3, 2, 7, 1]
num_copy = copy.deepcopy(num)
print('num =', num) 
print('num_copy =', num_copy)
num_copy.sort()
print('num_copy.sort() =', num_copy)
print('num =', num) 
