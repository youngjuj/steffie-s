
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작!')
#         func(input_text)
#         print('함수 끝!')
#
#     return decorated
#
# @decorator
# def hello_world(input_text):
#     print(input_text)


# hello_world('Hello World!')


def decorator(func):
    def decorated(width, height):
        if width and height > 0:
            return func(width, height)
        else:
            raise ValueError('양수를 입력하세요')
    return decorated


@decorator
def cal_tri(width, height):
    return(width * height / 2)

@decorator
def cal_sq(width, height):
    return(width * height)

cal_tri(2,3)


# class User:
#     def __init__(self, *args, **kwargs):
#         self.user
#
#
#
#
# def check_integer(func)