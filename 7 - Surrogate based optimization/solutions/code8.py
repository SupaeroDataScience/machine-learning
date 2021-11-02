### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

#define the constraint function g
def g(x):
    y= -np.atleast_2d(x-11)
    return y