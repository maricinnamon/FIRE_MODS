import math
import random

from utils.check_func import transform_compression_check, transform_turn_check
from utils.const import OPTIMIZATION, RND, DIST_COEF
from utils.other_func import s
from utils.target_func import f


def find_best_vector(FIG):
    """ FIND BEST VECTOR IN FIG
    шукаємо у кожній фігурі найкращий вектор """
    if (OPTIMIZATION == "max"):
        best = max(FIG, key=s)
    elif (OPTIMIZATION == "min"):
        best = min(FIG, key=s)
    return best


def find_center_vector(FIG):
    """  FIND CENTER VECTOR FOR FIG """
    center = []
    # проходимося по стовпчикам
    for j in range(len(FIG[0]) - 1):  # -1 бо останнє значення - це ЦФ
        x = 0
        y = 0
        for i in range(len(FIG)):
            x = x + FIG[i][j][0]
            y = y + FIG[i][j][1]

        x = round(x / len(FIG), RND)
        y = round(y / len(FIG), RND)
        center.append([x, y])

    center.append(f(center))  # ост. ел. - фінтес-функція "центрального" набору датчиків

    return center


def compression_of_one_figure(FIG):
    """ COMPRESSION OF ONE FIG """
    comprFIG = []  # масив, що містить всі вектори у фігурі
    newVector = []  # один новий вектор

    best = find_best_vector(FIG)  # знаходимо найкращий вектор
    center = find_center_vector(FIG)  # знаходимо центральний вектор

    # СТИКАЄМО НАЙКРАЩИЙ ВЕКТОР
    for i in range(len(best) - 1):  # -1 бо останнє значення - це ЦФ
        x0 = best[i][0]
        y0 = best[i][1]

        x2 = center[i][0]
        y2 = center[i][1]

        x1 = (1 + DIST_COEF) * x0 - DIST_COEF * x2
        y1 = (1 + DIST_COEF) * y0 - DIST_COEF * y2

        # transform compression check HERE
        x1, y1 = transform_compression_check(x1, y1, x0, y0)

        # regions check HERE
        # !!!!!!!!!!!!!!!!!!!!!!
        # Якщо датчик не покриває частини зон пожежного навантаження - якось його перемістити

        x1 = round(x1, RND)
        y1 = round(y1, RND)

        newVector.append([x1, y1])
    newVector.append(f(newVector))  # останній елемент - фінтес-функція набору датчиків
    comprFIG.append(newVector)  # додаємо новий найкращий вектор до масиву нової стиснутої фігури

    # СТИСКАЄМО ВСІ ІНШІ ВЕКТОРИ
    for q in range(len(FIG)):
        curVector = FIG[q]  # записуємо поточний вектор

        if (curVector != best):  # для всіх векторів, які не є найкращим (бо тот ми вже змінили)
            newVector = []  # новий вектор, що утвориться із поточного вектора
            for i in range(len(curVector) - 1):  # -1 бо останнє значення - це ЦФ
                x1 = best[i][0]
                y1 = best[i][1]

                x2 = curVector[i][0]
                y2 = curVector[i][1]

                x0 = (x1 + DIST_COEF * x2) / (1 + DIST_COEF)
                y0 = (y1 + DIST_COEF * y2) / (1 + DIST_COEF)

                x0 = round(x0, RND)
                y0 = round(y0, RND)

                newVector.append([x0, y0])
            newVector.append(f(newVector))  # останній елемент - фінтес-функція
            comprFIG.append(newVector)  # додаємо новий вектор до масиву фігури

    return comprFIG


def compression(G):
    """ COMPRESSION OF ALL FIGURES """
    comprG = []

    for w in range(len(G)):  # для кожної фігури у масиві
        curFIG = G[w]
        comprFIG = compression_of_one_figure(curFIG)  # робимо стиснення фігури
        comprG.append(comprFIG)  # і записуємо її у новий масив

    return comprG


def turn_one_point(b1, b2, p1, p2, beta):
    """ TURN ONE POINT """
    # b1, b2 - координати точки у кращому векторі,
    # p1, p2 - координати точки у інших векторах,
    # beta - кут повороту
    p1new = b1 + (p1 - b1) * math.cos(beta) - (p2 - b2) * math.sin(beta)  # !!!! не +p1, а +b1
    p2new = b2 + (p1 - b1) * math.sin(beta) - (p2 - b2) * math.cos(beta)  # !!!! не +p2, а +b2

    return p1new, p2new


def turn_of_one_figure_around_best_vector(FIG):
    """ TURN OF ONE FIG AROUND BEST VECTOR """
    turnFIG = []

    best = find_best_vector(FIG)  # знаходимо найкращий вектор

    # ПОВЕРТАЄМО ВСІ ВЕКТОРИ, ОКРІМ НАЙКРАЩОГО
    for q in range(len(FIG)):
        curVector = FIG[q]  # записуємо поточний вектор

        if (curVector != best):
            newVector = []  # один новий вектор
            beta = random.uniform(0, 360)  # випадковий кут повороту всього вектору

            for i in range(len(curVector) - 1):  # -1 бо останнє значення - це ЦФ
                b1 = best[i][0]
                b2 = best[i][1]

                p1 = curVector[i][0]
                p2 = curVector[i][1]

                p1new, p2new = turn_one_point(b1, b2, p1, p2, beta)

                p1new, p2new = transform_turn_check(p1new, p2new)

                p1new = round(p1new, RND)
                p2new = round(p2new, RND)

                newVector.append([p1new, p2new])
            newVector.append(f(newVector))  # останній елемент - фінтес-функція
            turnFIG.append(newVector)  # додаємо новий вектор до масиву фігури

    return turnFIG


''' --- TURN ALL FIGURES AROUND BEST VECTOR ---- '''


def turn_around_best_vector(G):
    turnBestG = []

    for w in range(len(G)):  # для кожної фігури у масиві
        curFIG = G[w]
        turnFIG = turn_of_one_figure_around_best_vector(curFIG)  # робимо поворот навколо найкращого вектору
        turnBestG.append(turnFIG)  # і записуємо її у новий масив

    return turnBestG


''' --- TURN OF ONE FIG AROUND CENTER VECTOR --- '''


def turn_of_one_figure_around_center_vector(FIG):
    turnFIG = []

    center = find_center_vector(FIG)  # знаходимо найкращий вектор

    # ПОВЕРТАЄМО ВСІ ВЕКТОРИ, ОКРІМ НАЙКРАЩОГО
    for q in range(len(FIG)):
        curVector = FIG[q]  # записуємо поточний вектор
        newVector = []  # один новий вектор

        alpha = random.uniform(0, 360)  # випадковий кут повороту всього вектору

        for i in range(len(curVector) - 1):  # -1 бо останнє значення - це ЦФ
            c1 = center[i][0]
            c2 = center[i][1]

            p1 = curVector[i][0]
            p2 = curVector[i][1]

            p1new, p2new = turn_one_point(c1, c2, p1, p2, alpha)

            p1new, p2new = transform_turn_check(p1new, p2new)

            p1new = round(p1new, RND)
            p2new = round(p2new, RND)

            newVector.append([p1new, p2new])
        newVector.append(f(newVector))  # останній елемент - фінтес-функція
        turnFIG.append(newVector)  # додаємо новий вектор до масиву фігури

    return turnFIG


''' -- TURN ALL FIGURES AROUND CENTER VECTOR --- '''


def turn_around_center_vector(G):
    turnCenterG = []

    for w in range(len(G)):  # для кожної фігури у масиві
        curFIG = G[w]
        turnFIG = turn_of_one_figure_around_center_vector(curFIG)  # робимо поворот навколо центрального вектору
        turnCenterG.append(turnFIG)  # і записуємо її у новий масив

    return turnCenterG
