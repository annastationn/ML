import matplotlib.pyplot as plt
def plot(x, y, xlabel = 'x', ylabel = 'y', title = 'График'):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o', label=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()