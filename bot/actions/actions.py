
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

accountdb={
    12345678900001:{
        'name': 'samriddha',
        'phone':'9868849124',
        'balance':'Rs. 10,000'
    },
     12345678900002:{
        'name': 'rohan singh',
        'phone':'9868849125',
        'balance':'Rs. 10,000'
    }
}

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_account_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name= tracker.get_slot('name')
        phone= tracker.get_slot('phone_number')
        account_number= tracker.get_slot('account_number')
        print(name, phone, account_number)
        account_number=int(account_number)
        print(type(account_number))
        print(type(name))
        if account_number in accountdb:
       
            if accountdb[account_number]['name']==name and accountdb[account_number]['phone']==phone:
           
                balance=accountdb[account_number]['balance']
                message="Dear customer {}  your account number {} has balance {}".format(name,account_number,balance)
                dispatcher.utter_message(text=message)
            else:
                message="Please enter some of your valid account credentials correctly"
                dispatcher.utter_message(text=message)
        else:
            message='Please enter your detail correctly'
            dispatcher.utter_message(text=message)

        return []
