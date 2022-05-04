# store the item sets as tuples of strings in a list
from efficient_apriori import apriori
transactions = [
    ("beer", "wine", "cheese"),
    ("beer", "potato chips"),
    ("eggs", "flour", "butter", "cheese"),
    ("eggs", "flour", "butter", "beer", "potato chips"),
    ("wine", "cheese"),
    ("potato chips"),
    ("eggs", "flour", "butter", "wine", "cheese"),
    ("eggs", "flour", "butter", "beer", "potato chips"),
    ("wine", "beer"),
    ("beer", "potato chips"),
    ("butter", "eggs"),
    ("beer", "potato chips"),
    ("flour", "eggs"),
    ("beer", "potato chips"),
    ("eggs", "flour", "butter", "wine", "cheese"),
    ("beer", "wine", "potato chips", "cheese"),
    ("wine", "cheese"),
    ("beer", "potato chips"),
    ("wine", "cheese"),
    ("beer", "potato chips"),
]


# our min support is 7, but it has to be expressed as a percentage for efficient-apriori
min_support = 7/len(transactions)

# min confidence allows you to delete rules with low confidence.
# For now set min_confidence = 0 to obtain all the rules
min_confidence = 0
itemsets, rules = apriori(
    transactions, min_support=min_support, min_confidence=min_confidence)

print(itemsets)

for rule in rules:
    print(rule)
