<!-- ## happy path affirm payment
* affirm
  - action_ask_emi
* affirm 
  - action_ask_online
* affirm OR Online
  - action_send_sms 
    -->

## affirm all + 
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* affirm
  - action_ask_travel_when
* period
  - action_utter_coldCough
* affirm
  - action_ask_cough_when
* period
  - action_utter_fever
* affirm
  - action_ask_fever_when
* period
  - action_utter_breathingProblem
* affirm
  - action_ask_breathing_when
* period
  - action_schedule_appointment

## affirm traveled recently+ fever + cough
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* affirm
  - action_ask_travel_when
* period
  - action_utter_coldCough
* affirm
  - action_ask_cough_when
* period
  - action_utter_fever
* affirm
  - action_ask_fever_when
* period
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment


## affirm traveled recently+ no fever + cough
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* period
  - action_ask_travel_when
* affirm
  - action_utter_coldCough
* affirm
  - action_ask_cough_when
* period
  - action_utter_fever
* deny
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment

## affirm traveled recently+ no fever + no cough
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* affirm
  - action_ask_travel_when
* period
  - action_utter_coldCough
* deny
  - action_utter_fever
* deny
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment

## deny traveled recently+ no fever + no cough
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* affirm
  - action_ask_travel_when
* period
  - action_utter_coldCough
* deny
  - action_utter_fever
* deny
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment

## affirm only fever symptom
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* deny
  - action_utter_coldCough
* deny
  - action_utter_fever
* affirm
  - action_ask_fever_when
* period
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment

## affirm only breathing symptom
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* deny
  - action_utter_coldCough
* deny
  - action_utter_fever
* deny
  - action_utter_breathingProblem
* affirm
  - action_schedule_appointment

## affirm only cough symptom
* affirm
  - action_ask_help
* affirm 
  - action_ask_travel
* deny
  - action_utter_coldCough
* affirm
  - action_ask_cough_when
* period
  - action_utter_fever
* deny
  - action_utter_breathingProblem
* deny
  - action_schedule_appointment