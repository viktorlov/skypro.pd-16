import json


class PostsDAO:

    def __init__(self, path: str):
        """
        При создании экземпляра DAO нужно указать путь к файлу с данными.
        """
        self.path = path

    def load_file(self) -> list[dict]:
        """
        Загружает файл с указанным именем из папки "../data/".
        """
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self) -> list[dict]:
        """
        Возвращает все посты.
        """
        posts = self.load_file()
        return posts

    def get_by_pk(self, pk: int) -> list[dict]:
        """
        Возвращает пост по его идентификатору.
        """
        posts = self.load_file()
        for post in posts:
            if post["pk"] == pk:
                return [post]
        return [{}]

    def get_by_user(self, user_name: str) -> list[dict]:
        """
        Возвращает посты определенного пользователя.
        """
        posts = self.load_file()
        user_posts = []
        for post in posts:
            if post['poster_name'].lower() == user_name.lower():
                user_posts.append(post)
        return user_posts

    def search(self, query: str) -> list[dict]:
        """
        Возвращает список постов по ключевому слову.
        """
        posts_were_found = []
        posts = self.load_file()
        for post in posts:
            if query.lower() in post["content"].lower():
                posts_were_found.append(post)
        return posts_were_found

    def get_by_tag(self, tag: str) -> list[dict]:
        """
        Возвращает список постов по тэгу.
        """
        posts = self.load_file()
        posts_were_found = []
        for post in posts:
            for word in post['content'].split(' '):
                if word.lower() == '#' + tag.lower():
                    posts_were_found.append(post)
        return posts_were_found
