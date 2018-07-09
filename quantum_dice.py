# N-sided quantum die

from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce 
import math

qvm = QVMConnection()

n = float(input('N: '))
sides = math.ceil(math.log(n, 2))

gates = []
for i in range (0, sides):
	gates.append(H(i))
dice = Program (gates)

roll_dice = dice.measure_all()

dice_value = n + 1
while dice_value > n:
	result = qvm.run(roll_dice)
	dice_value = reduce(lambda x, y: 2*x + y, result[0], 0) + 1

print ("Quantum roll:", dice_value)

'''
# Testing to see if truly N-sided die
num_dict = {}
for i in range (0, 10000):
	# print ("Attempt #", i)
	dice_value = n + 1
	while dice_value > n:
		result = qvm.run(roll_dice)
		dice_value = reduce(lambda x, y: 2*x + y, result[0], 0) + 1

	if dice_value in num_dict:
		num_dict[dice_value] += 1
	else:
		num_dict[dice_value] = 1

print (num_dict)

# Frequency of each roll is roughly equal across 1 through N
'''
