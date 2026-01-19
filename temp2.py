principal_amount = float(input("enter the pincipal amount"))
rate_of_intrest = float(input("enter the intrest"))
years = int(input("number of years"))

future_value = principal_amount * (1 + rate_of_intrest / 100) ** years
print("the final future value is "  , future_value)





distance = int(input("Enter the distance(in feet) :"))
inches = distance*12
yard = distance / 3
miles = yard / 1760
print(inches , yard , miles)


def convert_second(seconds):
    hours = seconds//3600
    minutes = (seconds%3600)//60
    second = seconds%60
    return f"{hours::minutes::second}"
seconds = int(input("Enter the time in seconds :"))
convert_second(seconds)


def check(ch ):
    vowels = "aeiouAEIOU"
    if ch.isdigit():
        return "Digit"
    elif ch.isalpha():
        if ch in vowels:
            return "Vowels"
        else:
            return "consonent"
    else:
        return "Special Character"

character = input("enter the character ")
result = check(character)
print(check(result))






