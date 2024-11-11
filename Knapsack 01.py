# Function to solve the 0/1 Knapsack Problem using Dynamic Programming
def knapsack(weights, values, capacity, n):
    # Create a 2D DP array where dp[i][j] represents the maximum value
    # that can be achieved with the first i items and a maximum capacity of j
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP array from the bottom-up
    for i in range(1, n + 1):  # Loop through each item
        for w in range(1, capacity + 1):  # Loop through each weight capacity
            if weights[i - 1] <= w:  # If the item can be included in the knapsack
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Item cannot be included, take the previous result
                dp[i][w] = dp[i - 1][w]

    # The value at dp[n][capacity] is the maximum value that can be achieved
    return dp[n][capacity]

# Main function to test the knapsack function
def main():
    # Input number of items
    n = int(input("Enter the number of items: "))

    weights = []
    values = []
    
    # Input the weight and value of each item
    for i in range(n):
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        value = int(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)

    # Input the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Call the knapsack function to get the maximum value
    max_value = knapsack(weights, values, capacity, n)
    
    # Output the result
    print(f"The maximum value in the knapsack is: {max_value}")

if __name__ == "__main__":
    main()
