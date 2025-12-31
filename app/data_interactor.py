from pymongo import MongoClient


class DataInteractor:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['PhonebookDB']
        self.collection = db['contacts']

    def create_contact(self, contact_data: dict):
        if self.collection.find_one({"phone_number": contact_data['phone_number']}):
            return "The phone number already exist"
        doc = self.collection.insert_one(contact_data)
        return f"Inserted ID: {doc.inserted_id}"


    def get_all_contacts(self):
        contacts = self.collection.find({}, {"_id":0})
        contacts_list = list(contacts)
        print(contacts_list)
        return contacts_list

    def update_contact(self, phone_number: str, contact_data: dict):
        result = self.collection.update_one(
            {"phone_number": phone_number},
            {"$set": contact_data}
        )
        return True

    def delete_contact(self, phone_number):
        self.collection.delete_one({"phone_number": phone_number})
        return True