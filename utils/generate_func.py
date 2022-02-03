import random
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from utils.const import P1, P2, RND, Q1, Q2, FIRESENSORS, POPULATION, \
    FIGURETYPE, FIGUREGROUPS, RADIUS, REGIONS, ITERATIONS
from utils.target_func import f


def generate_one_firesensor():
    """ GENERATE ONE FIRESENSOR """
    x = round(random.uniform(P1, P2), RND)
    y = round(random.uniform(Q1, Q2), RND)

    return x, y


def generate_firesensors():
    """ GENERATE ARRAY OF FIREPOINTS
    розставляємо датчики на складі """
    FS = []
    while (len(FS) != FIRESENSORS):
        x, y = generate_one_firesensor()
        FS.append([x, y])
    return FS


def generate_firesensors_population():
    """ GENERATE POPULATION OF FIRESENSORS """
    P = []  # популяція складається із векторів-наборів датчиків
    for i in range(POPULATION):
        FS = generate_firesensors()
        P.append(FS)
        P[i].append(f(FS))  # останній елемент - фінтес-функція набору датчиків
    return P


def generate_one_figure(P):
    """ GENERATE FIGURES
    створюємо 1 фігуру заданого типу із векторів-наборів датчиків
    """
    FIG = random.sample(P, FIGURETYPE)
    return FIG


def create_figures(P):
    """ GENERATE FIGURES OF FIRESENSORS """
    G = []  # створюємо масив із створених груп (фігур)
    for i in range(FIGUREGROUPS):
        FIG = generate_one_figure(P)
        G.append(FIG)
    return G


def draw_scene(FP, FS, counterNum, method):
    """ DRAW PLOT SCENE """
    fig = plt.figure()
    # plt.figure(figsize=(P2, Q2))
    ax = plt.gca()
    ax.set_title('WAREHOUSE')  # заголовок
    plt.grid()
    ax.set_xlim(P1 - RADIUS / 2, P2 + RADIUS / 2)
    ax.set_ylim(Q1 - RADIUS / 2, Q2 + RADIUS / 2)
    ax.set_aspect('equal')

    # ДЖЕРЕЛА ПОЖЕЖ
    for i in range(len(FP)):
        plt.plot(FP[i][0], FP[i][1], 'x', color='r', markeredgewidth=3)

    # ЗОНИ ПОЖЕЖНОГО НАВАНТАЖЕННЯ
    for i in range(len(REGIONS)):
        start_x = REGIONS[i][0][0]
        start_y = REGIONS[i][0][1]
        r_width = REGIONS[i][1][0] - REGIONS[i][0][0]
        r_height = REGIONS[i][1][1] - REGIONS[i][0][1]
        rect = mpatches.Rectangle((start_x, start_y), r_width, r_height, linestyle='solid', edgecolor='blue',
                                  facecolor='none', linewidth=4)
        ax.add_patch(rect)

    # СПОВІЩУВАЧІ
    for i in range(len(FS) - 1):
        circ = mpatches.Circle((FS[i][0], FS[i][1]), RADIUS, linestyle='solid', edgecolor='g', facecolor='none',
                               linewidth=1.5)
        # plt.plot(FS[i][0], FS[i][1], '.', color='g', markeredgewidth=1.5) #центри сповіщувачів
        ax.add_patch(circ)

    plt.savefig('./plots/fire_' +
                str(ITERATIONS) +
                '_iter_' +
                method +
                str(FIGURETYPE) +
                '_counter_no_' +
                str(counterNum) +
                '.png')
    plt.show()


def draw_fitness_function_plot(allFitness, counterNum, method):
    """ DRAW FITNESS-FUNCTION PLOT """
    plt.figure()
    plt.title('FITNESS-FUNCTION')
    # plt.grid()
    plt.xlabel("iterations")
    plt.ylabel("fitness-function")

    plt.plot(allFitness, color='k', markeredgewidth=5)
    plt.savefig('./plots/fire_fitness_' +
                str(ITERATIONS) +
                '_iter_' +
                method +
                str(FIGURETYPE) +
                '_counter_no_' +
                str(counterNum) + '.png')
    plt.show()
