#!/usr/bin/env python3

from collections import Counter

# Create a sequence

alphabet_soup = 'rishabhkumarjain'
as_count = Counter(alphabet_soup)
print(as_count)

# Update Count
as_count.update('rishabh')

print(as_count)

# Substract Count
as_count.subtract('rishabh')
print(as_count)


# Print Most Common
print(as_count.most_common())
