# Mendelian Inheritence

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Total Population t = k + m + n
# Probability of atleast one dominant gene (numerator): k(k-1) + 2*k*m + 2*k*n + 0.5n*m + 0.5n*m + 0.75*m(m-1)

import random

def formula(k, m, n):
    total_population = k + m + n

    if total_population < 2:
        return 0.0

    numerator = (k * (k - 1) + # AA/AA
                 (k * m + m * k) + #AA/Aa
                 (k * n + n * k) + #AA/aa
                 0.75 * m * (m - 1) + #Aa/Aa
                 0.5 * m * n + 0.5 * m * n) #Aa/aa

    probability = numerator / (total_population * (total_population - 1))
    
    return probability

def simulate_probability(k, m, n, trials = 100000):
    # create the population
    population = ["AA"] * k + ["Aa"] * m + ["aa"] * n

    dominant_tally = 0
    for i in range (trials):
        parent1, parent2 = random.sample(population, 2)

        if parent1 == "AA" or parent2 == "AA":
            dominant_tally += 1
        elif parent1 == "Aa" and parent2 =="Aa":
            dominant_tally += random.choices([1, 1, 1, 0], k = 1)[0] # 0.75 chance of atleast one dominant allele
        elif (parent1 == "Aa" and parent2 == "aa") or (parent1 == "aa" and parent2 == "Aa"):
            dominant_tally += random.choices([1,0], weights = [0.5,0.5], k = 1)[0] # 0.5 chance of atleast one dominant allele

    probability = dominant_tally / trials
    return probability

    

print(f"Probability using the formula: {formula(2,2,2)}")
print(f"Simulated probability: {simulate_probability(2, 2, 2)}")


