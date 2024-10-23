#math functions. chapter 5
def max(x, y, z):
    m_value = x
    if m_value < y and z < y:
        m_value = y
    elif m_value < z and y < z:
        m_value = z
    else:
        return m_value
    return m_value
def absolute_value(x): return abs(x)

def sign_of(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1
print(max(4, 8, 10))
print(absolute_value(-9))
print(sign_of(-0))
