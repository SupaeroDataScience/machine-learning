### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).



#define the KRG object, give the DOE and train it
gpr = KRG()# some options to add theta0=[1e-2]*x_data.shape[1],print_prediction = False)
gpr.set_training_values(x_data,y_data)

gpr.train()

print('--------------')
print('Theta optimal', gpr.optimal_theta)