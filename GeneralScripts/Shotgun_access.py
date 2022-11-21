import datetime
import shotgun_api3, json


class User:
    """   A module for the user specifics   """
    id = 0

    def __init__(self, name, psd):
        self._user = name
        self._psd = psd
        User.id += 1
        self.valid_account()

    @property
    def name(self):
        return self._user

    def __str__(self):
        return f"name: {self.name} id:{User.id}"

    def __repr__(self):
        return f"User({self.name}, {len(self._psd)})"

    def valid_account(self):
        if self.name is None or self._psd is None:
            raise AttributeError("Please set your password and user name first !")


class Login:
    """    A main mode for the login related things    """
    def __init__(self, name, psd=None, project_id=0):
        self._shotgun_url = 'https://ea.shotgunstudio.com/'
        self._session_name = name
        self._project_id = project_id
        self._psd = psd
        self._date = datetime.datetime.now()

        """ Do initial process  """
        self.valid_session()
        self.sg = self.connect()

    @property
    def url(self):
        return self._shotgun_url

    @property
    def project_id(self):
        return self._project_id

    @property
    def user_session(self):
        return self._session_name

    @property
    def psd(self):
        return self._psd

    @psd.setter
    def psd(self, new_psd):
        self.reset_psd(new_psd)

    @property
    def timestamp(self):
        return self._date

    def reset_psd(self, new_psd):
        if new_psd == self.psd:
            raise AttributeError("The password is the same!!")
        else:
            self._psd = new_psd

    def connect(self):
        if self.psd is None:
            raise AttributeError("You haven't input an password!!")
        else:
            sg = shotgun_api3.Shotgun(self._shotgun_url, login=self.user_session, password=self.psd)
            # pprint.pprint([symbol for symbol in sorted(dir(sg)) if not symbol.startswith('_')])
            return sg

    def valid_session(self):
        if self.user_session is None or self.project_id == 0:
            raise AttributeError("You haven't input your user or a valid project id!!!")

    def find_project(self):
        asset_list = self.sg.find('Asset', filters=[['project', 'is', {'type': 'Project','id': self.project_id}]])
        """  Put all ids into a list and return it for further steps  """
        final_list = [x['id'] for x in asset_list]
        return final_list

    def find_task_with_id(self, asset_id):
        """
            Example code:
                filters = [['entity', 'is', {'id': asset_id, 'type': 'Asset'}],
            {
                "filter_operator": "any",
                "filters": [
                    ['content', 'contains', ['Whitebox']],
                    ['content', 'contains', ['Placeholder']]
                ]
            }
        ]
        ['entity', 'is', {'id': 74636, 'type': 'Asset'}]
        """
        filters = [
            ['entity', 'is', {'id': asset_id, 'type': 'Asset'}]
        ]
        fields = ['sg_status_list', 'content']

        # result = self.sg.find("Asset", filters=filters, fields=fields)
        task_result = self.sg.find("Task", filters=filters, fields=fields)

        # Check the filtered result
        # for i in task_result:
        #     self.search_keys(i)

        self.write_in_json(task_result)

        return task_result

    def search_keys(self, item):
        target = ['Whitebox', 'Placeholder']
        data_set = set(target)
        items = [(k, v) for k, v in item.items() if v in data_set]
        print(items)
        return items

    def write_in_json(self, obejct):
        with open("d:\\sample.json", "w") as outfile:
            json.dump(obejct, outfile)

    def execution(self):
        asset_list = self.find_project()

        with open(r"d:\myfile.txt", 'w') as f:
            for i in asset_list:
                result = self.find_task_with_id(i)
                #f.write(str(result))


class DatabaseReader:
    """  A database searching interface  """

    @classmethod
    def get_assets(cls, token, project_id):
        return token.sg.find('Asset', filters=[['project', 'is', {'type': 'Project', 'id': project_id}]])

    @classmethod
    def find_task(cls):
        pass


if __name__ == '__main__':
    # Testing code......
    user = User('', '')  # 'james' 'abcd#12345'
    test = Login('wenqiguo', 'xxxx')
    # test.execution()
    #pprint.pprint(test.find_task_with_id(74636))
