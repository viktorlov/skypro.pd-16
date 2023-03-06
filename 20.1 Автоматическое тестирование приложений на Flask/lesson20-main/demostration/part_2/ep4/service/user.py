from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        return self.dao.update(user_d)

    def partially_update(self, user_d):
        user = self.get_one(user_d["id"])
        if "name" in user_d:
            user.name = user_d.get("name")
        self.dao.update(user)

    def delete(self, rid):
        self.dao.delete(rid)
