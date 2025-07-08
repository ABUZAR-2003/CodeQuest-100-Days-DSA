num = input("Enter numbers: ")
input_line = list(map(int, num.strip().split()))

unique_numbers = list(set(input_line))

unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[1]
    print("Second Largest Number:", second_largest)
else:
    print("Not enough unique numbers to find the second largest.")