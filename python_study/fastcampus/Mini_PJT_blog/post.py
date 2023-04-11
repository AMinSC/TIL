class Post:
    """
        게시물 클래스
        param ids: 글번호
        param title: 글제목
        param content: 글내용
        param view_count: 조회수
    """
    def __init__(self, ids, title, content, view_count):
        self.ids = ids
        self.title = title
        self.content = content
        self.view_count = view_count

    def set_post(self, ids, title, content, view_count):
        self.ids = ids
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1

    def get_ids(self):
        return self.ids

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count


if __name__ == "__main__":
    post = Post(1, "테스트", "테스트입니다.", 0)
    # post.set_post(1, "테스트2", "테스트입니다2", 0)
    post.add_view_count()

    print(f"{post.get_ids()} {post.get_title()} {post.get_content()} {post.get_view_count()}")
