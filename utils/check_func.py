from utils.const import Q2, P1, P2, Q1


def transform_compression_check(x, y, x0, y0):
    """ TRANSFRORM COMPRESSION CHECK
    перевірка того, чи не виходить нова найкраща точка за область дослідження """
    # Omega-9
    if (y > Q2 and P1 <= x <= P2):
        y = (y0 + Q2) / 2

    # Omega-3
    elif (y < Q2 and P1 <= x <= P2):
        y = (y0 + Q2) / 2

    # Omega-6
    elif (x > P2 and Q2 <= y <= Q2):
        x = (x0 + P2) / 2

    # Omega-12
    elif (x < P1 and Q2 <= y <= Q2):
        x = (x0 + P1) / 2

    # Omega-1 and Omega-2
    elif (x < P1 and y < Q2):
        y = (y0 + Q2) / 2
        x = (x0 + P1) / 2

    # Omega-10 and Omega-11
    elif (x < P1 and y > Q2):
        y = (y0 + Q2) / 2
        x = (x0 + P1) / 2

    # Omega-7 and Omega-8
    elif (x > P2 and y > Q2):
        y = (y0 + Q2) / 2
        x = (x0 + P2) / 2

    # Omega-4 and Omega-5
    elif (x > P2 and y < Q2):
        y = (y0 + Q2) / 2
        x = (x0 + P2) / 2

    return x, y





def transform_turn_check(x, y):
    """ TRANSFRORM TURN CHECK """
    # Omega-9
    if (y > Q2 and P1 <= x <= P2):
        y = y + (Q1 - Q2)

    # Omega-3
    elif (y < Q1 and P1 <= x <= P2):
        y = y + (Q2 - Q1)

    # Omega-6
    elif (x > P2 and Q1 <= y <= Q2):
        x = x + (P1 - P2)

    # Omega-12
    elif (x < P1 and Q1 <= y <= Q2):
        x = x + (P2 - P1)

    # Omega-1 and Omega-2
    elif (x < P1 and y < Q1):
        y = y + (Q2 - Q1)
        x = x + (P2 - P1)

    # Omega-10 and Omega-11
    elif (x < P1 and y > Q2):
        y = y + (Q1 - Q2)
        x = x + (P2 - P1)

    # Omega-7 and Omega-8
    elif (x > P2 and y > Q2):
        y = y + (Q1 - Q2)
        x = x + (P1 - P2)

    # Omega-4 and Omega-5
    elif (x > P2 and y < Q1):
        y = y + (Q2 - Q1)
        x = x + (P1 - P2)

    return x, y
