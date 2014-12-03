#!/usr/bin/env python

from distutils.core import setup
import os
import sys

def datapath(path):
    if not os.path.exists(path):
        if 'REPO' in os.environ:
            path = os.path.join(os.environ['REPO'], path)
    return path

if __name__ == "__main__":
    # Add forceversion option to set the version via the command line
    version = '0.1'
    matchingarg = None
    for arg in sys.argv:
        if '--forceversion=' in arg:
            version = arg.replace('--forceversion=', '')
            matchingarg = arg
    sys.argv[:] = [arg for arg in sys.argv if matchingarg!=arg]

    setup(name='xscontainer',
          version=version,
          description='Container integration for XenServer.',
          author='Citrix Systems Inc., Robert Breker',
          license = "BSD",
          url='http://github.com/xenserver/xscontainer',
          packages=['xscontainer'],
          package_dir = {'xscontainer': 'src/xscontainer'},
          scripts = ['src/xscontainer-monitor', 'src/xscontainer-pluginexample',
                     'src/xscontainer-devsystemtest',],
          data_files = [('/etc/xapi.d/plugins',
                         [datapath('src/etc/xapi.d/plugins/xscontainer')]),
                         ('/etc/init.d',
                         [datapath('src/etc/init.d/xscontainer')])],
    )
