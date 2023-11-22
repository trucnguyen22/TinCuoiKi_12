from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import argparse

class GoogleFormGenerator:
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/forms.body"]
        self.DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
        self.creds = None
        # ========================
        self.store = file.Storage('assets/data/token.json')
        self.client_secret = "assets/data/keyGoogleFrom.json"
        # ========================
        self.form_service = None
        self.form_id = None
        self.description = """
        
        Form này được tạo bảo blong đẹp trai không được cãi
        Cảm ơn bạn vì đã sử dụng tool của mình
        I <3 U
        ================
        """
        # ========================
        self.required = True
        self.shuffle = True
        
        
                
    def authenticate(self):
        if not self.creds or self.creds.invalid:
            flow = client.flow_from_clientsecrets(self.client_secret, self.SCOPES)
            self.creds = tools.run_flow(flow, self.store)
            self.form_service = discovery.build('forms', 'v1', http=self.creds.authorize(Http()), discoveryServiceUrl=self.DISCOVERY_DOC, static_discovery=False)

    def setting_configure(self, is_quiz = True, is_required = True, is_shuffle = True):
        self.quiz = is_quiz
        self.required = is_required
        self.shuffle = is_shuffle
        update = {"requests": [
            {
                "updateSettings": {
                    "settings": {
                        "quizSettings": {
                            "isQuiz": self.quiz
                        },
                    },
                    "updateMask": "quizSettings.isQuiz"
                }
            }
        ]}
        self.update_google_form(update)


    def update_google_form(self, json_data):
        try:
            self.form_service.forms().batchUpdate(formId=self.form_id["formId"], body=json_data).execute()
        except Exception as e:
            print(f"Error updating Google Form: {str(e)}")

    def convert_to_format(self, data):
        update = {
            "requests": [{
                "createItem": {
                    "item": {
                        "title": data["title"],
                        "questionItem": {
                            "question": {
                                "required": self.required,
                                "grading": {
                                    "pointValue": 1,
                                    "correctAnswers": {
                                        "answers": data["right_answers"],
                                    },
                                    "whenRight": {"text": "You got it!"},
                                    "whenWrong": {"text": "Sorry, that's wrong"}
                                },
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": data["answers"],
                                    'shuffle': self.shuffle
                                }
                            }
                        }
                    },
                    "location": {
                        "index": data["index"]
                    }         
                }   
            }]
        }
        self.update_google_form(update)
        # return update
    
    
    def read_data_from_json(self, file_data):
        index = -1
        format_data = {
            "title": [],
            "answer": [],
            "right_answer": [],
        }
        for data in file_data:
            index += 1
            format_data = {
                "title": data["question"],
                "answers": data["answer"],
                "right_answers": data["right_answer"],
                "index": index,
            }
            self.convert_to_format(format_data)      

    def create_google_form(self, form_title, form_description, form_documentTitle):
        try:
            form  = {
                "info": {
                    "title": form_title,
                    "documentTitle": form_documentTitle
                }
            }
            self.form_id = self.form_service.forms().create(body=form).execute()
            update = {
                "requests": [
                    {
                        "updateFormInfo": {
                            "info": {
                                "description": self.description + form_description
                            },
                            "updateMask": "description"
                        },
                    },
                ]
            }
            self.update_google_form(update)
        except Exception as e:
            print(f"Error creating Google Form: {str(e)}")
            return None
    def get_link_form(self):
        form_id = self.form_id['formId']
        return f"https://docs.google.com/forms/d/{form_id}"