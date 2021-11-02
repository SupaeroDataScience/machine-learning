# Decision trees

* [Home](https://supaerodatascience.github.io/machine-learning/)
* [Github repository](https://github.com/SupaeroDataScience/machine-learning/)

This class introduces the concept of **decision trees** as supervized learning methods for classification and regression.
A decision tree is a simple model that can even be visualized and understood by a human after training.
It consists in a graph with a "tree" structure, meaning that there exists a root node with a pair of child nodes, themself having pairs of child nodes, etc., until some leaf nodes.
The way data are processed by the model is by flowing through the nodes until reaching a leaf, that corresponds to a class or a value.
At each node, a "split" was created at training time, testing some features of the data point.
The binary outcome of the test determines whether the next node seen by the data will be the first or the second child of the current node.

[Notebook](https://github.com/SupaeroDataScience/machine-learning/blob/main/8%20-%20Decision%20trees/Decision%20Trees.ipynb)

## References

[Scikit-learn documentation on decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)

[Wikipedia on decision tree learning](https://en.wikipedia.org/wiki/Decision_tree_learning)

[T. Hastie, R. Tibshirani and J. Friedman. Elements of Statistical Learning, Springer, 2009.](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
