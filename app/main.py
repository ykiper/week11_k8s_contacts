from typing import Optional

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


class UpdateItem(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None


app = FastAPI()

@app.get("/contacts")
def get_contacts():
    db = DataInteractor()
    return db.get_all_contacts()



@app.post("/contacts")
def create_contact_API(item: Item):
    db = DataInteractor()
    return db.create_contact(item.model_dump())


@app.put("/contacts/{phon_number}")
def update_contact_API(phon_number: str, update_item: UpdateItem):
    db = DataInteractor()
    return db.update_contact(phon_number, update_item.model_dump(exclude_unset=True))



@app.delete("/contacts/{Phone_number}")
def delete_contact_API(phone_number: str):
    db = DataInteractor()
    return db.delete_contact(phone_number)