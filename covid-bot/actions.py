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


def appoint_doctor(current_time):
    if '01:00:00' < current_time<='05:00:00':
        return "Dr. Arman Malik"
    elif '05:00:00' < current_time<='09:00:00':
        return "Dr. Anjali Choudhary"
    elif '09:00:00' < current_time<='13:00:00':
        return "Dr. Riddima Jennifer"
    elif '13:00:00' < current_time<='17:00:00':
        return "Dr. Naveen Reddy"
    elif '17:00:00' < current_time<='21:00:00':
        return "Dr. Suvreen Lewis"
    else:
        return "Dr. Hiralal J"

#   - action_ask_help
#   - action_ask_travel
#   - action_ask_travel_when
#   - action_utter_coldCough
#   - action_ask_cough_when
#   - action_utter_fever
#   - action_ask_fever_when
#   - action_utter_breathingProblem
#   - action_ask_breathing_when
#   - action_schedule_appointment


class ActionAskHelp(Action):

    def name(self) -> Text:
        return "action_ask_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_help"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAskTravel(Action):

    def name(self) -> Text:
        return "action_ask_travel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_travel"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAsk_travel_when(Action):

    def name(self) -> Text:
        return "action_ask_travel_when"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_travel_when"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]


class ActionColdCough(Action):

    def name(self) -> Text:
        return "action_utter_coldCough"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_coldCough"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAskWhenCough(Action):

    def name(self) -> Text:
        return "action_ask_cough_when"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_cough_when"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAsk_Fever(Action):

    def name(self) -> Text:
        return "action_utter_fever"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_fever"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]


class ActionAsk_fever_when(Action):

    def name(self) -> Text:
        return "action_ask_fever_when"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_fever_when"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]


class ActionBreathingProb(Action):

    def name(self) -> Text:
        return "action_utter_breathingProblem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_breathingProblem"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAskFromWhenBreathing(Action):

    def name(self) -> Text:
        return "action_ask_breathing_when"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["ask_breathing_when"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

class ActionAppointment(Action):

    def name(self) -> Text:
        return "action_schedule_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.now(IST)

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        doctor_name = appoint_doctor(current_time)

        a = templates["utter_schedule_appointment"].replace("doctor_name",doctor_name)

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

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
