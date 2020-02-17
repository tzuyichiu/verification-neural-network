import random
import numpy as np
import csv

nn_architecture = [{"input_dim": 2, "output_dim": 2, "activation": "relu", "b": np.array([[0],[0]], np.float64), "w": np.array([[1,1], [1, -1]], np.float64)},
                   {"input_dim": 2, "output_dim": 2, "activation": "relu", "b": np.array([[1],[ -1]], np.float64), "w": np.array([[1,-1], [1, -1]], np.float64)},
                   {"input_dim": 2, "output_dim": 2, "activation": "relu", "b": np.array([[1.25],[ 1]], np.float64), "w": np.array([[2,1], [1, -1]], np.float64)}
                  ]
#Initiate the network with input, weight and noise values
def init_layers(nn_architecture, seed = 99):
    np.random.seed(seed)
    number_of_layers = len(nn_architecture)
    params_values = {}
    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]

        params_values['W' + str(layer_idx)] = layer["w"]
        params_values['b' + str(layer_idx)] = layer["b"]

    return params_values

# The relu function
def relu(Z):
    return np.maximum(0,Z)


# The propagation function
def single_step(A_prev, W_curr, b_curr, activation="relu"):
    Z_curr = np.dot(W_curr, A_prev) + b_curr

    if activation is "relu":
        activation_func = relu
    else:
        raise Exception('Non-supported activation function')

    return activation_func(Z_curr), Z_curr


#Run funcion to run the whole process
def run_simulation(X, params_values, nn_architecture):
    memory = {}
    A_curr = X

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        A_prev = A_curr

        activ_function_curr = layer["activation"]
        W_curr = params_values["W" + str(layer_idx)]
        b_curr = params_values["b" + str(layer_idx)]
        A_curr, Z_curr = single_step(A_prev, W_curr, b_curr, activ_function_curr)                                                                                
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr

    return A_curr, memory

# The main function
def main():
    X = np.array([[random.uniform(0, 1)],[random.uniform(0, 1)]], np.float64)
    #X = np.array([[1],[0]], np.float64)
    #X = np.array([[1],[0]], np.float64)
    #print("Random Input Value between Interval [0, 1]: \n")
    #print(X)
    #print("\n")
    params_values = init_layers(nn_architecture)
    with open('test_results.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['x1', 'x2', 'x13', 'x14'])
            for i in range(1000):
                X = np.array([[random.uniform(0, 1)],[random.uniform(0, 1)]], np.float64)
                #print("Random Input Value between Interval [0, 1]: \n")
                #print(X)
                #print("\n")
                A_curr, memory = run_simulation(X, params_values, nn_architecture)
                #print("Output Value of the final layer: \n")
                #print(A_curr)
                writer.writerow([X[0][0], X[1][0], A_curr[0][0], A_curr[1][0]])

if __name__ == '__main__':
    main()
