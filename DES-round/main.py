import random
from tabulate import tabulate

E_BOX = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ]
]

def expansion_permutation(block):
    return ''.join(block[i - 1] for i in E_BOX)

def s_box_transform(block, s_box):
    row = int(block[0] + block[-1], 2)
    col = int(block[1:5], 2)
    return format(s_box[row][col], '04b')

def display_e_box():
    print("E_BOX table")
    for i in range(0, len(E_BOX), 6):
        print(E_BOX[i:i+6])
    print()

def display_s_box(s_box, index):
    print(f"S-BOX table {index + 1}")
    headers = [format(i, '04b') for i in range(16)]
    table = [[format(i, '02b')] + row for i, row in enumerate(s_box)]
    print(tabulate(table, headers=[""] + headers, tablefmt="grid"))
    print()

def des_round():
    print("DES Round")
    R_prev = format(random.randint(0, 2**32 - 1), '032b')
    K_i = format(random.randint(0, 2**48 - 1), '048b')
    print(f"R_(i-1) (32 bits): {R_prev}")
    print(f"K_i (48 bits): {K_i}")
    
    display_e_box()
    
    E_R_prev = expansion_permutation(R_prev)
    print(f"E(R_(i-1)) (48 bits): {E_R_prev}")
    
    xor_result = ''.join('1' if K_i[i] != E_R_prev[i] else '0' for i in range(48))
    print(f"K_i + E(R_(i-1)) (48 bits): {xor_result}")
    
    j = 1
    B_j = xor_result[(j - 1) * 6:j * 6]
    print(f"B_{j} (6 bits): {B_j}")
    
    display_s_box(S_BOXES[j - 1], j - 1)
    
    S_j_B_j = s_box_transform(B_j, S_BOXES[j - 1])
    print(f"S_{j}(B_{j}) (4 bits): {S_j_B_j}")

if __name__ == "__main__":
    des_round()