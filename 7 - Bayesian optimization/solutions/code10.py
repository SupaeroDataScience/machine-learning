# %load solutions/code10.py
### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

for k in range(n_iter):
    x_start = sampling(20)
    f_min_k = np.min(y_data)
    gpr.set_training_values(x_data, y_data)
    gpr.train()
    #obj_k = lambda x: -EI(gpr,np.atleast_2d(x),f_min_k)
    obj_k = lambda x: -EI(gpr,np.atleast_2d(x),f_min_k)[:,0]
    #print('obj_k(x_start)[:,0]=',obj_k(x_start)[:,0])

    ## UNCOMMENT ONE OF THE INFILL CRITERIA
    # obj_k = lambda x: -EI(gpr,np.atleast_2d(x),f_min_k)
    # obj_k = lambda x: SBO(gpr,np.atleast_2d(x))
    # obj_k = lambda x: UCB(gpr,np.atleast_2d(x))

    opt_all = np.array([minimize(obj_k, x_st, method='SLSQP', bounds=[(-2,2)]) for x_st in x_start])
    opt_success = opt_all[[opt_i['success'] for opt_i in opt_all]]
    obj_success = np.array([opt_i['fun'] for opt_i in opt_success])
    ind_min = np.argmin(obj_success)
    opt = opt_success[ind_min]
    x_et_k = opt['x']

    y_et_k = rosenbrock(np.atleast_2d(x_et_k))
    #print('At iteration ' + str(k) + ', new point with x values ' + str(x_et_k) +' and  value  ' + str(y_et_k)+' is added ')

    y_data = np.append(y_data,y_et_k)
    x_data = np.append(x_data,np.atleast_2d(x_et_k),axis=0)#np.atleast_2d(np.append(x_data,x_et_k))

ind_best = np.argmin(y_data)
x_opt = x_data[ind_best]
y_opt = y_data[ind_best]
print('With given '+str(n_iter)+' budget, optimal point  is found in ' + str(x_opt) +' with the value ' + str(y_opt))