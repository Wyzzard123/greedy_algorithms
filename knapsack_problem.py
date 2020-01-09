"""
Knapsack problem with divisible weights
"""

# class Item:
# TODO
#     def __init__(self, name, profit, weight):
#         """An item to be placed into the knapsack"""
#         self.name = name
#         self.profit = profit
#         self.weight = weight

# class Knapsack:
# TODO
#     def __init__(self, capacity):
#         """The knapsack"""
#         self.capacity = capacity
#         self.bag = [None] * capacity

# empty_knapsack = Knapsack(5)
# print(problem_bag.bag)

# Items to be placed into knapsack




def knapsack_greedy(names, profits, weights, capacity):
    """Solves a knapsack problem with a list of names, profits, and weights. Returns a dict with the optimal knapsack, with the keys being the item names and the values being tuples of the profits and weights."""
    items = {}
    item_densities = {}
    optimal_knapsack = {}
    number_of_items = len(names)
    
    if len(set(names)) != len(names):
        print("There are some non-unique names.")
        return False

    if len(names) == len(profits) == len(weights):
        for i in range(len(names)):
            name = names[i]
            profit = profits[i]
            weight = weights[i]
            density = profit/weight
            items[name] = (profit, weight)
            item_densities[name] = density
        # print(items)
        # print(item_densities)
    
        # Finds the key with the maximum value

        capacity_remaining = capacity
        items_in_knapsack = []
        total_profit = 0
        for i in range(capacity):
            
            if capacity_remaining == 0:
                break

            highest_profit_density_name = max(item_densities, key=lambda k: item_densities[k])

            items_in_knapsack.append(highest_profit_density_name)


            # Subtract weight. If less than 0, put a fraction
            if capacity_remaining - items[highest_profit_density_name][1] < 0:
                
                profit_of_item = item_densities[highest_profit_density_name] * capacity_remaining

                weight_of_item = items[highest_profit_density_name][1]
                
                amount_of_item = capacity_remaining/items[highest_profit_density_name][1]
                
                optimal_knapsack[highest_profit_density_name] = (amount_of_item, profit_of_item, weight_of_item)

                total_profit += profit_of_item

                break

            else:
                profit_of_item = items[highest_profit_density_name][0]
                weight_of_item = items[highest_profit_density_name][1]

                amount_of_item = 1

                optimal_knapsack[highest_profit_density_name] = (amount_of_item, profit_of_item, weight_of_item)
                
                capacity_remaining -= items[highest_profit_density_name][1]
                total_profit += profit_of_item
            
            item_densities.pop(highest_profit_density_name)
            # print(highest_profit_density_name)
            if i == number_of_items - 1:
                print("Number of items is lower than capacity")
                break
        items_in_knapsack.sort()
        print("The optimal_knapsack contains items:")
        for item in items_in_knapsack:
            print(f"{optimal_knapsack[item][0]:0.2f} of {item} with an original weight of {optimal_knapsack[item][2]:0.2f} and a profit of ${optimal_knapsack[item][1]:0.2f}")
        print("The total profit was $%0.2f" % total_profit)

        return optimal_knapsack
    else:
        print("Lists are not of the same length.")
        return False
    

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
profits = [10, 20, 10, 15, 23, 12, 18]
weights = [3, 2, 5, 3, 2, 4, 3]

knapsack_greedy(names, profits, weights, 11)

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x1', 'x2', 'ten', 'ah']
profits = [10, 20, 10, 15, 23, 12, 18, 12, 42, 12, 23]
weights = [3, 2, 5, 3, 2, 4, 3, 3, 12, 1, 3]

knapsack_greedy(names, profits, weights, 23)
