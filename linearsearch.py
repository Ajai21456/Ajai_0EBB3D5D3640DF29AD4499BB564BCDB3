def linear_search_product(product_list, target_product):
  indices = []
  for index, product in enumerate(product_list):
    if product == target_product:
      indices.append(index)
  return indices


# Sample list of products
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

# Target product to search for
target = "Apple"

# Call the linear_search_product function
result = linear_search_product(products, target)

# Print the result
print("Indices of '{}' found in the list: {}".format(target, result))
