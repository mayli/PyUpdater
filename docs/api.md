# API



## Table of contents

### [pyupdater.client](#pyupdaterclient)

* [pyupdater.client.AppUpdate](#pyupdaterclientappupdate)
* [pyupdater.client.Client](#pyupdaterclientclient)
* [pyupdater.client.LibUpdate](#pyupdaterclientlibupdate)




## pyupdater.client



### pyupdater.client.AppUpdate

Used to update an application. This object is returned by
pyupdater.client.Client.update_check

Args:

data (dict): Info dict

#### Methods

##### AppUpdate.cleanup()

Cleans up old update archives for this app or asset

##### AppUpdate.download(async=False)

Downloads update

######Args:

async (bool): Perform download in background thread

##### AppUpdate.extract()

Will extract the update from its archive to the update folder.
If updating a lib you can take over from there. If updating
an app this call should be followed by method "restart" to
complete update.

######Returns:

(bool) True - Extract successful. False - Extract failed.

##### AppUpdate.extract_overwrite()

Will extract the update then overwrite the current binary

##### AppUpdate.extract_restart()

Will extract the update, overwrite the current binary,
then restart the application using the updated binary.

##### AppUpdate.is_downloaded()

Used to check if update has been downloaded.

######Returns (bool): True - File is already downloaded.
False - File hasn't been downloaded.

##### AppUpdate.restart()

Will overwrite old binary with updated binary and
restart the application using the updated binary.
Not supported on windows.

Deprecated: Used extract_restart instead.

##### AppUpdate.win_extract_overwrite()

Overwrite current binary with update bianry on windows.

Deprecated: Use extract_overwrite instead.

### pyupdater.client.Client

Used to check for updates & returns an updateobject if there is an update.

######Kwargs:

obj (instance): config object

refresh (bool): True - Refresh update manifest on object initialization.
False - Don't refresh update manifest on object initialization

progress_hooks (list): List of callbacks

######Returns:

(obj): AppUpdate or LibUpdate

#### Methods

##### Client.add_progress_hook(cb)

Add a download progress callback function to the list of progress
hooks.

total:  Total size of the file to download

downloaded: The amount of bytes that have been downloaded so far.

percent_complete: The percentage downloaded so far

status: Status of download

Args:

cb (function): Function which takes a dict as its first argument

##### Client.init_app(obj, refresh=False, test=False)

Sets up client with config values from obj

######Args:

obj (instance): config object

######Kwargs:

refresh (bool) Meaning: True - Refresh update manifest on object
initialization. False - Don't refresh update manifest on object
initialization

##### Client.refresh()

Will download and verify the version manifest.

##### Client.update_check(name, version, channel=u'stable')

Checks for available updates

######Args:

name (str): Name of file to update

version (str): Current version number of file to update

channel (str): Release channel

######Returns:

(updateobject) Meanings:

AppUpdate - Used to update current binary

LibUpdate - Used to update external assets

None - No Updates available

### pyupdater.client.LibUpdate

Used to update library files used by an application. This object is
returned by pyupdater.client.Client.update_check

######Args:

data (dict): Info dict

#### Methods

##### LibUpdate.cleanup()

Cleans up old update archives for this app or asset

##### LibUpdate.download(async=False)

Downloads update

######Args:

async (bool): Perform download in background thread

##### LibUpdate.extract()

Will extract the update from its archive to the update folder.
If updating a lib you can take over from there. If updating
an app this call should be followed by method "restart" to
complete update.

######Returns:

(bool) True - Extract successful. False - Extract failed.

##### LibUpdate.is_downloaded()

Used to check if update has been downloaded.

######Returns (bool): True - File is already downloaded.
False - File hasn't been downloaded.

