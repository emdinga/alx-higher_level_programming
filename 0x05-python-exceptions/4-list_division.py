#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                if divisor != 0:
                    division_result = dividend / divisor
                else:
                    division_result = 0
            else:
                raise TypeError
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (IndexError, TypeError):
            print("out of range" if i >= min(len(my_list_1), len(my_list_2)) else "wrong type")
            division_result = 0
        finally:
            result.append(division_result)
    return (result)
