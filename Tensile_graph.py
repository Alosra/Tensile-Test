import pandas as pd
import matplotlib.pyplot as plt


file = input("Enter the file name\n")
df = pd.read_excel(file)

x = df["Tensile strain(%)"]
y = df["Tensile stress(MPa)"]


plt.plot(x, y)
plt.xlabel("Strain (%)")
plt.ylabel("Stress (MPa)")
plt.title("Tensile Stress versus Strain")
plt.tight_layout()
plt.show()

