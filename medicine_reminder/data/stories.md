## affirm availability
* intent_affirm
  - action_ask_availability
* intent_affirm 
    - form_questions
    - form{"name": "form_questions"}
    - form{"name": null}
    - action_notify

## deny availability
* intent_affirm
  - action_ask_availability
* intent_deny 
  - action_notify

## deny availability
* intent_affirm
  - action_ask_availability
* deny_medicine 
  - action_notify