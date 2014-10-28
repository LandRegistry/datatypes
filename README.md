#Datatypes

[![Build Status](https://travis-ci.org/LandRegistry/datatypes.svg)](https://travis-ci.org/LandRegistry/datatypes)

[![Coverage Status](https://img.shields.io/coveralls/LandRegistry/datatypes.svg)](https://coveralls.io/r/LandRegistry/datatypes)

Contains the core types, validators and serializers for Land Registry concepts


### Using this package

**Add the following to your requirements.txt**

```
lrdatatypes==0.1
```

### Push new versions to PYPI public repository

Note this code is currently hosted on PYPI. The LR may want to run their own PYPI repo in LR envs and host this and other LR packages there. An easy way to do this is use [localshop](https://github.com/mvantellingen/localshop).

The travis build will push tagged versions of this package to pypy (currently using my account - this should be transferred to an LR dev/webops person, or as mentioned above pushed to your own pypi)

##### When you want to push a new version

* Set version number in setup.py
```
git tag [version number] -m "update version"
git push --tags origin master
```

