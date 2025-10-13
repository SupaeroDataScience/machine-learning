import matplotlib.image as mpimg
import matplotlib.animation as animation
from IPython.display import HTML

#to choose the infill criterion (EI, SBO or LCB)
IC = 'EI'

plt.ioff()
x_data = np.atleast_2d([0,7,25]).T
ndoe= np.shape(x_data)[0]
print("Ndoe init", ndoe)
y_data = fun(x_data)


sm = KRG(theta0=[1e-2],print_global = False)

for k in range(n_iter):
    x_start = np.atleast_2d(np.random.rand(20)*25).T
    f_min_k = np.min(y_data)
    sm.set_training_values(x_data,y_data)
    sm.train()
    
    if IC == 'EI':
        obj_k = lambda x: -EI(sm,np.atleast_2d(x),f_min_k) #EI to maximize
    elif IC =='SBO':
        obj_k = lambda x: SBO(sm,np.atleast_2d(x)) #SBO to minimize
    elif IC == 'LCB':
        obj_k = lambda x: LCB(sm,np.atleast_2d(x))  #LCB to minimize
    
    opt_all = np.array([minimize(lambda x: float(obj_k(x)), x_st, method='SLSQP', bounds=[(0,25)]) for x_st in x_start])

    opt_success = opt_all[[opt_i['success'] for opt_i in opt_all]]
    obj_success = np.array([opt_i['fun'] for opt_i in opt_success])
    ind_min = np.argmin(obj_success)
    opt = opt_success[ind_min]
    x_et_k = opt['x']
    
    y_et_k = fun(x_et_k)
    
    
    y_data = np.atleast_2d(np.append(y_data,y_et_k)).T
    x_data = np.atleast_2d(np.append(x_data,x_et_k)).T
    
    print(x_data[k+ndoe],y_data[k+ndoe,0])
    Y_GP_plot_mean = sm.predict_values(X_plot)
    Y_GP_plot_var = sm.predict_variances(X_plot) 
    Y_EI_plot = obj_k(X_plot)

    fig = plt.figure(figsize=[10,10])
    ax = fig.add_subplot(111)
    if  IC == 'SBO':
        ei, = ax.plot(X_plot,Y_EI_plot,color='red')
    else:    
        ax1 = ax.twinx()
        ei, = ax1.plot(X_plot,Y_EI_plot,color='red')
    true_fun, = ax.plot(X_plot,Y_plot)
    data, = ax.plot(x_data[0:k+ndoe],y_data[0:k+ndoe,0],linestyle='',marker='o',color='orange')
    opt, = ax.plot(x_data[k+ndoe],y_data[k+ndoe,0],linestyle='',marker='*',color='r')
    gp, = ax.plot(X_plot,Y_GP_plot_mean,linestyle='--',color='g') 
    un_gp  = ax.fill_between(X_plot.T[0], np.ravel(Y_GP_plot_mean-3*np.sqrt(Y_GP_plot_var)), np.ravel(Y_GP_plot_mean+3*np.sqrt(Y_GP_plot_var)),alpha=0.3,color='g')
    lines = [true_fun,data,gp,un_gp,opt,ei]
    ax.set_title('$x \sin{x}$ function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(lines,['True function','Data','SM prediction','99 % confidence','Next point to Evaluate','Infill Criteria'])
    plt.savefig('Optimization%d' %k)
    plt.close(fig)
    k=k+1
    ind_best_current = np.argmin(y_data)
    y_opt_current = y_data[ind_best_current]
    
ind_best = np.argmin(y_data)
x_opt = x_data[ind_best]
y_opt = y_data[ind_best]

print('Results : X = %s, Y = %s' %(x_opt,y_opt))
print('obtained in :',k,' iterations')
print('Xopt test 1D ', x_opt, 'with Yopt value=', y_opt, ' obtained using EGO criterion = ', IC )
print('Check if the optimal point is closed to the reference solution Xopt= (array([0.75724809]), array([-6.020740])')
print('---------------------------')

fig = plt.figure(figsize=[10,10])

ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

ims = []
for i in range(k):
    image_pt = mpimg.imread('Optimization%d.png' %i)
    im = plt.imshow(image_pt)
    ims.append([im])
    
ani = animation.ArtistAnimation(fig, ims,interval=500)
HTML(ani.to_jshtml())