li = [lambda: x for x in range(10)]
li2 = [lambda x=x: x for x in range(10)]

if __name__ == "__main__":
    print("li列表的第一个值，li[0]为：", li[0]())  # 9
    print("li列表的第一个值，li2[0]为：", li2[0]())  # 0
    '''
    难以置信，为什么第一个值是9，不应该是0吗，
    由于延时求值的特性，表达式的求值不在被绑定到变量之后就立刻求值，而是在该值被使用的时候才求值，
    当调用li[0]()的时候，函数中x的值已经为9了，所以输出9
    可以看li列表的打印结果
    [<function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>,
    <function __main__.<listcomp>.<lambda>()>]
    解决方式：
    采用变量传值的方式，即添加默认的参数，如li2
    在li2中每次都记录的x的值
    '''
