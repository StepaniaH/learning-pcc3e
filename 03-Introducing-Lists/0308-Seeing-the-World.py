tourist_destinations = ['US', 'JP', 'UK', 'DE', 'FR']
print(tourist_destinations)

print(sorted(tourist_destinations))

print(tourist_destinations)

print(sorted(tourist_destinations, reverse=True))

print(tourist_destinations)

tourist_destinations.reverse()
print(tourist_destinations)
"""
The output of the command `print(tourist.destinations.reverse())` is `None`, due to reverse() returns nothing.
If you want to write it in one line, you can use the reverse() method with a logical OR operator:
```
print(tourist.destinations.reverse() or tourist.destinations)
```
This method utilizes Python's short-circuit evaluation of the logical OR operator (or). Here's how it works:
    a. reverse() is called first. This method reverses the list a in-place and returns None.
    b. In Python, None is considered False in a boolean context.
    c. The or operator evaluates its left operand (a.reverse()). Since it's None (which is False), it moves on to evaluate the right operand (a).
    d. The right operand a is the reversed list, which is then returned and printed.
"""

tourist_destinations.reverse()
print(tourist_destinations)

tourist_destinations.sort()
print(tourist_destinations)

tourist_destinations.sort(reverse=True)
print(tourist_destinations)