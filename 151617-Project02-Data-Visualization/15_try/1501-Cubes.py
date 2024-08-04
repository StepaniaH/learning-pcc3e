import matplotlib.pyplot as plt

n = input("Enter the number you want to cube to: ")
x_value = range(1, int(n) + 1)
y_value = [x**3 for x in x_value]

fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=5) 

ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Cube of Number", fontsize=14)

ax.tick_params(labelsize=14)
ax.axis([0, int(n) + 1, 0, (int(n) + 1)**3])
ax.ticklabel_format(style='plain')
plt.show()

