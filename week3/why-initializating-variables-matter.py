# In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?

# def count_down(start_number):
#     while (current > 0):
#         print(current)
#         current -= 1
#     print("Zero!")
#
# count_down(3)

def count_down(start_number):
      while (start_number > 0):
        print(start_number)
        start_number -= 1
      print("Zero!")
    
count_down(3)
