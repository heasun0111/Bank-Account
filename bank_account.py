import account_function

f = account_function.Account_function()

def Bank_menu():
    while (1):
        print('''
        ======Bank Menu======
        1. 계좌개설
        2. 입금하기
        3. 출금하기
        4. 전체조회
        5. 프로그램 종료
        =====================
        ''')
        choice = int(input('입력:'))

        if choice == 1:
            f.Making_account()

        elif choice == 2:
            f.Deposit_money()

        elif choice == 3:
            f.Withdraw_money()

        elif choice == 4:
            f.Checking_account()

        elif choice == 5:
            print("##프로그램을 종료합니다##")
            break

        else:
            print("잘못된 값을 입력하였습니다.")

if __name__=='__main__':
    Bank_menu()
