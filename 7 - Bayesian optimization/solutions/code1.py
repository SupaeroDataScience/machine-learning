### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def myGPpredict(x_new, x_data, y_data, K_inv, ls, sig):
    K_et = cov_vect(x_new,x_data,ls,sig)
    mu = K_et.dot(K_inv.dot(y_data))[0]
    k_xx = cov_function(x_new,x_new,ls,sig)
    sigma2 = k_xx - K_et.dot(K_inv.dot(K_et.T)) #sigma * sigma
    sigma = np.sqrt(sigma2)
    return mu,sigma
