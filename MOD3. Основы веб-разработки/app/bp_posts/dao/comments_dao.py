import json


class CommentsDAO:

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

    def get_by_post_id(self, post_id: int) -> list[dict]:
        """
        Возвращает комментарии определенного поста.
        """
        comments = self.load_file()
        post_id_comments = []
        for comment in comments:
            if comment['post_id'] == post_id:
                post_id_comments.append(comment)
        if len(post_id_comments) == 0:
            post_id_comments.append({})
        return post_id_comments
