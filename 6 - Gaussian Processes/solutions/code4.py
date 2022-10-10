# %load solutions/code4.py
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).
def kernel(x1,x2,sigma_kernel,l,sigma_noise):
    ### WRITE YOUR CODE HERE
    k = sigma_kernel * sigma_kernel * np.exp(-(x1-x2)**2 / (2*l*l)) 
    return k + sigma_noise*(x1==x2)