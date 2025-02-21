
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

import datetime
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def time_check(): #수행시간 확인 함수입니다. 내용 수정하지 말아주세요
    print("중간고사 시험 수행 인증시간:", "%s년 %s월 %s일 %s시 %s분" %(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day,datetime.datetime.now().hour,datetime.datetime.now().minute))

#미로찾기 함수입니다. 내용 수정하지 말아주세요
def my_maze(maze, start, end):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)

    print("시작")
    while qu:
        p = qu.pop(0)
        v = p[-1]
        
        if v == end:
            print("종료")
            return p

        for x in maze[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)



def exam_1():
    print("문제1번")
    #코딩은 여기부터 시작해주세요
    x_values = list(range(-10, 11))

    y1_values = [2 ** x for x in x_values]  # For 2^x
    y2_values = [(1 / 2) ** x for x in x_values]  # For (1/2)^x

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y1_values, label=r'$2^x$', marker='o', color='blue')

    plt.plot(x_values, y2_values, label=r'$(\frac{1}{2})^x$', marker='x', color='red')

    plt.title("Graphs of $2^x$ and $(\\frac{1}{2})^x$", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)
    plt.show()
    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()

def exam_2():
    print("문제2번")
    #코딩은 여기부터 시작해주세요
    x = np.linspace(0, 10 * np.pi, 500)

    a = (x + 1) ** 2
    b = 2 * (x + 1)

    sin_a = np.sin(a)
    cos_b = np.cos(b)
    sin_a_plus_b = np.sin(a + b)

    plt.figure(figsize=(10, 4))
    plt.plot(x, sin_a, label=r'$\sin(a)$', color='blue')
    plt.title(r'Graph of $\sin((x+1)^2)$', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, cos_b, label=r'$\cos(b)$', color='red')
    plt.title(r'Graph of $\cos(2(x+1))$', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)
    plt.show()

    plt.figure(figsize=(10, 4))
    plt.plot(x, sin_a_plus_b, label=r'$\sin(a+b)$', color='green')
    plt.title(r'Graph of $\sin((x+1)^2 + 2(x+1))$', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend(fontsize=12)
    plt.show()
    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()

def exam_3():
    print("문제3번")
    #코딩은 여기부터 시작해주세요

    n = int(input("숫자를 입력하세요: "))

    A = {i for i in range(1, n + 1, 2)}

    B = {i for i in range(1, n + 1, 3)}

    C = {2**i for i in range(0, n + 1) if 2**i <= n}

    B_cross_C = {(b, c) for b in B for c in C}

    print("집합 A:", A)
    print("집합 B:", B)
    print("집합 C:", C)
    print("곱집합 B × C:", B_cross_C)
    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()
    
def exam_4():
    print("문제4번")
    #코딩은 여기부터 시작해주세요

    A_positive = 14540
    A_negative = 1120
    B_positive = 14250
    B_negative = 170090

    A_non_carrier_positive = B_positive
    total_A_non_carrier = B_positive + B_negative
    prob_A_non_carrier_positive = A_non_carrier_positive / total_A_non_carrier

    A_carrier_negative = A_negative
    total_A_carrier = A_positive + A_negative
    prob_A_carrier_negative = A_carrier_negative / total_A_carrier

    print(f"(1) A균 미보균자일 때 양성 반응을 보일 확률: {prob_A_non_carrier_positive:.4f}")
    print(f"(2) A균 보균자일 때 음성 반응을 보일 확률: {prob_A_carrier_negative:.4f}")

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()
    
def exam_5():
    print("문제5번")
    #코딩은 여기부터 시작해주세요

    A = np.array([[1, -1, 2],
                  [2, 1, -3],
                  [4, 1, 1]])

    B = np.array([[3, -1, -2],
                  [-4, 2, 1],
                  [1, 4, -3]])

    C = A + B
    print("A + B:")
    print(C)

    D = np.dot(A, B)  # A x B
    D_T = D.T  # 전치
    print("\n(A x B)^T:")
    print(D_T)

    try:
        D_inv = np.linalg.inv(D)  # 역행렬
        print("\n(A x B)의 역행렬:")
        print(D_inv)
    except np.linalg.LinAlgError:
        print("\n(A x B)의 역행렬은 존재하지 않습니다.")

    #수행시간 확인 함수입니다. 함수 호출을 지우지 말아주세요
    time_check()


def final_exam(): #기말고사 문제 메뉴 입니다
    
    exam_1()
    exam_2()
    exam_3()
    exam_4()
    exam_5()
    
final_exam()
    
    
