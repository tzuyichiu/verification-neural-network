# Abstract interpretation-based verification of neural networks

This is a project done in Ecole Polytechnique, proposed in the course INF575: 
Safe Intelligent Systems. This project is done in collaboration with my 
classmate, Biswajeet Kar. The goal is to verify neural networks by using case 
disjunctions and junctions for ReLU activation function in order to refine
output results.

## Overview

Since neural network activation functions are non-linear, it becomes more 
complicated to prove a property related to the output results. **[3]** 
proposes an abstraction using Zonotope transformers applied to neural network 
activation functions, while **[4]** proposes an improvement combining MILP 
(Mixed Integer Linear Programming) and LP (Linear Programming). It is thus 
crucial to refine the upper and lower bounds of output results, as shown in the 
example provided by **[4]** in **Figure1.png**. 

In the context of this project, we only work on the ReLU function as our target 
function that we would like to abstract. Each time we approximate ReLU by a 
linear function using an abstract Zonotope transformer, the output generates a 
noise symbol and loses precision at every hidden layer. In the previous work 
proposed by **[3]** and **[4]**, these noise symbols were ranged in `[−1, 1]`, 
which could have been constrained by making use of conditional statements, as 
suggested in **[2]**:
```
ReLU(x) = max(x, 0) = x if x ≥ 0 ; 0 otherwise
```

In our approach, we propose to create case disjunctions whenever we encounter a 
ReLU function for which the input variable can range from negative values to 
positive values. Indeed, the number of cases at the output layer can increase 
exponentially with the number of layers, but the precision is exact in every 
single case, and every output will only depend on the intial input values.

Though a lot of cases may be computed, some expressions of final output values 
can be considered "closed enough" to be joined, by simply abstracting the minor 
different parts, in order to obtain only one expression at the end. The number 
of cases can thus be reduced when propogating inside the neural network, 
without losing too much precision. Especially, we will show that the 
constraints used for case disjunctions may lead to a refinement of the 
abstraction we apply for the junctions.

We show how the junctions and disjunctions are concretely computed, with the 
example provided by **[4]** in **Figure1.png**, step by step. In **[4]**, the 
authors were able to prove that `x_13` is always greater than `x_14` by 
refining the bounds while using an abstract Zonotope transformer. In our 
abstraction using disjunctions and junctions, the bounds computed for the 
output variables will be the same as those computed in the paper. We can 
actually prove that they are the optimal ones.

## Implementation

We implemented a simple "empirical verifier", which tests the network by 
inputing random values in a particular range, and visualize the bounds of 
output values. This empirical method can, after a sufficient number of tests, 
produce the distribution of output values between the theoretical lower and 
upper bounds in order to validate the bounds we have computed with our 
abstraction. The file **test_results.csv** is generated with output values with
random input values.

## Further details

Please refer to **Subject.pdf** as an initial guide, and **Report.pdf** for 
the details of our work, including computation details and illustrations.

## References

[1] T. Gehr, M. Mirman, D. Drachsler-Cohen, P. Tsankov, S. Chaudhuri, and M. 
Vechev. Ai2: Safety and robustness certification of neural networks with 
abstract interpretation. In 
*2018 IEEE Symposium on Security and Privacy (SP), 2018*.

[2] Khalil Ghorbal, Eric Goubault, and Sylvie Putot. A logical product approach 
to zonotope intersection. In 
*Proceedings of the 22Nd International Conference on Computer Aided Verification, CAV’10, 2010*.

[3] Gagandeep Singh, Timon Gehr, Matthew Mirman, Markus Puschel, and Martin
Vechev. Fast and effective robustness certification. In 
*Advances in Neural Information Processing Systems 31. 2018*.

[4] Gagandeep Singh, Timon Gehr, Markus Puschel, and Martin Vechev. Boosting 
robustness certification of neural networks. In 
*International Conference on Learning Representations*. 
URL: https://files.sri.inf.ethz.ch/website/papers/RefineZono.pdf.