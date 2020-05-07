
account_number = []
account_name = []
account_deposit = []

def Deposit_money():
    print("======입금하기======")

    read_account = int(input("입금하실 계좌번호를 입력해주세요:"))
    if read_account in account_number:
        num = account_number.index(read_account)
        print("계좌이름:",account_name[num])
        print("계좌잔고:",account_deposit[num])

        deposit_money = int(input("입금하실 금액을 입력해주세요:"))
        account_deposit[num] = account_deposit[num] + deposit_money
        print("##계좌잔고:",account_deposit[num],"원##")
        print("##입금이 완료되었습니다##")
        print("===================")
    else :
        print("입력하신 계좌를 조회할 수 없습니다.")

def Withdraw_money():
    print("======출금하기======")

    read_account = int(input("출금하실 계좌번호를 입력해주세요:"))
    if read_account in account_number:
        num = account_number.index(read_account)
        print("계좌이름:",account_name[num])
        print("계좌잔고:",account_deposit[num])

        withdraw_money = int(input("출금하실 금액을 입력해주세요:"))
        account_deposit[num] = account_deposit[num] - withdraw_money
        print("##계좌잔고:",account_deposit[num],"원##")
        print("##출금이 완료되었습니다##")
        print("===================")
    else :
        print("입력하신 계좌를 조회할 수 없습니다.")


def Making_account():
    print("======계좌개설======")

    Number = int(input("계좌번호:"))
#    if()
    account_number.append(Number)

    Name = str(input("이름:"))
    account_name.append(Name)

    Deposit = int(input("예금:"))
    account_deposit.append(Deposit)

    print("""##계좌개설을 완료하였습니다##
    ===================""")

def Checking_account():
    print("======전체조회=====")
    for i in range(len(account_number)):
        print("계좌번호:",account_number[i],"/ 이름:",account_name[i],"/ 잔액:",account_deposit[i],"원")


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
            print("계좌개설 실행")
            Making_account()

        elif choice == 2:
            print("입금하기 실행")
            Deposit_money()

        elif choice == 3:
            print("출금하기 실행")
            Withdraw_money()

        elif choice == 4:
            print("전체조회 실행")
            Checking_account()

        elif choice == 5:
            print("##프로그램을 종료합니다##")
            break

        else:
            print("잘못된 값을 입력하였습니다.")

if __name__=='__main__':
    Bank_menu()