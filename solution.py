# PART-a --------------------->

# Code to calculate total number of combinations
total_combination = 6 * 6
print("Total number of possible combinations :", total_combination)


# Code to calculate and display all distributions
dist = [[0] * 6 for row in range(6)]
print(dist)
for i in range(6):
    for j in range(6):
        dist[i][j] = (i + 1) + (j + 1)

print("\nDistribution of all possible combinations:")
for row in dist:
    print(row)
    

# Code to calculate probability of each sum
p = {}
for i in range(2, 13):
    count = sum(row.count(i) for row in dist)
    p[i] = count / total_combination

print("\nProbability of each sum:")
for key, value in p.items():
    print(f"P(Sum = {key}) = ( {value:.3f} )")

    
    
# PART-B --------------------->  

def undoom_dice(die_a, die_b):
    # Calculate probabilities of all possible sums
    sum_probabilities = [0] * 13  # Index 0 won't be used
    # Calculate probabilities for each sum
    for face_a in die_a:
        for face_b in die_b:
            sum_probabilities[face_a + face_b] += 1

    total_combination = len(die_a) * len(die_b)

    # Calculate new spots distribution for Die A     
    new_die_a = [ ]
    for face_a in die_a:
        # Probability of each face on Die A
        p = sum_probabilities[face_a] / total_combination
        if p > 1 / 36:  
            new_face_a = min(4, face_a) 
        else:
            new_face_a = face_a
        new_die_a.append(new_face_a)

    # New Die B remains the same
    new_die_b = die_b

    return new_die_a, new_die_b

# Input
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]

new_die_a, new_die_b = undoom_dice(die_a, die_b)

# Output
print("\nNew Die A:", new_die_a)
print("New Die B:", new_die_b)


