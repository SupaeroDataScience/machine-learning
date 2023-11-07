### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

def EI(GP,points,f_min):
    pred_mu = GP.predict_values(points)
    var = GP.predict_variances(points)
    pred_sig = np.sqrt(var)
    args0 = (f_min - pred_mu)/np.atleast_2d(pred_sig)
    args1 = (f_min - pred_mu)*norm.cdf(args0)
    args2 = np.atleast_2d(pred_sig)*norm.pdf(args0)
    ei = args1 + args2
    return ei