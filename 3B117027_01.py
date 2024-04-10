class test2_1:

    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_even_squares(num_list):                 #取偶數做平方後輸出
        x = []
        for i in range(len(num_list)):
            if int(num_list[i] % 2 ==0):
                num_list[i]*=num_list[i]
                x.append(int(num_list[i]))
        return x
    result = (get_even_squares(num_list))


    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_odd_cubes(num_list):                    #取奇數做立方後輸出
        y = []
        l = 0
        while l < len(num_list):
            if (num_list[l]%2 == 1):
                    num_list[l]= num_list[l]**3
                    y.append(int(num_list[l]))
            l+=1
        return y
    result_2 = (get_odd_cubes(num_list))


    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_sliced_list(num_list):                  #list中最後五個值用切片返回並輸出
        c = num_list[4:]
        return c

    result_3 = get_sliced_list(num_list)

    def format_numbers(numbers):
        f = []
        for num in numbers:
            formatted_num = '{:>8}'.format(num)  # 將數字格式化為 8 個字元的寬度然後靠右對齊  ex: '{:<8}'為寬度8向左對齊, 置中'{:^8}' .format格式化字串的函式
            f.append(formatted_num)
        return f

    to1 = format_numbers(result)
    print(' ,'.join(to1))

    to2 = format_numbers(result_2)
    print(' ,'.join(to2))

    to3 = format_numbers(result_3)
    print(' ,'.join(to3))


