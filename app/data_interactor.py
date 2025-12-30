from pymongo import MongoClient


class DataInteractor:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['PhonebookDB']
        self.collection = self.db['contacts']



    def get_all_contacts(self):
        contacts = self.collection.find({}, {"_id":0})
        contacts_list = list(contacts)
        print(contacts_list)
        return contacts_list


