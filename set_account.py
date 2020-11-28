#모든 user 매개변수는 string

import os
from tkinter import *
from tkinter import filedialog

# (pin 바꾸고자 하는 user이름, 새로운 pin)
# users/user/pin.txt에 등록된 pin번호를 바꿔줌
def change_pin(user, pin):
    f = open(user + "/pin.txt", "w")
    f.write(pin)
    f.close()

# (유저 이름)
# user의 task를 리스트로 한줄한줄 읽어온 다음 그 리스트를 리턴
def read_tasks(user):
    f = open(user + "/tasks.txt", "r")
    l = f.readlines();
    return l

# (유저 이름, 설정할 작업 리스트)
# tasks.txt파일의 처음부터 tasks 리스트의 목록을 덮어씌움.
# 설정한 tasks의 리스트를 리턴
def set_tasks(user, tasks):
    f = open(user + "/tasks.txt", "w")
    for t in tasks:
        f.write(t + "\n")
    f.close()
    return tasks

# (유저이름, 설정할 작업 리스트)
# tasks.txt파일에 중복 없이 새 tasks를 추가
# 새로 설정한 tasks의 리스트를 리턴
def add_tasks(user, tasks):
    if os.path.exists(user + "/tasks.txt"):
        list = []
        with open(user + "/tasks.txt") as f:
            for t in tasks:
                if t not in f.read():
                    list.append(t)
                    print(t)
                f.seek(0)
        f.close()
        f = open(user + "/tasks.txt", "a")
        for l in list:
            f.write(l + "\n")
        f.close()

        return list

    else:
        return set_tasks(user, tasks)

# (유저이름, 작업 리스트)
# tasks.txt 에 있는 task들 중에서 tasks리스트에 있는 경우 삭제턴
# 삭제한 tasks 리스트를 리턴
def delete_tasks(user, tasks):
    templist = read_tasks(user)
    olist = newline_delete(templist) #리스트의 문자열 요소의 공백문자 제거
    oset = set(olist)
    tset = set(tasks)
    nset = oset - tset
    nlist = list(nset)
    set_tasks(user, nlist)
    return list(tset)

# 파일 관리자를 불러들여서 파일을 선택
# 파일 절대경로를 리턴
def select_task_file():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/home", title="choose your file",
                                               filetypes=(("txt files", "*.txt"),("all files", "*")))
    root.withdraw()
    sys.stdout.flush()
    return root.filename

# 파일 관리자를 불러들여서 디렉토리를 선택
# 디렉토리 절대경로를 리턴
def select_task_directory():
    dirname = filedialog.askdirectory()
    sys.stdout.flush()
    return dirname

# (리스트)
# 리스트의 목록에 있는 문자열의 뉴라인 문자를 제거
# 뉴라인이 제거된 리스트를 리턴
def newline_delete(list):
    newlist = [tlist.rstrip() for tlist in list]
    return newlist

# (유저, task list)
# task폴더에 심볼릭 링크를 생
def tasks_to_symbolic(user, list):
    newlist = newline_delete(list)
    if not os.path.exists(user + "/task/"):
        os.mkdir(user + "/task/")
    for i in newlist:
        head, tail = os.path.split(i)
        os.symlink(i, user + "/task/" + tail)

# (유저)
# 작업들을 실행할 수 있는 옵션 메뉴 띄워줌
def select_option(user):
    while True:
        print("\033[34m" + "================= main menu ==================")
        print("select menu")
        print("1. add tasks\n2. delete tasks\n3. exit")
        print("===================================" + "\033[0m")
        menu = int(input(">> "))

        if menu == 1:
            task_list = []
            print("\033[31m" + "\n---------------- add tasks ----------------")
            print("you can add multiple tasks\nselect menu")
            print("1. add task - file\n2. add task - open directory\n3. done" + "\033[0m")
            print("--registered tasks--\n", newline_delete(read_tasks(user)))
            while True:
                add_tasks_num = int(input(">> "))
                if add_tasks_num == 1:
                    task_list.append(select_task_file())
                    print("selected tasks : ", task_list)
                elif add_tasks_num == 2:
                    task_list.append(select_task_directory())
                    print("selected tasks : ", task_list)
                elif add_tasks_num == 3:
                    task_set = set(task_list)
                    task_list = list(task_set)

                    print("added tasks : ",add_tasks(user, task_list))
                    print("whole tasks : ",newline_delete(read_tasks(user)))
                    break;
                else:
                    print("wrong menu\n")

        elif menu == 2:
            if not os.path.exists(user + "/tasks.txt"):
                print("no tasks to delete!")
                continue

            delete_list = []
            print("\033[31m" + "\n---------------- delete tasks ----------------")
            print("you can delete multiple tasks\nselect menu")
            print("1. delete task - file\n2. delete task - directory\n3. done" + "\033[0m")
            print("--registered tasks--\n", newline_delete(read_tasks(user)))
            while True:
                delete_task_num = int(input(">> "))
                if delete_task_num == 1:
                    delete_list.append(select_task_file())
                    print("selected tasks : ", delete_list)
                elif delete_task_num == 2:
                    delete_list.append(select_task_directory())
                    print("selected tasks : ", delete_list)
                elif delete_task_num == 3:
                    delete_set = set(delete_list)
                    delete_list = list(delete_set)
                    print("deleted tasks : ", delete_tasks(user, delete_list))
                    print("whole tasks : ", newline_delete(read_tasks(user)))
                    break;
                else:
                    print("wrong menu\n")

        elif menu == 3:
            tasks_to_symbolic(user, read_tasks(user))
            break

        else:
            print("wrong menu\n")


#만약 오픈할 파일이 .desktop이라면 gtk-launch
#만약 오픈할 파일이 텍스트라면 gedit