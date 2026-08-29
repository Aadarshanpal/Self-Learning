from numbers import send_word_ones, send_word_tens
def logic(num):
    if 0 <= num <= 19:
        return ones(num) 
    if 20 <= num <= 99:
        return tens(num)
    if 100 <= num <= 999:
        return hundreds(num)
    if 1000 <= num <= 999999:
        return thousands(num)
    if 1000000 <= num <= 999999999:
        return millions(num)
    if 1000000000 <= num < 1000000000000:
        return billion(num)

def ones(num):
    return send_word_ones(num)

def tens(num):
    return send_word_tens(num//10) + " " + ones(num%10)
    
def hundreds(num):
    return logic(num // 100) + " hundred " + (tens(num%100) if num%100 >= 10 else ones(num%100))

def thousands(num):
    return logic(num//1000) + " thousand " + logic(num % 1000)

def millions(num):
    return logic(num//1000000) + " million " + logic(num % 1000000)

def billion(num):
    return logic(num//1000000000) + " Billion " + logic(num%1000000000)
