# Niryo-Bravo
Tools to test the Niryo One Python API

## Features
 * Expose a Webapp to control the [Niryo One](https://niryo.com/) from a web browser.

## Getting started

### Requirements
 * python 2.7;
 * pip;
 * virtualenv;
 * [Niryo One Python API](https://github.com/NiryoRobotics/niryo_one_ros/tree/master/niryo_one_python_api).


### Install
Upgrade `pip` and install `virtualenv`:

```
$ sudo pip install --upgrade pip
$ sudo pip install virtualenv
```

Install all the required tools in a virtualenv:
```
$ make install
```

### Serve
To run the application locally in a development environment:
```
$ make serve
```

### Usage
Just visit [http://0.0.0.0:8080](http://0.0.0.0:8080) with a web browser to command the robot!

## Tech/framework used
 * [Flask](http://flask.pocoo.org/)
 * [Bootstrap](https://getbootstrap.com/)

## Versioning
We use [SemVer](http://semver.org/) for versioning. See the [CHANGELOG.md](CHANGELOG.md) file for details.

## Contributing
If you'd like to contribute, please raise an issue or fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license. See the [LICENSE](LICENSE) file for details.

## Contributors
 * **Julien Lebunetel** - [jlebunetel](https://github.com/jlebunetel)
