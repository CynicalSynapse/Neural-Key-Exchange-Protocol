# This file contains the Tree Parity Machine class, which is a key part of NKEP
# It has a certain number of inputs, hidden nodes, and exactly 1 output node.
# 
import copy
import random

def big_theta(a, b):
	if(a==b):
		return 1
	else:
		return 0

class TPM:


	def __init__(self, input_num, hidden_node_num, weight_range):
		self.input_num = input_num
		self.weight_range = weight_range
		self.hidden_node_num = hidden_node_num
		random.seed()
		self.weights = []
		self.step2_arr = []
		for x in xrange(input_num):  #Creates initial weights for the TPM randomly.
			self.weights.append(random.randint(-weight_range, weight_range))

	def fullcopy (self,new):
		
		new.input_num = self.input_num
		new.weight_range = self.weight_range
		new.hidden_node_num = self.hidden_node_num
		new.weights = []
		new.step2_arr = []

		for x in range(new.input_num):
			test = self.weights[x]
			new.weights.append(test)
		for y in range(new.hidden_node_num):
			test = self.step2_arr[y]
			new.step2_arr.append(y)

	#Calculates the output of the TPM on a given input vector
	def output(self, input_arr):
		self.step2_arr = []
		step_sum = 0
		counter = 0
		result = 1
		for x in xrange(len(input_arr)):
			step_sum+=input_arr[x] * self.weights[x]
			if x % (self.input_num/self.hidden_node_num) != 0:
				if step_sum > 0:
					self.step2_arr.append(1)
				elif step_sum == 0:
					self.step2_arr.append(0)
				else:
					self.step2_arr.append(-1)
				step_sum = 0


		for y in self.step2_arr:
			#print "step2_arr value is ", y
			result *= y

		if result == 0:
			result = -1

		#print result, "result"
		return result

	def hebbian_learning_rule(self, inputs, out1, out2):
		for x in xrange(self.input_num):
			self.weights[x] += self.step2_arr[x/self.hidden_node_num]*inputs[x]*big_theta(self.step2_arr[x/self.hidden_node_num], out1)*big_theta(out1, out2)

			if self.weights[x] > self.weight_range:
				self.weights[x] = self.weight_range

			if self.weights[x] < -self.weight_range:
				self.weights[x] = -self.weight_range

	def anti_hebbian_learning_rule(self, inputs, out1, out2):
		for x in xrange(self.input_num):
			self.weights[x] -= self.step2_arr[x/self.hidden_node_num]*inputs[x]*big_theta(self.step2_arr[x/self.hidden_node_num], out1)*big_theta(out1, out2)

			if self.weights[x] > self.weight_range:
				self.weights[x] = self.weight_range

			if self.weights[x] < -self.weight_range:
				self.weights[x] = -self.weight_range

	def random_walk(self, inputs, out1, out2):
		for x in xrange(self.input_num):
			self.weights[x] += inputs[x]*big_theta(self.step2_arr[x/self.hidden_node_num], out1)*big_theta(out1, out2)

			if self.weights[x] > self.weight_range:
				self.weights[x] = self.weight_range

			if self.weights[x] < -self.weight_range:
				self.weights[x] = -self.weight_range

		
	

	def print_weights(self):
		for x in self.weights: 
			print x




