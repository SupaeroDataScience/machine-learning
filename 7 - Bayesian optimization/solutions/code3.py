### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def likelihood(x_data, y_data, ls, sig):
    K = cov_matrix(x_data, ls, sig)
    N = x_data.shape[0]

    # -1/2 * Y^T K^{-1} Y
    K_inv_y = np.linalg.solve(K, y_data)       # plus stable que inv(K)
    term1 = 0.5 * y_data.T.dot(K_inv_y)

    # -1/2 * log|K|  (utilise slogdet pour la stabilité)
    sign, logdet = np.linalg.slogdet(K)
    term2 = 0.5 * logdet

    # -N/2 * log(2*pi)
    term3 = 0.5 * N * np.log(2 * np.pi)

    like = (term1 + term2 + term3) #to minimize the negative log-likelihood
    return float(like) if np.isscalar(like) else like[0, 0]
