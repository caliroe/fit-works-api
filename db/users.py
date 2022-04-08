import pymongo

from pymongo import errors
from settings.configurations import DefaultConfig
from schemas.sign_up import UserSignUp
from schemas.auth import UserInDB


config = DefaultConfig()


class DataBase:
    """
    Only an IP address you add to your Access List will be able to 
    connect to your project's clusters. You can manage existing IP 
    entries via the Network Access Page.
    """

    def __init__(self, data_base = config.DATABASE_NAME) -> None:
        self.users_collection = 'users_data'
        self.data_base = data_base
        self.client = None
        
        try:
            CONNECTION_DB = f"mongodb+srv://{config.CLUSTER_USERNAME}:{config.CLUSTER_PASSWORD}@fitworksusers.ljd2v.mongodb.net/{data_base}?retryWrites=true&w=majority"
            self.client = pymongo.MongoClient(CONNECTION_DB)
        
        except errors.ConnectionFailure:
            raise errors.ConnectionFailure(
                message='Error connect to MongoDB'
            )    

    def get_user(self, username):
        users_list = self.client[self.data_base][self.users_collection].find()
        user_data = [user[username] for user in users_list if list(user.keys())[1] == username]
        
        if user_data:
            user_data = user_data.pop()
            user_data.update({"username": username})
            return UserInDB(**user_data)
        
        return None

    def insert_one(self, user_data: UserSignUp):
        try: 
            data = {user_data.username: user_data.dict()}
            _ = self.client[self.data_base][self.users_collection].insert_one(data)
        
        except Exception as error:
            print(f"Error on insert_one DataBase. Error message: {error}")
            return False

        else:
            return True
