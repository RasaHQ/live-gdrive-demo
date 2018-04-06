from rasa_core.actions import Action


class ActionExample(Action):

    def name(self):
        return "action_example"

    def run(self, dispatcher, tracker, domain):
        # do stuff
        return []
