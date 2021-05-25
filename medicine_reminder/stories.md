## deny ath the beginning
* deny
    - action_call_later

## story with wrong number
* wrong_number
    - action_wrong_number

## story with call_later
* call_later
    - action_call_later

## Person Healthy (000) with yes to migration
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* deny
    - action_coldCough
    - action_utter_fever
* deny
    - action_fever
    - action_utter_breathingProblem
* deny
    - action_breathingProblem
    - action_utter_thank


## Person with all symptoms (111)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* affirm
    - action_coldCough
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_coldCough
    - action_utter_fever
* affirm
    - action_fever
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_fever
    - action_utter_breathingProblem
* affirm
    - action_breathingProblem
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_breathingProblem
    - action_utter_thank
* affirm
    - action_breathingProblem
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_breathingProblem
    - action_utter_thank

## Person with breathing disorder (001)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* deny
    - action_coldCough
    - action_utter_fever
* deny
    - action_fever
    - action_utter_breathingProblem
* affirm
    - action_breathingProblem
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_breathingProblem
    - action_utter_thank


## Person with fever (010)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* deny
    - action_coldCough
    - action_utter_fever
* affirm
    - action_fever
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_fever
    - action_utter_breathingProblem
* deny
    - action_breathingProblem
    - action_utter_thank


## Person with fever and breathing problem (011)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* deny
    - action_coldCough
    - action_utter_fever
* affirm
    - action_fever
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_fever
    - action_utter_breathingProblem
* affirm
    - action_breathingProblem
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_breathingProblem
    - action_utter_thank

## Person with cold cough (100)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* affirm
    - action_coldCough
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_coldCough
    - action_utter_fever
* deny
    - action_fever
    - action_utter_breathingProblem
* deny
    - action_breathingProblem
    - action_utter_thank

## Person with cold cough and breathing problem (101)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* affirm
    - action_coldCough
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_coldCough
    - action_utter_fever
* deny
    - action_fever
    - action_utter_breathingProblem
* affirm
    - action_breathingProblem
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_breathingProblem
    - action_utter_thank

## Person with cold cough and fever (110)
* affirm
    - action_ask_loaction
    - action_utter_coldCough
* affirm
    - action_coldCough
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_coldCough
    - action_utter_fever
* affirm
    - action_fever
    - action_utter_numberOfDays
* period
    - slot{"days":"25"}
    - action_fever
    - action_utter_breathingProblem
* deny
    - action_breathingProblem
    - action_utter_thank


## Person Healthy (000) with deny to migration
* deny
    - action_utter_coldCough
* deny
    - action_coldCough
    - action_utter_fever
