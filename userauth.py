from dataclasses import dataclass

@dataclass 

class UserAuth:
    user_name:str
    user_password:str
    user_shop:bool

    def login(self, user_name, user_password):
        pass
    
    


