import os.path
import csv
from post import Post

file_path = "C:\\Users\\mycom\\Documents\\dev\\TIL\\python_study\\" \
            "fastcampus\\Mini_PJT_blog\\data.csv"

# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # 파일 생성하기
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()


# 게시글 쓰기
def write_post():
    """게시글 쓰기"""
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력해 주세요\n>>")
    content = input("내용을 입력해 주세요\n>>")
    # 글번호
    ids = post_list[-1].get_ids() + 1
    post = Post(ids, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")


# 게시글 목록
def list_post():
    """게시글 목록"""
    print("\n\n- 게시글 목록 -")
    ids_list = []
    for post in post_list:
        print("번호 :", post.get_ids())
        print("제목 :", post.get_title())
        print("조회수 :", post.get_view_count())
        print("")
        ids_list.append(post.get_ids())

    while True:
        print("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            ids = int(input(">> "))
            if ids in ids_list:
                detail_post(ids)
                break
            elif ids == -1:
                break
            else:
                print("없는 글 번호 입니다.")
        except ValueError:
            print("숫자를 입력해 주세요")


# 글 상세
def detail_post(ids):
    """게시글 상세 보기 함수"""
    print("\n\n- 게시글 상세 -")

    for post in post_list:
        if post.get_ids() == ids:
            # 조회수 1증가
            post.add_view_count()
            print("번호 :", post.get_ids())
            print("제목 :", post.get_title())
            print("본문 :", post.get_content())
            print("조회수 :", post.get_view_count())
            target_post = post

    while True:
        print("Q) 수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력해주세요")
        try:
            choice = int(input(">> "))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")


# 게시글 수정
def update_post(target_post):
    """게시글 수정 함수"""
    print("\n\n- 게시글 수정 -")
    title = input("제목을 입력해 주세요\n>> ")
    content = input("본문을 입력해 주세요\n>> ")
    target_post.set_post(target_post.ids, title, content, target_post.view_count)
    print("# 게시글 수정되었습니다.")


# 게시글 삭제
def delete_post(target_post):
    """게시글 삭제 함수"""
    post_list.remove(target_post)
    print("# 게시글이 삭제되었습니다.")


# 게시글 저장
def save():
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_ids(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("저장이 완료 되었습니다.")
    print("#프로그램 종료")


# 메뉴 출력하기
while True:
    print("\n\n- FASTCAMPUS BLOG -")
    print("- 메뉴를 선택해 주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">> "))
    except ValueError:
        print("숫자를 입력해 주세요")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            save()
            break
