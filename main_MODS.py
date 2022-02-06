import time
from utils.MODS_func import compression, turn_around_best_vector, turn_around_center_vector
from utils.const import FIGURETYPE, COUNT, ITERATIONS, FP
from utils.generate_func import generate_firesensors_population, create_figures, draw_scene, draw_fitness_function_plot, \
    generate_firesensors_square_net, generate_firesensors_triangle_net
from utils.other_func import aggregate, delete_duplicates, make_new_population
from utils.target_func import fitness_function

print("FIGURE TYPE: ", FIGURETYPE)

seconds1 = time.time()
local_time1 = time.ctime(seconds1)
print("start time: ", local_time1)

counterNum = 0
bestCounterFitness = []



while (counterNum < COUNT):  # запускаємо код COUNT раз, щоб вибрати найліпший варіант
    print("---- LAUNCH # ", counterNum)

    P = generate_firesensors_population()  # Початкова популяція
    allFitness = []
    iterNum = 0
    while (iterNum < ITERATIONS):
        # print("Current Iteration = ", iterNum)
        G = create_figures(P)  # формуємо масив фігур із популяції
        comprG = compression(G)  # робимо стиснення кожної фігури у масиві
        turnBestG = turn_around_best_vector(G)  # робимо поворот навколо найкращого вектору для кожної фігури у масиві
        turnCenterG = turn_around_center_vector(G)  # робимо поворот навкого центр. вектору для кожної фігури у масиві
        P_full = aggregate(P, comprG, turnBestG, turnCenterG)
        P_full = delete_duplicates(P_full)
        P = make_new_population(P_full)
        allFitness.append(P[0][-1])
        iterNum = iterNum + 1
    draw_scene(FP, P[0][:-1], counterNum, 'MODS')
    draw_fitness_function_plot(allFitness, counterNum, 'MODS')
    # останній результат після кожного запуску програми - найкращий, записуємо його
    bestCounterFitness.append([counterNum, allFitness[-1]])
    print("best fitness: ", allFitness[-1])
    print()
    counterNum = counterNum + 1

seconds2 = time.time()
local_time2 = time.ctime(seconds2)
print("start time: ", local_time2)

total_time = seconds2 - seconds1
print("TOTAL time (sec): ", total_time)


# SQUARE NET OF FIRESENSORS
FS_square_net = generate_firesensors_square_net()
print(len(FS_square_net))
square_net_fitness = fitness_function(FS_square_net)
print("SQUARE NET FITNESS-FUNCTION = ", square_net_fitness)
draw_scene(FP, FS_square_net, -1, 'SQUARE_NET')

# TRIANGLE NET OF FIRESENSORS
FS_triangle_net = generate_firesensors_triangle_net()
print(len(FS_triangle_net))
triangle_net_fitness = fitness_function(FS_triangle_net)
print("TRIANGLE NET FITNESS-FUNCTION = ", triangle_net_fitness)
draw_scene(FP, FS_triangle_net, -1, 'TRIANGLE_NET')





