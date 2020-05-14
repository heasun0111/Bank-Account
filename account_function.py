
account_number = []
account_name = []
account_deposit = []

"""
def Integer_check(Number_check):
    if (Number_check.isdigit() != True):
        print("**잘못 입력하셨습니다**")
"""
class Account_function():

    def Deposit_money(self):
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

    def Withdraw_money(self):
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


    def Making_account(self):
        print("======계좌개설======")
        Number_check = input("계좌번호:")
        if( Number_check.isdigit() != True ):
            print("**잘못 입력하셨습니다**")

        else:
            Number = int(Number_check)
            if( Number in account_number ):
                print("**이미 생성된 계좌번호입니다.**")

            else :
                account_number.append(Number)

                Name = str(input("이름:"))
                account_name.append(Name)

                Deposit = int(input("예금:"))
                account_deposit.append(Deposit)

                print("""##계좌개설을 완료하였습니다##
                ===================""")

    def Checking_account(self):
        print("======전체조회=====")
        for i in range(len(account_number)):
            print("계좌번호:",account_number[i],"/ 이름:",account_name[i],"/ 잔액:",account_deposit[i],"원")

        print("===================")
