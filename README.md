Mentor
======

A simple file sharing app over HTTP (for the HTTPS version, see https://github.com/fim/mentor)

Simply provide a list of files and directories to share and they will be
shared without the need for any webserver or any extra configuration. Manual port forwarding is required if desired.

Requirements
------------

 * Python (2.7 tested)
 * gevent

Installation
------------

```sh
$ pip install git+git://github.com/fim/mentor.git
```

Usage
-----

 * Share specific files

```sh
$ mentor file1 file2
```

* Share specific files over HTTPS

```sh
$ mentor -s file1 file2
```

* Share specific files and folders recursively with UPnP hole punching

```sh
$ mentor -u -r dir1 file1 file2
```
