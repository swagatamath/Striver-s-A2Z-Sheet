def count_digits(num):
    # support negatives and zero
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

def main():
    try:
        num = int(input("Enter a number you want to count digits of: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    print("Number of digits:", count_digits(num))

if __name__ == "__main__":
    main()
