"""
You have a list with all available products in a store. The data is represented as a list of dicts

Your mission here is to find the most expensive products in the list. The number of products we are looking for will be given as the first argument and the list of all products as the second argument.

Input: int and list of dicts. Each dict has the two keys "name" and "price"

Output: The same format as the second input argument.
"""
from typing import List, Dict

var = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1},
]


def bigger_price(limit: int, data: List[Dict]) -> List[Dict]:
    return sorted(data, key=lambda x: x["price"], reverse=True)[:limit]
