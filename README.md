# METO

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Jaspreet8843/METO.git
$ cd METO
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m virtualenv myenv
$ myenv\Scripts\activate
```

Then install the dependencies:

```sh
(myenv)$ pip install -r requirements.txt
```
Note the `(myenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(myenv)$ py manage.py runserver
```
And navigate to `http://127.0.0.1:8000/METO/`.

## Walkthrough
The project has the user side and admin side.
