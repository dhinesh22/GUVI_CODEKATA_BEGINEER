N=int(input(""))
list=["Hello\n"]
def foo(x):
    print(x*N)
def main(fun,list):
    for item in list:
        fun(item)
main(foo,list)
