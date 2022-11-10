from mycroft import MycroftSkill, intent_file_handler


class MycroftTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.mycroft.intent')
    def handle_test_mycroft(self, message):
        intensity = ''
        intensity = self.settings.get('my_selected_option')
        

        self.speak_dialog('test.mycroft', data={
            'intensity': intensity
        })


def create_skill():
    return MycroftTest()

