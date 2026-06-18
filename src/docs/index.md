# Supervised and Unsupervised Machine Learning
This is the Supervised and Unsupervised Learning section of the [Algorithms in Machine Learning](https://supaerodatascience.github.io/syllabus.html#fsd311) class at ISAE-Supaero. The Neural Networks and Deep Learning topics have a [class of their own](https://supaerodatascience.github.io/deep-learning/) and won't be covered here.

* [Home](https://supaerodatascience.github.io/machine-learning/)
* [Github repository](https://github.com/SupaeroDataScience/machine-learning/)

## Syllabus and schedule

This course offers a discovery of the landscape of Machine Learning through some key algorithms.  
It will be followed by the [Neural Networks and Deep Learning part](https://supaerodatascience.github.io/deep-learning/) and the  [Reinforcement Learning part](https://supaerodatascience.github.io/reinforcement-learning/) .

Over 25 hours, we will cover the landscape of Supervised and Unsupervised Machine Learning by taking three different points of view and formalisms: the geometrical perspective, the probabilistic (Bayesian) perspective, and the ensemble perspective.  
The class is organized in 8 sessions:  

Schedule | | |
| --- | --- | --- |
21/09 PM | [Introduction to Machine Learning](index.md/#introduction-to-machine-learning) | Supervised and unsupervised learning, data preprocessing and ML workflow |
22/09 AM | [Geometrical approach](geometric.md) | Support Vector Machines, the bias/variance tradeoff and a bit of kernel theory.|
29/09 AM | [Probabilistic approach, pt 1](probabilistic.md) | Naive Bayes classification and Gaussian Processes  |
29/09 PM | [Probabilistic approach, pt 2](probabilistic.md#surrogate-modeling-and-bayesian-optimization) | Surrogate Modeling and Bayesian Optimization |
30/09 AM | [Committee learning, pt 1](commitee.md) | Decision Trees and Boosting |
06/10 AM | [Committee learning, pt 2](commitee.md#bagging) | Bagging, Random Forests|
06/10 PM | [Committee learning, pt 3](commitee.md#anomaly-detection) | Anomaly Detection |
07/10 AM | [Explainability](xai.md) | LIME, SHAP|

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

## Bibliography

**The Elements of Statistical Learning.**  
T. Hastie, R. Tibshirani, J. Friedman.  
Springer Series in Statistics.  
[https://web.stanford.edu/~hastie/ElemStatLearn/](https://web.stanford.edu/~hastie/ElemStatLearn/)  




## Introduction to Machine Learning

[Slides](https://github.com/SupaeroDataScience/machine-learning/blob/main/0%20-%20Introduction/pres.pdf)

## A quick tour of Unsupervised Learning
--8<--
docs/unsup.md
--8<--


## The importance of data pre-processing
--8<--
docs/preproc.md
--8<--

