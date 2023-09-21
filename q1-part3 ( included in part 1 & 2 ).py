plt.scatter(normalizeX1, normalizeY, label='Data X1')
plt.scatter(normalizeX2, normalizeY, label='Data X2')
plt.scatter(normalizeX3, normalizeY, label='Data X3')
regression_line = [theta[0] + theta[1] * x + theta[2] * y + theta[3] * z for x, y, z in zip(normalizeX1, normalizeX2, normalizeX3)]
plt.plot(normalizeX1, regression_line, label='Regression Line', color='red')
plt.xlabel('Normalized X1, X2, X3')
plt.ylabel('Normalized Y')
plt.legend()
plt.title('Linear Regression')
plt.show()