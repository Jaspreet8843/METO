# METO
Hosted on https://meto-jrt.herokuapp.com/

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
The user side allows 
1. Login
2. Book Service
3. Edit Profile
4. Track Bookings

The admin side allows
1. Add services
2. View Bookings
3. Change status of bookings

## Snapshots
Column 1 | Column 2
------------ | -------------
![](https://github.com/manabsaha/assets/blob/main/METO/home1.PNG) | ![](https://github.com/manabsaha/assets/blob/main/METO/home2.PNG) 
Navigation | Services
![](https://github.com/manabsaha/assets/blob/main/METO/login.PNG) | ![](https://github.com/manabsaha/assets/blob/main/METO/book.PNG)
Login | Book service
![](https://github.com/manabsaha/assets/blob/main/METO/profile.PNG) | ![](https://github.com/manabsaha/assets/blob/main/METO/bookings.PNG)
Profile | Bookings

## Objective
Welcome to METO, your own managing assistant that will help you to manage each and every daily problem within minutes. METO is a managing startup, founded on June 1st,2020. In the period of the COVID19 pandemic, an ample amount of vocations have crashed and many workers have got unemployed. So, keeping an eye on this crisis, our METO community has risen to support those people and provide a helping hand towards managing your daily problems.

It support you in minor daily problems like managing a professional photographer or carpenter or makeup artist or electrician and many more including groceries. And creating a connected society in every locality.

## Project
The project is built with
* Django Framework
* HTML CSS JS
* ORM Model Django
