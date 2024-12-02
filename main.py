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

        choice = input("번호 : ")

        if choice == "quit":
            print("종료")
            break
        elif choice in ["1", "2", "3", "4"]:
            x = float(input("첫 번째 숫자 입력: "))
            y = float(input("두 번째 숫자 입력: "))
            if choice == 1:
                print("결과:")
            elif choice == 2:
                print("결과:")
            elif choice == 3:
                print("결과: ", x*y)
            elif choice == 4:
                print("결과:")
        else:
            print("잘못된 입력.")


if __name__ == "__main__":
    main()