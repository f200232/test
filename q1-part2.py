import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

dataX = "DataX.dat"
dataY = "DataY.dat"
dataSize = 50
rateOfLearning = 0.02
x1= []
x2= []
x3= []
y= []

normalizeX1= []
normalizeX2= []
normalizeX3= []
normalizeY= []



with open(dataY, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        numeric_value = float(cleaned_line)
        y.append(numeric_value)
    
    
with open(dataX, "r") as file:
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        columns = cleaned_line.split()
        x1_value = float(columns[0])
        x2_value = float(columns[1])
        x3_value = float(columns[2])
        x1.append(x1_value)
        x2.append(x2_value)
        x3.append(x3_value)

def normalize(data):
    maxvalx1 = max(data)
    minvalx1 = min(data)
    meanx1 = sum(data)/50
    normalized_data = []
    for x in data:
     normalized_data.append(float((x - meanx1) / (maxvalx1 - minvalx1)))
    
    return normalized_data

normalizeX1 = normalize(x1)
normalizeX2 = normalize(x2)
normalizeX3 = normalize(x3)
normalizeY = normalize(y)
X = []
Y = []


for i in range(dataSize):
    X.append([1,normalizeX1[i],normalizeX2[i],normalizeX3[i]])
    
for i in range(dataSize):
    Y.append(normalizeY[i])
    
def transpose(matrix):
    # Determine the number of rows and columns in the original matrix
    num_rows = len(matrix)
    num_columns = len(matrix[0]) 

    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_columns)]
    # Fill the transposed matrix with values from the original matrix
    for i in range(num_rows):
        for j in range(num_columns):
            transposed_matrix[j][i] = matrix[i][j]
   
    return transposed_matrix

def inverse_matrix(matrix):
   
    # Convert the input matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)

    # Calculate the inverse using np.linalg.inv
    inverse = np.linalg.inv(matrix)

    return inverse.tolist()  # Convert the result back to a nested list
   

def matrix_multiply(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
          row.append(0)
        result.append(row)

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result    
      
transposeX = np.transpose(X)
inverse_X_transpose_X = inverse_matrix((transposeX @ X))
print(np.dot(transposeX , X))
theta = ((inverse_X_transpose_X @ transposeX)) @ Y
print(theta)
print("Theta 0 : " + str(float(theta[0])))
print("Theta 1 : " + str(float(theta[1])))
print("Theta 2 : " + str(float(theta[2])))
print("Theta 3 : " + str(float(theta[3])))

predicted_y = np.dot(X, theta)

# Calculate the squared error
squared_error = (predicted_y - Y)**2

# Calculate the cost function
cost = (1 / (2 * dataSize)) * np.sum(squared_error)
print(cost)
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