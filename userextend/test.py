
from random import seed
from random import sample
seed(1)
sequence = [i for i in range(20)]
print(sequence)
subset = sample(sequence, 6)
print(subset)