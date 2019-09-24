
# for i in range(1,11,1):
#     print(i)


def __one_to_ten_h(param1):
    if( param1 > 10):
        return
    print(param1)
    __one_to_ten_h(param1 + 1)

def one_to_ten():
    __one_to_ten_h(1)


one_to_ten()
