from art import logo

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiplication
def multiply(n1, n2):
  return n1 * n2

#division
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  should_continue=True
  
  for symbol in operations:
      print(symbol)
    
  while should_continue:
    operation_symbol=input("Pick an operation ")
    num2 = float(input("What's the next number "))
    calculation_function= operations[operation_symbol]
    answer= calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")=="y":
      num1=answer
    else:
      should_continue= False
      calculator()

calculator()