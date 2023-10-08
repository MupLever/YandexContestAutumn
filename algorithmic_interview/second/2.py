"""
Дан массив точек с целочисленными координатами (х, у).
Определить, существует ли вертикальная прямая, делящая
все точки, не лежащие на ней, на 2 симметричных относительно 
этой прямой набора точек.
"""

def answer(array):
    coord_set = set(array)
    left_border = min(array)
    right_border = max(array)
    med = (left_border + right_border) >> 1

    for x, y in coord_set:
        if (med + med - x, y) not in coord_set:
            return False
    return True
