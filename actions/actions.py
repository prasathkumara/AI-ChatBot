# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pymongo import MongoClient

# mongodb connection (dashboard clients)
client = MongoClient("mongodb+srv://cynnent:cynnent123@cluster0.0ybxpvk.mongodb.net")
print("MongoDB Connected:", client.server_info())
db = client['alex-chatbot']
collection = db['offers']

# Actions
class clientOffers(Action):
    def name(self) -> Text:
        return "action_get_offers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        query = {"clientName" : "Appland"}
        findOffers = collection.find_one(query)
        print("offers",findOffers)
        if findOffers and "offers" in findOffers:
            products =[]
            for offer in findOffers["offers"]:
                if "offer" in offer and "link" in offer:
                    product = {
                        "name": offer["offer"],
                        "link": offer["link"]
                    }
                    products.append(product)
            
            # Send a message in the required structure
            response = {
                "text": "Here are the current offers:",
                "products": products
            }
            dispatcher.utter_message(json_message=response)

        else:
            dispatcher.utter_message(text="No offers found for Appland.")

        return []


class ActionShowSlotValues(Action):
    def name(self) -> Text:
        return "action_show_slot_values"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Access slot values
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        
        print(f"Name: {name}")
        print(f"Email: {email}")

        dispatcher.utter_message(text=f"Your name is {name} and your email is {email}.\n\n Thank you for providing your details")
        
        return []

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot('name')
        if name:
            dispatcher.utter_message(template="utter_greet_known", name=name)
        else:
            dispatcher.utter_message(template="utter_greet")
        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
