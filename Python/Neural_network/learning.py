w = 2
x = 3
actual = 12
learn_rate = 0.1
def prediction(w,x,b=0):
    return w*x + b

def loss_derivative(x,actual,prediction):
    error = actual - prediction
    loss_function = -(2*x*(actual - prediction))
    return error, loss_function

def learn(loss_function,w,learn_rate):
    wnew = w - learn_rate * loss_function
    return wnew

def main(w,x,actual,learn_rate):
    count = 0
    while True:
        count += 1
        print(f"Prediction Number {count}\n")
        print("w(initial) = ",w)
        predict = prediction(w,x)
        error, derivative = loss_derivative(x,actual,predict)
        w = learn(derivative,w,learn_rate)
        print("Prediction = ",predict)
        print("Error = ",error)
        print("w(new) = ",w)

        if (abs(error) / abs(actual)) * 100 < 0.1 or count > 1000:
            print("Relative error = ", (abs(error) / abs(actual)) * 100)
            break


    print("Final prediction: ",prediction(w,x))



if __name__ == "__main__":
    main(w,x,actual,learn_rate)
