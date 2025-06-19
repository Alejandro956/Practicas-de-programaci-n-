import matplotlib.pyplot as plt

x= [1, 2, 3, 4, 5]
y= [5, 7, 4, 9, 6]

plt.plot(x,y, color='red', linestyle='-', marker='o')
plt.title("Mi primer grafico")
plt.xlabel("valores en x")
plt.ylabel("valores en y")
plt.grid(True)
plt.show()


