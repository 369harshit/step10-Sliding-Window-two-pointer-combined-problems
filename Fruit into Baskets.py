def totalFruit(fruits):
    max_fruits = 0
    n = len(fruits)

    for i in range(n):
        basket1 = basket2 = None
        count = 0
        j = i

        while j < n:
            if fruits[j] == basket1 or fruits[j] == basket2:
                count += 1
            elif basket1 is None:
                basket1 = fruits[j]
                count += 1
            elif basket2 is None:
                basket2 = fruits[j]
                count += 1
            else:
                break
            j += 1

        max_fruits = max(max_fruits, count)

    return max_fruits

fruits = [1,2,1]
result = totalFruit(fruits)
print("Maximum number of fruits picked:", result)
