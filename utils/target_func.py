from utils.const import REGIONS, RADIUS, PROB, FP
from utils.other_func import euclidean_distance


def fitness_function(FS):
    """ TARGET FUNCTION """
    '''
    s = 0 # фінтес-функція просто для перевірки, що все гарно працює, без помилок
    for i in range(len(FS)):
        s = s + FS[i][0]*FS[i][1]
    return s
    '''

    N = len(FS)  # кількість сповіщувачів у наборі
    M = len(FP)  # кількість точок пожежі
    R = len(REGIONS)  # кількість регіонів підвищенної небезпеки

    # СТАРА ВЕРСІЯ
    firstSum = 0
    for l in range(R):
        nu = REGIONS[l][-1]  # ваговий коефіцієнт
        sM = 0
        for i in range(M):
            sN = 0
            allDistInRow = []  # для вибору мінімальної відстані в рядку
            for j in range(N):
                dist = euclidean_distance(FP[i], FS[j])
                allDistInRow.append(dist)

                if (dist < RADIUS):  # якщо відстань менше радіусу, записуємо 1
                    sN = sN + 1

            if (sN > 0 and
                    (REGIONS[l][0][0] <= FP[i][0] <= REGIONS[l][1][0] and
                    REGIONS[l][0][1] <= FP[i][1] <= REGIONS[l][1][1])):
                # якщо точка пожежі належить хоча б одній зоні відповідальності якогось датчика
                # і належить поточному регіону небезпеки, записуємо 1
                temp = 1
            else:
                temp = 0

            sPow = 0  # сума для обчислення числа степені у множнику, що буде далі
            for j in range(N):  # знову проходимося по коміркам поточного рядка матриці, рахуємо нову суму
                dist = euclidean_distance(FP[i], FS[j])
                if (dist < RADIUS and (
                        REGIONS[l][0][0] <= FP[i][0] <= REGIONS[l][1][0] and REGIONS[l][0][1] <= FP[i][1] <=
                        REGIONS[l][1][1])):
                    sPow = sPow + 1

            if (sPow > 0):  # якщо степінь додатня
                p = 1 / (1 - pow((1 - PROB), sPow))
            else:  # інакше - просто прирівнюємо до 1 (це взято із книжки)
                p = 1

            sM = sM + temp * p * min(allDistInRow)

        firstSum = firstSum + sM * nu

    # друга сума - штрафна, буде збільшуватися,
    # якщо точка виникнення пожежі не належить жодній зоні відповідальності датчика
    secondSum = 0
    for l in range(R):
        nu = REGIONS[l][-1]  # ваговий коефіцієнт
        sM = 0
        for i in range(M):
            sN = 0
            allDistInRow = []  # для вибору мінімальної відстані в рядку
            for j in range(N):
                dist = euclidean_distance(FP[i], FS[j])
                allDistInRow.append(dist)

                if (dist < RADIUS and
                   (REGIONS[l][0][0] <= FP[i][0] <= REGIONS[l][1][0] and
                   REGIONS[l][0][1] <= FP[i][1] <=REGIONS[l][1][1])):
                    sN = sN + 1

            if (sN == 0):
                temp = 1
            else:
                temp = 0

            sM = sM + temp * min(allDistInRow)

        secondSum = secondSum + sM * nu

    result = firstSum + secondSum

    return result


