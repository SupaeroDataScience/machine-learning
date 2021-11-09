# <a id="sec5"></a> 5. Gradient Boosting

AdaBoost incrementally builds a committee of classifiers (or regressors) where each one tries to compensate the weaknesses of all the previous ones. This description makes it sound a lot like gradient descent.

Let's write $f_k = \{h_0,\ldots,h_k\}$ the committee predictor obtained at step $k$. $f_k$ is a point in $\mathcal{H}$ and our goal is to find the function (the point) in $\mathcal{H}$ that minimizes a certain loss function $L(f), \ f\in\mathcal{H}$. Therefore, $h_{k+1}$ should point in the opposite direction of the gradient of $L$ with respect to functions $f$.

This is precisely the idea of Gradient Boosting, that extends traditionnal Boosting to any differentiable loss function. Let's write this formally.

Suppose we have a loss function $L(f(x),y)$ that quantifies how bad a predictor $f$ is, given the true data pair $(x,y)$. This could be a squared error, a cross-entropy, or any other loss function that compares $f(x)$ to the true $(x,y)$ data.

The goal of a learning algorithm is to find
$$f^* = \arg\min_{f\in\mathcal{H}} \mathbb{E}_{(x,y)\sim p(x,y)} \left( L(f(x),y) \right)$$

To simplify the notation, we will write $\mathbb{E}_{x,y}$ for $\mathbb{E}_{(x,y)\sim p(x,y)}$.

So if we assume an current function $f_{k-1}$, one can perform gradient descent by writing 
$$f_{k} = f_{k-1} + \alpha_{k} h_{k}$$
Where
$$h_{k} = \nabla_f \left[\mathbb{E}_{x,y} \left( L(f_{k-1}(x),y) \right)\right] = \mathbb{E}_{x,y} \left[ \nabla_f L(f_{k-1}(x),y) \right]$$
And $\alpha_{k}$ is found by line search
$$\alpha_{k} = \arg\min_\alpha \left[ \mathbb{E}_{x,y} \left[ L(f_{k-1}(x) + \alpha h_{k}(x),y) \right] \right]$$

Of course, the true value of $\mathbb{E}_{x,y} \left[ \nabla_f L(f_k(x),y) \right]$ is not accessible since it would require an infinite amount of data. But we can still approximate it using the training set:
$$h_{k} = \sum_{i} \nabla_f L(f_{k-1}(x_i),y_i)$$
And similarly
$$\alpha_{k} = \arg\min_\alpha \left[ \sum_{i} L(f_{k-1}(x_i) + \alpha h_{k}(x_i),y) \right]$$

Taking the gradient with respect to $f$ functions in $\mathcal{H}$ is quite an abstract operation, so how do we choose the descent direction in practice? The key remark here is to notice that, for a given function $f$, although $f$ lives in a possibly infinite-dimensional function space, $f(x_i)$ lives in $\mathbb{R}$ and is a descriptor of $f$ (around $x_i$). Thus, the function that would fit the training set $\left\{ \left(x_i, \left[\frac{\partial L(f(x_i), y_i)}{\partial f(x_i)}\right]_{f = f_{k-1}} \right) \right\}$ is an approximate descent direction.

The initial function $f_0$ is chosen to be a constant function, so:
$$f_0 = \arg\min_\gamma \sum_i L(\gamma, y_i)$$

So the algorithm can be written:
<div class="alert alert-success">
$f_0 = \arg\min_\gamma \sum_i L(\gamma, y_i)$<br>
For $k=1$ to $K$
<ul>
<li> Compute the pseudo-residuals
$$r_i = \left[ \frac{\partial L(f(x_i), y)}{\partial f(x_i)} \right]_{f = f_{k-1}}$$
<li> Train $h_k$ to fit the dataset $\left(x_i, r_i\right)$
<li> Find $\alpha_k$ though line search
$$\alpha_{k} = \arg\min_\alpha \left[ \sum_i L\left(f_{k-1}(x_i) + \alpha h_{k}(x_i),y_i\right) \right]$$
<li> Update the model
$$f_k = f_{k-1} + \alpha_k h_k$$
</ul>
Return $f_K$
</div>

AdaBoost is actually a Gradient Boosting procedure.

When $\mathcal{H}$ is the set of regression or classification trees, Gradient Boosting is called **Gradient Tree Boosting**. Several extensions (regularization, local step-sizes, etc.) are possible in that case.

The most well-known Gradient Boosting library is called [XGBoost](https://github.com/dmlc/xgboost). It is efficient and quite flexible. It has be used to win several Data Science competitions. But Scikit-Learn also provides a decent implementation that we will use below.
