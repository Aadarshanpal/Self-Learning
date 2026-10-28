def predictor(x,w,b):
    return w*x + b

def error(prediction,actual):
    return actual-prediction

prediction = predictor(x = 3, w =2, b = 4)

print("prediction=",prediction)


print("Error =", error(prediction,actual=25))



