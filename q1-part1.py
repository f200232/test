import matplotlib.pyplot as plt
dataX = "DataX.dat"
dataY = "DataY.dat"
dataSize = 50
rateOfLearning = 1
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
    print(maxvalx1)
    print(minvalx1)
    
    return normalized_data

normalizeX1 = normalize(x1)
normalizeX2 = normalize(x2)
normalizeX3 = normalize(x3)
normalizeY = normalize(y)






theta0 = 0
theta1 = 0
theta2 = 0
theta3 = 0






# Initialize an initial_cost_function with a large value
initial_cost_function = float('inf')

while True:
    sumOfTheta0 = 0
    sumOfTheta1 = 0
    sumOfTheta2 = 0
    sumOfTheta3 = 0
    sumOfCostFunction = 0
    
    for i in range(dataSize):
        hyppthesis = (theta0 + theta1 * normalizeX1[i] + theta2 * normalizeX2[i] + theta3 * normalizeX3[i])
        sumOfTheta0 += (hyppthesis - normalizeY[i])
        sumOfTheta1 += (hyppthesis - normalizeY[i]) * normalizeX1[i]
        sumOfTheta2 += (hyppthesis - normalizeY[i]) * normalizeX2[i]
        sumOfTheta3 += (hyppthesis - normalizeY[i]) * normalizeX3[i]
        sumOfCostFunction += (hyppthesis - normalizeY[i])**2

    costFunction = (1 / (2 * len(normalizeX1))) * sumOfCostFunction
    if costFunction >= initial_cost_function:
        break
    initial_cost_function = costFunction
    theta0 -= (rateOfLearning * (1 / len(normalizeX1)) * sumOfTheta0)
    theta1 -= (rateOfLearning * (1 / len(normalizeX1)) * sumOfTheta1)
    theta2 -= (rateOfLearning * (1 / len(normalizeX1)) * sumOfTheta2)
    theta3 -= (rateOfLearning * (1 / len(normalizeX1)) * sumOfTheta3)

    
    
    
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
    


