from pydantic import UUID4


class BaseLeakyException(Exception):
    def __init__(self):
        self.status_code: int = 400
        self.error: str = "base_error"
        self.description: str = "Неопознанная ошибка"


class UserException(BaseLeakyException):
    def __init__(self):
        self.status_code = 400
        self.error = "user_error"
        self.description = "Ошибка пользователя"


class UserExistsError(UserException):
    def __init__(self, user_id: UUID4):
        self.status_code = 409
        self.error = "user_exists_error"
        self.description = "Пользователь уже существует"

        self.user_id: UUID4 = user_id


class UserDoesNotExistError(UserException):
    def __init__(self, user_id: UUID4):
        self.status_code = 404
        self.error = "user_does_not_exist_error"
        self.description = f"Пользователя {user_id} не существует"
