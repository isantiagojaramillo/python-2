temparature = float(input("Enter temperature "));

scale = input("Farenheit(F) OR Celsius(C)? ").lower();

if scale == "f":
    celsius = (temparature - 32) * 5/9;
    print(celsius);
elif scale == "c":
    farenheit = (temparature * 1.8) + 32
else:
    print("Wrong scale");
