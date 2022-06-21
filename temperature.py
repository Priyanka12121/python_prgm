#wap in python to prove that at -40 both,centigrade and fahrenheit shows the same temperature.you need to write compare() and main() function.Compare() will return true/false based on the comparision result.
def compare(c):
    f=(c*9/5)+32
    if c==f:
        return 1
    else:
        return 0
def main():
    c=float(input("enter the temperature in celsius"))
    r=bool(compare(c))
    print("Result is",r)
if __name__=='__main__':
    main()
