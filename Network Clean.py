
# Standard lib
import random
import csv
import copy

# External lib
import numpy as np


class Network:

    def __init__(self, sizes):
        """
        This function creates the neural network. Sizes is a list that contains the input of how many nodes there is on
        each layer of the network.
        """
        self.sizes = sizes
        self.layers = len(sizes)
        self.biases = [np.random.randn(x, 1) for x in sizes[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(sizes[1:], sizes[:-1])]


    def feedForward(self, a_data,write = True):
        """
        This feeds the A_data through the neural network.
        """
        # This converts it to an np array so we are able to use np matrix mul
        self.a_data = []
        self.nodes = []
        self.zs = []
        self.a_data = np.matrix(a_data).transpose
        self.nodes.append(self.a_data)
        for x in range(self.layers - 1):
            self.zs.append(self.weights[x]*self.nodes[x]) + self.biases[x])
            self.nodes.append(self.zs[x])

    def back_prop(self, x, y):
        self.feedForward(x,False)
        y_tran = np.matrix(y).transpose()
        delta = np.multiply(cost_prime(self, y_tran), sigmoid_prime(self.zs[-1]))
        biases_copy = copy.deepcopy(self.biases)
        weights_copy = copy.deepcopy(self.weights)
        biases_copy[-1] = delta
        nodes_2 = np.matrix(self.nodes[-2])
        weights_copy[-1] = np.dot(delta, nodes_2.transpose())
        for back in range(1, self.layers - 1):
            weight = np.matrix(self.weights[-back])
            delta = np.multiply(np.dot(weight, delta), sigmoid_prime(self.zs[-back-1]))
            biases_copy[-back] = delta
            nodes = np.matrix(self.nodes[-back-1])
            weights_copy[-back] = np.dot(delta, nodes.transpose())

        return biases_copy, weights_copy


def sigmoid(x):
    """
    Sigmoid function for a matrix applied to every element.
    """
    x = np.matrix(x)
    return 1 / (1 + np.exp(-x))

def sigmoid_prime(x):
    """
    Sigmoid prime function for a matrix applied to every element.
    """
    x = np.matrix(x)
    out = np.multiply(sigmoid(x),(1-sigmoid(x)))
    return out

def costFunction(network, correct_data):
    """
    Works for out the cost function
    """
    return np.sum(np.square(np.subtract(network.nodes[network.layers - 1], correct_data)))

def cost_prime(self, y):
    return np.subtract(self.nodes[-1], y)

A = Network([1,6,1])
A.feedForward([.1])
print(A.nodes[-1])
A.feedForward([.5])
print(A.nodes[-1])
A.feedForward([0.0001])
print(A.nodes[-1])
A.feedForward([1000])
print(A.nodes[-1])



