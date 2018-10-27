from matplotlib import pyplot as plt
programming = ['Software Engineer', 'Information System', 'Networking', 'Artificial Intelligence']
popular = [20, 35, 60, 5]

# for customization bar size
xs = [i + 0.5 for i, _ in enumerate(programming)]
plt.bar(xs, popular)

plt.ylabel('# Popular Topic')
plt.title('Popular Thesis Topic')

plt.xticks([i + 0.5 for i, _ in enumerate(programming)], programming)
plt.show()