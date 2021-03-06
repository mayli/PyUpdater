#Welcome to PyUpdater


##What is PyUpdater?

An autoupdate framework for pyinstaller that enables simple, secure & efficient shipment of app updates.

## Status

[![](https://badge.fury.io/py/PyUpdater.svg)](http://badge.fury.io/py/PyUpdater)
[![Build Status](https://travis-ci.org/JMSwag/PyUpdater.svg?branch=master)](https://travis-ci.org/JMSwag/PyUpdater)
[![Build status](https://ci.appveyor.com/api/projects/status/6kex9r8i2625pw9u/branch/master?svg=true)](https://ci.appveyor.com/project/JMSwag/pyupdater/branch/master)
[![](https://requires.io/github/JMSwag/PyUpdater/requirements.svg?branch=master)](https://requires.io/github/JMSwag/PyUpdater/requirements/?branch=master)
[![Code Health](https://landscape.io/github/JMSwag/PyUpdater/master/landscape.svg?style=flat)](https://landscape.io/github/JMSwag/PyUpdater/master)
[![Coverage Status](https://coveralls.io/repos/github/JMSwag/PyUpdater/badge.svg?branch=master)](https://coveralls.io/github/JMSwag/PyUpdater?branch=master)
[![Gitter](https://badges.gitter.im/pyupdater/Lobby.svg)](https://gitter.im/pyupdater/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

##Features

- Easy Setup
- Secured with EdDSA
- Secure off line update
- Release channels
- Automatic generation & application of patch updates
- Smart patch updates
    - This method is only applied if the total size of patches is less than a full update.
- Asynchronous downloads
- Update your application's assets.
    - A bundled copy of ffmpeg for example
- Dual key verification
    - If the repository key is compromised it is very easy to create a new one.
- Get download progress with progress hooks a.k.a. callbacks
    - Great for GUI applications.
    - Super easy setup
- Upload system based on a plugin architecture
- I really feel like I'm missing something else


##Limitations

* No Pyinstaller onedir support