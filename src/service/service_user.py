from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.busca_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "Registered User"
                else:
                    return "User already exists"
            else:
                return "User must contain only letters"
        else:
            return "Invalid parameters"

    def update_user(self, name, new_job):
        if name is not None and new_job is not None:
            if isinstance(name, str) and isinstance(new_job, str):
                for user in self.store.bd:
                    if user.name == name:
                        user.job = new_job
                        return "Updated User"
                    else:
                        return "User not registered"
            else:
                return "User must contain only letters"
        else:
            return "Invalid parameters"

    def get_user_by_name(self, name):
        if name is not None:
            if isinstance(name, str):
                response = self.busca_user(name)
                if response is not None:
                    return response
                else:
                    return "User not found"
            else:
                return "User must contain only letters"
        else:
            return "Invalid parameters"

    def remove_user(self, name):
        search = self.busca_user(name)
        if search is not None:
            self.store.bd.remove(search)
            return "User Removed Successfully"
        else:
            return "User not found"

    def busca_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None
