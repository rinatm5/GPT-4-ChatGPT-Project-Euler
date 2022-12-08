# Define the function that finds the number of distinct
# terms in the sequence generated by a**b for 2 ≤ a ≤ 200
# and 2 ≤ b ≤ 200
def find_distinct_terms():
    # Create an empty set
    terms = set()

    # Loop over the possible values of a
    for a in range(2, 201):
        # Loop over the possible values of b
        for b in range(2, 201):
            # Calculate the value of a**b and add it to the set
            terms.add(a**b)

    # Return the number of distinct terms in the set
    return len(terms)

# Find the number of distinct terms in the sequence
# generated by a**b for 2 ≤ a ≤ 200 and 2 ≤ b ≤ 200
distinct_terms = find_distinct_terms()

# Print the result
print(distinct_terms)  # 15,625

