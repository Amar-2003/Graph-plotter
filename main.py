import matplotlib.pyplot as plt

n = float(input("Enter n for the function y = mx^n:"))
m = float(input("Enter m:"))
i = -100.1
arrx = []
arry = []
while(i < 100):
    arrx.append(i)
    arry.append((pow(i,n))*m)
    i += 1
plt.plot(arrx,arry)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title("Graph for your function")
plt.show()
