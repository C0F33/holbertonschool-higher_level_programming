#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            val1 = my_list_1[i]
            val2 = my_list_2[i]

            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise TypeError("wrong type")

            if val2 == 0:
                raise ZeroDivisionError("division by 0")

            result_list.append(val1 / val2)

        except TypeError as e:
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError as e:
            print("division by 0")
            result_list.append(0)
        except IndexError as e:
            print("out of range")
            result_list.append(0)
        finally:
            pass

    return result_list
