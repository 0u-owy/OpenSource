import math
def main():
    print("----------------------------")
    print("계산기 프로그램 입니다.")
    print("----------------------------")
    while True:

        print("\n사용할 기능을 선택하세요.")
        print("사용할 기능을 선택하세요./종료하려면 quit 입력하세요.")
        
        print("1. 더하기")
        print("2. 빼기")
        print("3. 곱하기")
        print("4. 나누기")
        print("5. 지수")  # 지수 기능 추가
        print("6. 제곱근")  # 제곱근 기능 추가

        choice = input("번호 : ")

        if choice == "quit":
            print("종료")
            break
        elif choice in ["1", "2", "3", "4","5","6"]:
            x = float(input("첫 번째 숫자 입력: "))
            if choice in ["1","2","3","4","5"]: #두번째 숫자가 필요한 경우
                y = float(input("두 번째 숫자 입력: "))
            if choice == "1":
                print("결과:")
            elif choice == "2":
                print("결과:")
            elif choice == "3":
                print("결과: ", x*y)
            elif choice == "4":
                if y != 0:  # 0으로 나누는 경우를 방지
                    print("결과:", x/y)
                else:
                    print("0으로 나눌 수 없습니다.") # 0으로 나누면 오류 메시지
            elif choice == "5":  # 지수 (x^y)
                print("결과:", x ** y)  # x^y 계산
            elif choice == "6":  # 제곱근
                if x >= 0:  # 음수에 대한 제곱근은 계산 불가
                    print("결과:", math.sqrt(x))  # 제곱근 계산
                else:
                    print("음수에 대한 제곱근은 계산할 수 없습니다.")
        else:
            print("잘못된 입력.")


if __name__ == "__main__":
    main()