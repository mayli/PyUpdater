#Create Upload Plugins

- Plugins are enabled on installation
- Plugins authors can get config info from the user. (Optional)
- Plugin configs are saved by PyUpdater

##Example
####my_uploader.py
```

from pyupdater.uploader import BaseUploader


class MyUploader(BaseUploader):

    name = 'my uploader'
    author = 'Jane Doe'

    def init_config(config):
        "Pyupdater will call this function when setting the uploader"
        # config (dict): a dict with settings specific to this plugin

    def set_config(config):
        "PyUpdater will call this function when user selects this plugin in settings"
        # config (dict): a dict with settings specific to this plugin

    def upload_file(self, filename):
        "PyUpdater will call this function on every file that needs to be uploaded."
        # filename (str): Absolute path to the file
```


####In your setup.py
```
setup(
    provides=['pyupdater.plugins',],
    entry_points={
        'pyupdater.plugins': [
            'my_uploader = my_uploader:MyUploader',
            ]
        },
```

##Plugin Settings
Plugin authors have 2 ways of getting config information from users.  The first would be env var. The second would be requesting information from users by calling self.get_answer('Question'). Repo settings override env vars. See the example plugins below.

##Examples plugins
###[S3 Plugin](https://github.com/JMSwag/PyUpdater-S3-Plugin "S3 Plugin")
###[SCP Plugin](https://github.com/JMSwag/PyUpdater-SCP-Plugin "SCP Plugin")