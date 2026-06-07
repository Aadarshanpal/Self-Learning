import matplotlib.pyplot as plt
def visualization(iteration,guess,num_to_guess):
    plt.plot(iteration,guess,marker = 'o')
    plt.xlabel("iteration")
    plt.ylabel("guess")
    plt.axhline(y = num_to_guess)
    plt.grid(False)

    plt.show()