import json
from pythonmonkey import require
from commonattributes import Commonattributes

class Commonmethods:

    common_attributes_object: Commonattributes

    def __init__(self, common_attributes_object: Commonattributes):
        self.common_attributes_object = common_attributes_object
        pass

    def readyPages(self, parent):
        from Pages.startpage import Startpage
        from Pages.pageone import Pageone
        from Pages.pagetwo import Pagetwo
        for P in (Startpage, Pageone, Pagetwo):
            page = P(parent, self.common_attributes_object)
            self.common_attributes_object.pages.update({P : page})

    def changePage(self, page):
        page.mainframe.tkraise()

    def parseJSON(self, json_string) -> dict:
        try:
            data = json.loads(json_string)
            return data
        except json.JSONDecodeError as error:
            print(f"Error in JSON parsing: {error}")

    async def parseTest(self):
        try:
            print('Starting parseTest...')
            jsgrabber = require('./jsgrabber')
            print('Successfully got jsgrabber.')
            print('Data type of jsgrabber: ' + str(type(jsgrabber)))
            data = await jsgrabber.findAnItem('/Lotus/Powersuits/Excalibur/ExcaliburPrime')
            print('Successfully got data from findAnItem.')
            print("This is the unparsed data:" + str(data))
            parsed_data = json.loads(data)
            print("This is the parsed data:" + str(parsed_data))
        except Exception as error:
            print('Something went wrong :< - ' + str(error))