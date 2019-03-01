
def calculateProfit(n, earning, cost, e):
    total_earnings = sum(earning[1:n]) * e
    total_cost = sum(cost[1:n-1]) * e
    final_result = total_earnings - total_cost
    return final_result 

print(calculateProfit(3, [1,5,5], [2,1,4], 4))
print(calculateProfit(4, [1,5,5], [2,1,4], 5))
