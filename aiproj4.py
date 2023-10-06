import csv

data = []
float_row = []
float_data = []

with open("./cleaned.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    data.append(row)

#-----Adjustable Vars-----
initalWeight = 1
stepSize = .5
threshold = 7
cycles = 20 #number of cycles to train the data before validating

result = 0
numCorrect = 0

weights = []
weights.insert(0,0)#to make indexing weights the same as data
for i in range(1,87):#doesnt include last element of range
    weights.insert(i,initalWeight)

#1-587 survey responces/people(rows)
#predictors are in colums 1-86
#value to compare against is in colum 87
for z in range(0,cycles):
    for row in range(130,588):#130-588 to train
        for col in range(1,87):#col is actually range 1-86
            result += weights[col]*float(data[row][col])

        #set value to 1 or 0 to compare against correct value
        if result >= threshold:
            result = 1
        else:
            result = 0

        #check against correct value
        if result > float(data[row][87]):#87 stores correct value
            #do stuff to decrease weights
            for col in range(1,87):
                weights[col] -= (stepSize*float(data[row][col]))#normally would only adjust weights that effected outcome,
                                                                #since in a range, multiply by how big the predictor is
        elif result < float(data[row][87]):
            #do stuff to increase weights
            for col in range(1,87):
                weights[col] += (stepSize*float(data[row][col]))
        #DO NOTHING, value is correct

for row in range(1,130):#1-130 to validate
    for col in range(1,87):#col is actually range 1-86
        result += weights[col]*float(data[row][col])

    #set value to 1 or 0 to compare against correct value
    if result >= threshold:
        result = 1
    else:
        result = 0

    #check against correct value
    if result == float(data[row][87]):#87 stores correct value
        numCorrect += 1


#for i in range(1,87):
    #print(weights[i])

print(100*(float(numCorrect)/129.0))# Divide by size of validation data

#Write to file
i = 0
file = open('weights.txt', 'w')
file.write(str(threshold) + "\n")
for item in weights:
    file.write(str(weights[i]) + "\n")
    i+=1
file.close()
