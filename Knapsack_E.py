# Write a program to solve a 0-1 Knapsack problem using dynamic #programming or branch and bound strategy. 
def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i - 1][0] <= w:
                dp[i][w] = max(
                    items[i - 1][1] + dp[i - 1][w - items[i - 1][0]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruct the selected items
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            i -= 1
            w -= items[i][0]
        else:
            i -= 1

    return dp[n][capacity], selected_items

# Example usage
items = [(2, 10), (3, 15), (5, 40), (7, 60)]
capacity = 10

max_value, selected_items = knapsack(items, capacity)

print("Maximum Value:", max_value)
print("Selected Items:")
for item in selected_items:
    print("Weight:", item[0], "Value:", item[1])

