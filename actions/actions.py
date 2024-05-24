# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import sqlite3


class CheckisAvailable(Action):
    def name(self) -> Text:
        return 'action_check_is_available'

    def run(self, dispatch: CollectingDispatcher, domain: Dict[Text, Any]) -> List[SlotSet]:
        return [SlotSet('isAvailable', True)]


class SaveBooking(Action):
    def name(self) -> Text:
        return 'action_save_booking'

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any], ) -> List[
        Dict[Text, Any]]:
        conn = sqlite3.connect('rasa.db')
        cursor = conn.cursor()

        booking_name = tracker.get_slot('slot_name')
        booking_date = tracker.get_slot('slot_date')
        booking_time = tracker.get_slot('slot_time')
        nb_people = tracker.get_slot('slot_nb_people')
        nb_phone = tracker.get_slot('slot_phone_number')

        cursor.execute('''insert into booking (booking_name, booking_date, booking_time, nb_people, nb_phone)
        values (?,?,?,?,?)''', (booking_name,booking_date,booking_time,nb_people,nb_phone))
        cursor.execute('''select last_insert_rowid()''')

        id = cursor.fetchall();
        print(id)