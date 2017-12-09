import sys

def compute_average(numbers):
    if not numbers:
        return 0
    sum = 0
    for number in numbers:
        sum += number
    return sum/len(numbers)    

def main():
    list = []
    for argv in sys.argv[1:]:
        list.append(int(argv))
    print("Average :" +   
         str(compute_average(list)))

if __name__ == "__main__":
    main()
