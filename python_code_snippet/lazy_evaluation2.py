vals = [x for x in range(10,80,10)]  # [10, 20, 30, 40, 50, 60, 70]

def make_funcs(num):
    for i in range(num):
        yield lambda x,i=i: x*vals[i]   # 注意此处同样是要使用变量接受i的值，否则后续调用的时候手动添加i参数

if __name__ == "__main__":
    functions = make_funcs(7)

    l = list(functions)
    for func in l:
        print(func(4))

    '''
    40
    80
    120
    160
    200
    240
    280
    '''


