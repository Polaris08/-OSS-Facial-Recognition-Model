from new_account import *
from setting import *
from delete_account import *
from modify_account import *

while True:
    print("===================================================================================")
    print("얼굴인식 자동실행 시스템에 오신 것을 환영합니다. 원하시는 기능을 입력해 주세요.")
    print("===================================================================================")
    print("1. 신규 계정 생성\n2. 기존 계정 수정\n3. 계정 세팅 모드\n4. 계정 삭제 모드\n5. 종료")
    print("===================================================================================")
    choice = int(input(">>"))
    
    if choice == 1:
        new_account()
    elif choice == 2:
        mod_face()
    elif choice == 3:
        user = input("유저 이름을 입력해주세요 : ")
        select_tasks(user)
    elif choice == 4:
        del_face()
    elif choice == 5:
        break
    else:
        print("등록되지 않은 선택지입니다.")
