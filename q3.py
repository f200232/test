import math
dataX = "DataX.dat"
dataY = "ClassY.dat"
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






theta0 = 0
theta1 = 0
theta2 = 0
theta3 = 0






print("Input Data : ")
for i in range(50):
    print("Row " + str(i) + " : ")
    print(str(normalizeX1[i]) + " " + str(normalizeX2[i]) + " " + str(normalizeX3[i]) + " = " + str(normalizeY[i]))
    

convergence_threshold = 0.0001
initial_cost = float('inf')
while True:
    sumOfTheta1 = 0
    sumOfTheta2 = 0
    sumOfTheta3 = 0
    sumOfTheta0 = 0
    cost = 0
    for j in range(dataSize):
        hypothesis = theta0 + theta1 * normalizeX1[j] + theta2 * normalizeX2[j] + theta3 * normalizeX3[j] 
        probability = 1 / (1 + math.exp(-hypothesis))
        sumOfTheta0 += (probability - normalizeY[j])
        sumOfTheta1 += (probability - normalizeY[j]) * normalizeX1[j]
        sumOfTheta2 += (probability - normalizeY[j]) * normalizeX2[j]
        sumOfTheta3 += (probability - normalizeY[j]) * normalizeX3[j]
        cost += normalizeY[j] * math.log(probability) + (1 - normalizeY[j]) * math.log(1 - probability)

    cost = -cost / dataSize
    theta0 -= rateOfLearning * (1/dataSize) * sumOfTheta0
    theta1 -= rateOfLearning * (1/dataSize) * sumOfTheta1
    theta2 -= rateOfLearning * (1/dataSize) * sumOfTheta2
    theta3 -= rateOfLearning * (1/dataSize) * sumOfTheta3

    if abs(initial_cost - cost) < convergence_threshold:
        print("Converged at iteration", i)
        break

    initial_cost = cost

    print("-------------------------------------------------")
    print("Cost : " + str(cost))
    print("Theta0 : " + str(theta0))
    print("Theta1 : " + str(theta1))
    print("Theta2 : " + str(theta2))
    print("Theta3 : " + str(theta3))
    
    
    
    
    
    


