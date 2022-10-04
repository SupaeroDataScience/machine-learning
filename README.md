# Supervised and Unsupervised Machine Learning
This is the Supervised and Unsupervised Learning section of the [Algorithms in Machine Learning](https://supaerodatascience.github.io/syllabus.html#fsd311) class at ISAE-Supaero. The Neural Networks and Deep Learning topics have a [class of their own](https://supaerodatascience.github.io/deep-learning/) and won't be covered here.

* [Home](https://supaerodatascience.github.io/machine-learning/)
* [Github repository](https://github.com/SupaeroDataScience/machine-learning/)

## Syllabus

This course offers a discovery of the landscape of Machine Learning through some key algorithms.
It follows the [Statistical Foundations of Machine Learning part](https://supaerodatascience.github.io/stat-ml) and will be followed by the [Neural Networks and Deep Learning part](https://supaerodatascience.github.io/deep-learning/).

Over 25 hours, we will cover the landscape of Supervised and Unsupervised Machine Learning by taking four different points of view and formalisms: the geometrical perspective, the probabilistic (Bayesian) perspective, the connectionnist perspective (which we will postpone to the next class on Deep Learning), and the ensemble perspective.
The class is organized in 9 sessions:

- Introduction.
    - Introduction to the landscape and workflow of Machine Learning, a few words on specificities of Unsupervised Learning, the importance of data preprocessing (1 session).
- A geometrical approach to Machine Learning.
    - Support Vector Machines, the bias/variance tradeoff and a bit of kernel theory.
- A Bayesian perspective on Machine Learning.
    - Naive Bayes Classification and Gaussian Processes,
    - followed by an in-depth class on Surrogate Modeling and Bayesian Optimization.
- Committee learning methods.
    - Decision Trees and Boosting,
    - followed by an in-depth class on Gradient Boosting.
    - Bagging and Random Forests,
    - followed by an in-depth class on anomaly detection.
- A "perspectives" final session.
    - Explainability in Machine Learning.

The pedagogy taken mixes voluntarily hands-on practice in Python with theoretical and mathematical understanding of the methods. At the end of the course you will be able to make an informed choice between the main families of ML algorithms, depending on the problem at hand. You will have an understanding of the algorithmic and mathematical properties of each family of methods and you will have a basic practical knowledge of the Scikit-Learn library.

# Pre-requisites
- Basic level in Python (language fundamentals, numpy).
- Basic probability and optimization theory.

You must download and install an Anaconda distribution for the latest version of Python before the course ([https://anaconda.org/](https://anaconda.org/)). Alternatively (to downloading Anaconda), you'll need a working Python installation (latest version) with at least, Numpy, Scipy, Matplotlib and Jupyter installed (for instance through pip commands).<br>
If you have a compatible OS, you can [install Docker](https://docs.docker.com/get-docker/) and Docker compose for ready-to use environments.

Additional required Python packages:
- nltk
- keras (conda install keras)
- tensorflow (conda install tensorflow)
- graphviz (conda install graphviz)

## Bibliography

**The Elements of Statistical Learning.**
T. Hastie, R. Tibshirani, J. Friedman.
Springer Series in Statistics.
[https://web.stanford.edu/~hastie/ElemStatLearn/](https://web.stanford.edu/~hastie/ElemStatLearn/)

