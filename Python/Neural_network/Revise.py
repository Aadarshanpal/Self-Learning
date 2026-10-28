
x = 3
y = 16

w = 3
b =2

learning_rate = 0.01

def prediction(w,x,b):
    return w*x + b

def gradiant_w(x,y,y_bar):
    return -(2*x*(y-y_bar))

def gradiant_b(y,y_bar):
    return -(2*(y-y_bar))

def learn(param,grad,learning_rate):
    return param - learning_rate * grad

def main(w,x,b,y,learning_rate):
    iteration = 0
    while True:
        y_bar = prediction(w,x,b)
        if ((y-y_bar) / y_bar) * 100 < 0.01:
            break
        print("Iteration: ", iteration)
        print("w = ",w,"\nb = ",b)
        print("Prediction = ",y_bar)
        print("Loss = ", (y-y_bar) ** 2)
        grad_w = gradiant_w(x,y,y_bar)
        grad_b = gradiant_b(y,y_bar)
        w = learn(w,grad_w,learning_rate)
        b = learn(b,grad_b,learning_rate)
        iteration += 1
    print("The learning ended at iteration: ",iteration)
    print("w = ",w,"\nb = ", b)
    print("Prediction = ",y_bar)


if __name__ == "__main__":
    main(w,x,b,y,learning_rate)
