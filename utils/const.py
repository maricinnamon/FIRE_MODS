import math
import random

FIREPOINTS = 100  # кількість пожеж
POPULATION = 10  # кількість наборів сповіщувачів
FIRESENSORS = 15  # кількість сповіщувачів у наборі
RADIUS = 2  # радіус дії одного сповіщувача
PROB = 0.9  # ймовірність спрацювання сповіщувача

FIGURETYPE = 3  # n-кутник
FIGUREGROUPS = 10  # скільки фігур створюємо для перетворень
DIST_COEF = 2  # коефіцієнт для перетворень

RND = 4  # кількість знаків після коми
OPTIMIZATION = "min"  # "max" / "min"

# OX
P1 = 0
P2 = 10
# OY
Q1 = 0
Q2 = 10

# ДИНАМІЧНА ШТРАФНА ФУНКЦІЯ
C = 0.1  # початкове значення множника штрафної ф-ції
V = 10  # швидкість зростання
LYAMBDAMAX = 10  # максимальне значення множника

# РЕГІОНИ ПІДВИЩЕННОЇ НЕБЕЗПЕКИ
# прямокутні зони із коєфіцієнтом загоряння
REGIONS = [
    [[0, 0], [2, 10], 0.9],
    [[3, 9], [10, 10], 0.2],
    [[3, 0], [10, 8], 0.5]
]

# УМОВИ ЗАКІНЧЕННЯ
ITERATIONS = 100
EPS = math.pow(1 * 10, -1 * RND)  # точність

# СКІЛЬКИ РАЗІВ ЗАПУСКАЄМО КОД
COUNT = 5



def generate_firepoints():
    """ GENERATE ARRAY OF FIREPOINTS
    розставляємо точки пожежі на складі """
    FP = []
    while (len(FP) != FIREPOINTS):
        x = round(random.uniform(P1, P2), RND)
        y = round(random.uniform(Q1, Q2), RND)

        for j in range(len(REGIONS)):
            if (REGIONS[j][0][0] <= x <= REGIONS[j][1][0] and REGIONS[j][0][1] <= y <= REGIONS[j][1][1]):
                FP.append([x, y])
    return FP


FP = generate_firepoints()
