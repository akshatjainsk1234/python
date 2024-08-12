def remove_odd_numbers(number_list):
    even_numbers = [num for num in number_list if num % 2 == 0]
    return even_numbers

user_input = input("Enter numbers separated by spaces: ")

number_list = list(map(int, user_input.split()))

result = remove_odd_numbers(number_list)

print(f"List after removing odd numbers: {result}")
