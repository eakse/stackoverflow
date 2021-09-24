import os
import json


def loadUsers(self):
    # Dosya var?
    if os.path.exists("AccInformation.json"):  # True ise......
        with open("AccInformation.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        for user in users:
            newUser = Account(
                user_id=user["user_id"],
                firstName=user["first_name"],
                lastName=user["last_name"],
                email=user["email"],
                username=user["username"],
                password=user["password"],
                accountKEY=user["AccountKEY"],
            )

            self.users.append(newUser)
        print(self.users)
    else:
        print("""'AccInformation' adlı Dosya bulunamadı.""")
