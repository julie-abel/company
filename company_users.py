class User:

    def __init__(self, user_id: int, name: str, access_level: str = 'user'):

        self.user_id = user_id  # Присваивание ID
        self.name = name  # Присваивание имени
        self.access_level = access_level  # Уровень доступа ('user' для обычных сотрудников)

    def __str__(self):

        return f"User(ID: {self.user_id}, Name: {self.name}, Access: {self.access_level})"

    def get_info(self):
        return {
            'ID': self.user_id,
            'Name': self.name,
            'Access Level': self.access_level
        }

class Admin(User):
    """
    наследуется от User.
    """

    def __init__(self, user_id: int, name: str):

        super().__init__(user_id, name, access_level='admin')  # Администратор получает уровень доступа 'admin'

    def add_user(self, user_list: list, user: User):

        user_list.append(user)
        print(f"Пользователь {user.name} (ID: {user.user_id}) добавлен.")

    def remove_user(self, user_list: list, user_id: int):

        for user in user_list:
            if user.user_id == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.name} (ID: {user_id}) удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")
