def create_multipliers():
    return [lambda x : i * x for i in range(5)]
for mul in create_multipliers():
    print(mul(2))
