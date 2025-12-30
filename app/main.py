from fastapi import FastAPI
from pydantic import BaseModel
from data_interactor import DataInteractor

class Contact:

    def __init__(self, id, first_name, last_name, phone_number):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


    def convert_to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }

class Item(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


app = FastAPI()

@app.get("/contacts")
def get_contacts():
    db = DataInteractor()
    return db.get_all_contacts()



@app.post("/contacts")
def create_contact_API(item: Item):
    return


@app.put("/contacts/{id}")
def update_contact_API(id: int, item: Item):
    contact_dict = {'first_name': item.first_name, 'last_name': item.last_name, 'phone_number': item.phone_number}
    return


# @app.delete("/contacts/{id}")
# def delete_contact_API(id: int):
#     return