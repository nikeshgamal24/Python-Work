#program to reverse a string using function

def reverse_string(local_string: str)-> str:
    result_string = ''
    for ind in range(len(local_string)-1,-1,-1):
    
        # print(f'index: {ind} value: {local_string[ind]}')
        # print(f'old-result: {result_string}')

        result_string = result_string +  local_string[ind]

        # print(f'new-result:{result_string}')
    
    return result_string

input_string = input("Enter the desirable string: ")

# #ouput--> hahsinim

result = reverse_string(input_string)
print('Outside of function')
print(input_string)
print('The reverse of the string is:')
print(result)