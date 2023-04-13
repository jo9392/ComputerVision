import os
PATH = "C:\\python\\ComputerVision"
global b_image, label_image, m, n


def read_image(file_name):
    global m, n
    f = open(PATH+file_name, 'r')
    m, n = map(int, f.readline().split())
    binary_list = []
    while(True):
        line = f.readline().split()
        if not line: break
        binary_list.append(line)
    return m, n, binary_list

def label_with_BT():    #라벨링 함수
    global b_image, label_image, m, n
    max_size = 1000 # 임의의 가능 개체 수 max 지정
    num_region = [0]*(max_size)   #개체의 개수 세는 리스트
    label_num=1                     #현재 추적 중인 개체의 라벨
    for i in range(1,height-1):     #네 면의 한 줄씩은 띄워놓고 사용
        for j in range(1, width-1):
            if label_image[i][j] == 0:  #label image에서 픽셀이 0일때
                cur_p = b_image[i][j]   #현재 탐색중인 픽셀 지정
                if cur_p == 1: # object를 만났을 때 탐색 시작
                    ref_p1 = label_image[i][j-1]
                    ref_p2 = label_image[i-1][j-1]
                    if ref_p1 > 1 : # p1에 개체가 있으면 propagation
                        num_region[ref_p1] += 1
                        label_image[i][j] = ref_p1
                    elif ref_p1==0 and ref_p2 >= 2: # p1은 비었고 p2에만 개체가 있으면 hole
                        num_region[ref_p2] += 1
                        label_image[i][j] = ref_p2
                        boundary_tracing(i, j, ref_p2, backward)
                    elif ref_p1 == 0 and ref_p2 == 0: ## 새로운 개체 탐색, region start
                        label_num += 1
                        num_region[label_num] += 1
                        label_image[i][j] = label_number
                        boundary_tracing(i, j, label_num, foreward)

def read_neighbor(y, x, neighbor8):
    return 0

def cal_coord(add_o, &y, &x):
    return 0

def boundary_tracing(y, x, label, tag):
    # neighbor8 배열은 x,y 주변 8픽셀값이 시계방향 순서대로 리스트 형태로 들어가있어야 함
    if tag == 'foreward': cur_orient = 0
    else: cur_orient = 6
    end_x = x
    end_y = y

    first_flag = False
    while(y!=end_y or x!=end_x or not first_flag):
        read_neighbor8(y, x, neighbor8)
        start_o = (8+cur_orient-2) % 8
        for i in range(8):
            add_o = (start_o + i) % 8
            if neighbor8[add_o] != 0:
                break

        # 여기부터 뭔말인지 모르겠다.
        if i < 8:
            cal_coord(add_o, &y, &x)
            cur_orient = add_o
            if label_image[y][x] == 0:
                num_region[label] += 1
                label_image[y][x] = label
        else: break

        first_flag = True


if __name__ == "__main__":
    m, n, b_image = read_image("\\input_example\\input1.txt")
    for i in input1: print(i)
