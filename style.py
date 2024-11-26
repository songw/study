# class Duck:
#     """鸭子类

#     :param color: 鸭子颜色
#     """

#     def __init__(self, color):
#         self.color = color


import re


def find_number(input_string):
    """找到字符串里的第一个整数"""
    matched_obj = re.search(r'\d+', input_string)
    if matched_obj:
        return int(matched_obj.group())
    return None
