# Interview Practice Problem Homework
# Page 3
import copy
def max_product(num_list):
    copy_num_list = copy.deepcopy(num_list)
    copy_num_list.sort()
    last_three = copy_num_list[-3:]
    return sum(last_three)



if __name__ == '__main__':
    print(max_product([2, 3, 6, 9, 5, 4]))
