
# trantor-ebookdl

**trantor-ebookdl** is a simple python CLI program to download ebooks
in the EPUB format from the
[Imperial Library of Trantor](https://github.com/trantor-library/trantor)

It uses the asynchronous [aiohttp](https://github.com/aio-libs/aiohttp) library
for the web requests and [aiohttp-socks](https://github.com/romis2012/aiohttp-socks)
for the socks connection with TOR.

## Usage

You need to be connected to the Tor network to access the Imperial Library.

Downloading by name:

```sh
trantor-ebookdl --byname python
```

Downloading by subject, no more than 5 ebooks:

```sh
trantor-ebookdl --bysubject rome --max 5
```

Specify the download directory (by default '.'):

```sh
trantor-ebookdl --byname 'james bond' --dstdir $HOME/ebooks
```

Change the default SOCKS host/port parameters:

```sh
trantor-ebookdl --byname rimbaud --sockshost remotehost --socksport 9999 
```

You can use the **-i** flag for interactive mode (it will ask your confirmation
before downloading anything). Use **--help** for full usage list.

## Installation

```sh
python setup.py install
```

## Requirements

* python3 >= 3.5 (async support)
* aiohttp
* aiohttp_socks
