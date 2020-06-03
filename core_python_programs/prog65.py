# Variable lenght args: It can store zere(0) or more values, it should be last one
#it assign using * example { *x } here *x is var lenght args.
def display(*x):
    for i in range(len(x)):
        print(x[i])
display(10)
display(10,20)
display(10,20,30,20,50,40)
