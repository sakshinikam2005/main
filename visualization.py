import matplotlib.pyplot as plt

def plot_distribution(data, column):
    plt.hist(data[column])
    plt.show()

