# Nested lists are a way to combine two lists that are separate but related.
# Example can be fruits and vegetables with pesticides in them.
# We want to take two separate lists and combine them into one list.

# These are known as the dirty dozen of fruits and vegatables that have the highest pesticides in them
print("\n\n")
fruits = ["strawberries", "nectarines", "apples",
          "grapes", "peaches", "cherries", "pears"]
print(f"Fruits with the most amount of pesticides: {fruits}\n\n")

vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]
print(
    f"Vegetables with the most amount of pesticides in them: {vegetables}\n\n")
# Combine the lists into a nested list

dirty_dozen = [fruits, vegetables]
print(
    f"The combined list of fruits and vegetables with the most amount of pesticides are: \n {dirty_dozen}\n\n")
