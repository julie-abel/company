class User:

    def __init__(self, user_id: int, name: str, access_level: str = 'user'):

        self.__user_id = user_id  #   ID
        self.__name = name  #   имя
        self.__access_level = access_level  # уровень доступа

    def __str__(self):

        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level})"

    def get_info(self):

        return {
            'ID': self.__user_id,
            'Name': self.__name,
            'Access Level': self.__access_level
        }

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_access_level(self):
        return self.__access_level


class Admin(User):

    def __init__(self, user_id: int, name: str):

        super().__init__(user_id, name, access_level='admin')  # Администратор получает уровень доступа 'admin'

    def add_user(self, user_list: list, user: User):

        user_list.append(user)
        print(f"Пользователь {user.get_name()} (ID: {user.get_user_id()}) добавлен.")

    def remove_user(self, user_list: list, user_id: int):

        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} (ID: {user_id}) удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")
