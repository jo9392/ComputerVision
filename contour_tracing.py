import os
PATH = "C:\\python\\ComputerVision"

def read_image(file_name):
    f = open(PATH+file_name, 'r')
    m, n = map(int, f.readline().split())
    binary_list = []
    while(True):
        line = f.readline().split()
        if not line: break
        binary_list.append(line)
    return m, n, binary_list

def label_with_BT():
    for i in range(max_size):
        num_region[i]=0
        label_num=1
    for i in range(1,height-1):
        for j in range(width-1):
            if label_image[i][j] <= 0:
                cur_p = b_image[i][j]
                if cur_p == 1: # object
                    ref_p1 = label_image[i][j-1]
                    ref_p2 = label_image[i-1][j-1]
                    if ref_pl > 1 : # propagation
                        num_region[ref_p1] += 1
                        label_image[i][j] = ref_p1
                    elif ref_pl==0 and ref_p2 >= 2: # hole
                        num_region[ref_p2] += 1
                        label_image[i][j] = ref_p2
                        boundary_tracing(i, j, ref_p2, backward)
                    elif ref_pl==0 and ref_p2==0: ## region start
                        label_num += 1
                        num_region[label_num] += 1
                        label_image[i][j] = label_number
                        boundary_tracing(i, j, label_num, foreward)
                else:
                    label_image[i][j] = 0


if __name__ == "__main__":
    m, n, input1 = read_image("\\input1.txt")
    for i in input1: print(i)
