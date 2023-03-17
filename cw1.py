"""Класна робота 1"""

# 10.1
def make_empty():
    return (0, 0, True)

def is_empty(seg):
    return seg[2]

def set_segment(a, b):
    if a != b:
        if a < b:
            return (a, b, False)
        else:
            raise Exception(ValueError)

    return make_empty()

def intersect(seg_1, seg_2):
    if seg_1[2] or seg_2[2]:
        return make_empty()

    if seg_1[1] < seg_2[0] or seg_1[0] > seg_2[1]:
        return make_empty()

    if seg_1[0] >= seg_2[0] and seg_1[1] <= seg_2[1]:
        return seg_1
    elif seg_1[0] <= seg_2[0] and seg_1[1] >= seg_2[1]:
        return seg_2
    
    if seg_1[0] >= seg_2[0] and seg_1[1] >= seg_2[1]:
        return (seg_1[0], seg_2[1], False)
    elif seg_1[0] <= seg_2[0] and seg_1[1] <= seg_2[1]:
        return (seg_2[0], seg_1[1], False)

if __name__ == '__main__':
    t1 = set_segment(-1, 10)
    t2 = set_segment(1, 12)
    print(t1)
    print(t2)
    t3 = intersect(t1, t2)
    print(t3)