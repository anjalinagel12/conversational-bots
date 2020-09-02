# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import requests
import re
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from typing import Any, Text, Dict, List, Union, Optional

from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, FollowupAction, UserUtteranceReverted, ActionReverted, Restarted
from rasa_sdk.executor import CollectingDispatcher
import pickle
import datetime
#from sms_api import send_message
from threading import Thread
#from date_valid import validate_date , haptik_date_validation 
from pytz import timezone
#from datetime import datetime

from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata') 

with open("templates.json", "r", encoding="utf-8") as temp:
    templates = json.load(temp)


class ActionFallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        # Checking for 2 fallback, if bot didn't understand final message is uttered.
        bot_msg  = "" 
        count = 0

        templates_temp = {}

        for key,message in templates.items():
            templates_temp[key] = message


        for event in reversed(tracker.events):
            if event.get("event") == "bot":
                #logger.debug("Inside Fallback : text is : "+event.get("text"))
                if templates["utter_fallback"] in event.get("text"):
                    count += 1
                    if count >= 2:
                        dispatcher.utter_message(templates["utter_bot_not_understand"])
                        return [Restarted()]
                        # Call is Ended EOC
                    else:
                        count += 1
                        bot_msg = event.get("text")
                        for template_key,template_message in templates_temp.items():
                            if event.get("text") == template_message:
                                short_key = template_key + "_short"
                                if short_key in templates_temp:
                                    bot_msg = templates_temp[short_key]
                                    break
                                else:
                                    bot_msg = templates_temp[template_key]
                                    break
                        #bot_msg = last_bot_message
                        break
                elif event.get("text") in templates_temp.values():
                    # replace bot message here\
                    
                    bot_msg = event.get("text")
                    #logger.debug(" Bot message in the elif block of fallback is : "+str(bot_msg))
                    for template_key,template_message in templates_temp.items():
                        #logger.debug("Template message in the elif block of fallback is : "+str(template_message))
                        if event.get("text") == template_message:
                            short_key = template_key + "_short"
                            if short_key in templates_temp:
                                bot_msg = templates_temp[short_key]
                                break
                            else:
                                bot_msg = templates_temp[template_key]
                                break
                    break
                else:
                    bot_msg = event.get("text")
                    #logger.debug("Bot message in the else block of fallback is : "+str(bot_msg))
                    for template_key,template_message in templates_temp.items():
                        #logger.debug("Template message in the else block of fallback is : "+str(template_message))
                        if event.get("text") == template_message:
                            short_key = template_key + "_short"
                            if short_key in templates_temp:
                                bot_msg = templates_temp[short_key]
                                break
                            else:
                                bot_msg = templates_temp[template_key]
                                break
                    #bot_msg = last_bot_message
                    count += 1
                    break

        if bot_msg == "":
            dispatcher.utter_message(templates["initial_message"])
        else:
            if templates["utter_fallback"] in bot_msg:
                dispatcher.utter_message(bot_msg)
            else:
                dispatcher.utter_message(templates["utter_fallback"]+ '. ' + bot_msg) 

        return [UserUtteranceReverted()]


# Question Number 1
class FormGetRatingQuestion2(FormAction):
    def name(self) -> Text:
        return "form_question1"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["question1"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "question1": self.from_text(), 
        }

    def validate_question1(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate form_question1"""

        try:

            intent_name = tracker.latest_message['intent']['name']
            if intent_name == "intent_name":
                return {"question1": value}

            else:
                dispatcher.utter_message(templates["utter_question_1"])
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"question1": None}
        except Exception as e:
            print("EXCEPTION here : "+ str(e))

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        return []


# Question Number 2
class FormGetRatingQuestion2(FormAction):
    def name(self) -> Text:
        return "form_question2"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["question2"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "question2": self.from_text(), 
        }

    def validate_question2(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate form_question2"""

        try:

            intent_name = tracker.latest_message['intent']['name']
            if intent_name == "intent_age" :
                return {"question2": value}

            else:
                dispatcher.utter_message(templates["utter_question_2"])
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"question2": None}
        except Exception as e:
            print("EXCEPTION here : "+ str(e))

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        return[]



# Question Number 3
class FormGetRatingQuestion3(FormAction):
    def name(self) -> Text:
        return "form_question3"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["question3"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "question3": self.from_text(),
        }

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []


