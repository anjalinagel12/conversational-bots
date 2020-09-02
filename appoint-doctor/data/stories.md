<!-- ## happy path affirm payment
* affirm
  - action_ask_emi
* affirm 
  - action_ask_online
* affirm OR Online
  - action_send_sms 
    -->


## story with affirm + appoint
* affirm 
    - form_question1
    - form{"name": "form_question1"}
    - form{"name": null}
    - form_question2
    - form{"name": "form_question2"}
    - form{"name": null}
    - form_question3
    - form{"name": "form_question3"}
    - form{"name": null}
    - utter_successful

## story with deny 
* deny 
    - utter_ask_help
* deny
    - utter_

## story with deny 
* deny 
    - utter_bye
* affirm 
    - form_question1
    - form{"name": "form_question1"}
    - form{"name": null}
    - form_question2
    - form{"name": "form_question2"}
    - form{"name": null}
    - form_question3
    - form{"name": "form_question3"}
    - form{"name": null}
    - utter_successful
