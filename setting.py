import set_account
import os

def check_fefault_istrue(str):
    if str == 'y' or str == 'Y':
        return "1"
    elif str == 'n' or str =='N':
        return "0"
    else:
        print("잘못된 입력\n")
        return "false input"

def select_tasks():
    user = input("please input user name: ")
    while True:
        print("================= 세팅 모드 =====================")
        print("1. 기본 프로그램 설정")
        print("2. 사용자설정 바로가기 만들기/삭제")
        print("3. pin번호 변경")
        print("4. 종")
        menu = int(input(">> "))
        if menu == 1:
            print("-------------- 기본 프로그램 설정 ------------------")
            ch = True
            while True:
                ch = check_fefault_istrue(input("리브레 오피스 (y/n) "))
                checkLib = ch
                if ch == "false input":
                    continue
                ch = check_fefault_istrue(input("썬더버드 이메일 (y/n) "))
                checkThu = ch
                if ch == "false input":
                    continue
                ch = check_fefault_istrue(input("파이어폭스 (y/n) "))
                checkFir = ch
                if ch == "false input":
                    continue
                break;

            if checkFir == "1":
                while True:
                    ch = check_fefault_istrue(input("파이어폭스 자동실행 url을 지정하시겠습니까? (y/n) "))
                    if ch == "false input":
                        continue
                    break
                if ch == "0":
                    if not os.path.exists("users/" + user + "/default/"):
                        os.mkdir("users/" + user + "/default/")
                    f = open ("users/" + user + "/default/checklist.txt", "w")
                    f.writelines(checkLib)
                    f.writelines(checkThu)
                    f.writelines(checkFir)
                    f.close()
                elif ch == "1":
                    url = []
                    print("----------------")
                    print("url 입력\n종료 : q 입력")
                    while True:
                        temp = input(">> ")
                        if temp == "q":
                            break;
                        else:
                            url.append(temp)

                    if not os.path.exists("users/" + user + "/default/"):
                        os.mkdir("users/" + user + "/default/")
                    f = open ("users/" + user + "/default/checklist.txt", "w")
                    f.writelines(checkLib)
                    f.writelines(checkThu)
                    f.writelines(checkFir)
                    f.close()

                    d = open("users/" + user + "/default/user_url.txt", "w")
                    for i in url:
                        d.writelines(i)
                    d.close()
            else:
                if not os.path.exists("users/" + user + "/default/"):
                    os.mkdir("users/" + user + "/default/")
                f = open("users/" + user + "/default/checklist.txt", "w")
                f.writelines(checkLib)
                f.writelines(checkThu)
                f.writelines(checkFir)
                f.close()
        elif menu == 2:
            set_account.select_option("users/" + user)
        elif menu == 3:
            print("\n---------------- change pin ----------------")
            pin = input("input new pin >> ")
            set_account.change_pin("users/" + user, pin)
            print("new pin : ", pin)
        elif menu == 4:
            break
        else:
            print("wrong menu\n")


#select_tasks("man")
