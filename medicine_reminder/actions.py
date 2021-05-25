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
from threading import Thread
from pytz import timezone
#from datetime import datetime

from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata') 

with open("templates.json", "r", encoding="utf-8") as temp:
    templates = json.load(temp)


class ActionAskHelp(Action):

    def name(self) -> Text:
        return "action_ask_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        a = templates["utter_ask_availability"]

        dispatcher.utter_message(a)
        return [AllSlotsReset()]

# Questions
class FormQuestions(FormAction):
    def name(self) -> Text:
        return "form_questions"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["question1","question2","question3"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return{"question1": self.from_text(),"question2":self.from_text()}

    def validate_question1(self, value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> Dict[Text, Any]:
        val=tracker.latest_message['text']
        intent_name = tracker.latest_message['intent']['name']
        if intent_name in ['affirm_medicine','intent_affirm','medicine_timing']:
            return {"question1": value}

        elif intent_name in ['deny_medicine','intent_deny']:
            return {"question1": "no","question2": "no","question2": "no"}
        
        else:
            return {"question1": None}


    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
        ) -> Optional[List[EventType]]:
        """Request the next slot and utter template if needed,
            else return None"""

        
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):

                if slot=='question1':
                    message = templates["utter_ask_medicine"]
                    dispatcher.utter_message(text=message)
                    return [SlotSet(REQUESTED_SLOT, slot)]
    
                elif slot=='question2':
                    message = templates["utter_ask_medicine_names"]
                    dispatcher.utter_message(text=message)
                    return [SlotSet(REQUESTED_SLOT, slot)]

                elif slot=='question3':
                    message = templates["utter_ask_timing"]
                    dispatcher.utter_message(text=message)
                    return [SlotSet(REQUESTED_SLOT, slot)]

        # no more required slots to fill
        return None

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        return []




class action_notify(Action):

    def name(self) -> Text:
        return "action_notify"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent_name = tracker.latest_message['intent']['name']
        time = tracker.get_slot('time')

        print("===time to remind= ",str(time))

        if intent_name in ['deny_medicine','intent_deny']:

            a = templates["utter_healthy"]
            dispatcher.utter_message(a)

        else:
            a = templates["utter_will_notify"]
            dispatcher.utter_message(a)

            initiate_background_task(time)

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
