def calculation_area_circle(r):
    S = 3.14 * (r ** 2)
    return S

def calculation_area_triangle(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S

