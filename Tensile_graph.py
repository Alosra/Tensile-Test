import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator



file = input("Enter the file name\n")
df = pd.read_excel(file)

x = df["Tensile strain(%)"]
y = df["Tensile stress(MPa)"]

fig, ax = plt.subplots()
ax.plot(x, y)

ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.grid(which="major", linestyle="-", linewidth=0.8, alpha=0.6)
ax.grid(which="minor", linestyle=":", linewidth=0.5, alpha=0.4)

fig.suptitle("Tensile Stress versus Strain")
ax.set_xlabel("Strain (%)")
ax.set_ylabel("Stress (MPa)")

plt.tight_layout()
plt.show()

