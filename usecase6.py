import Calculator.Operations as CC

# get two inputs
input1 = int(input("input First number: "))
input2 = int(input("input Second number: "))

#perform various operations
print(CC.add(input1, input2))
print(CC.subtract(input1, input2))
print(CC.multiply(input1, input2))
print(CC.divide(input1, input2))