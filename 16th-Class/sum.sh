
#!/bin/bash

# Function to add two numbers

adder() {
  local num1=$1  # Use local to keep variables within the function's scope
  local num2=$2
  local sum=$((num1 + num2))
  echo "$sum"
}

# Get the first number from the user
read -p "Enter the first number: " num1

# Get the second number from the user
read -p "Enter the second number: " num2

# Call the adder function and store the result
result=$(adder "$num1" "$num2") #added "" to the variables

echo "The sum of $num1 and $num2 is: $result"
