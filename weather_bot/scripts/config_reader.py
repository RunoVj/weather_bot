import os
import yaml

# read authorization parameters from local file
TOKEN = None
API_KEY = None


class ConfigReader:

    def __init__(self):
        self.token = None
        self.api_key = None
        self.__read_param_from_heroku()
        if self.token is None:
            self.__read_param_from_file()
            if self.token is None:
                raise IOError('Cannot read authorization parameters')

    def __read_param_from_heroku(self):
        # read authorization parameters from heroku
        self.token = os.environ.get('TOKEN')
        self.api_key = os.environ.get('API_KEY')

    def __read_param_from_file(self):
        base_dir = '/'.join(os.path.dirname(__file__).split('/')[0:-2])
        filename = base_dir + '/.authorization.yaml'
        with open(filename) as f:
            authorization = yaml.load(f, Loader=yaml.FullLoader)
            self.token = authorization['token']
            self.api_key = authorization['api_key']



