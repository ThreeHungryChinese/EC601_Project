EC601_Project：Automated Admission Platform
==================

Haoyang Wang, Qingxuan Pei, Kefan Zhang

## Demo
 (Web App): https://threehungrychinese.github.io/MaineCoonUi/
 
 (iOS App): (Checkout screenshots of iOS App or contact kefan29@bu.edu for it) https://github.com/ThreeHungryChinese/iOSApp
 

## Project Repos：

https://github.com/ThreeHungryChinese/EC601_Project Main readme of this prjcect by **all group members**

https://github.com/ThreeHungryChinese/EC601_Project Regression scripts and server configurations by **Kefan Zhang**

https://github.com/ThreeHungryChinese/iOSApp iOS Application by **Kefan Zhang**

https://github.com/ThreeHungryChinese/WebApps [*abandoned*] Web Application (Sprint 1 & Sprint 2) by **Haoyang Wang**

https://github.com/ThreeHungryChinese/MaineCoonUi Vue web interface (Sprint 3) by **Haoyang Wang**

https://github.com/ThreeHungryChinese/MaineCoonApi Back-end services (Sprint 3) by **Haoyang Wang**

https://github.com/ThreeHungryChinese/PDFprocess PDF Process Algrothim by **Qingxuan Pei**

# Project Guide

## Introductions
 A user Interface based on Vue.js
 
![Vue logo](/pictures/logo.png)
### features
* Material Design User Interface
* COOL visible design for building a data flow
* Elegant Animations
* High completion level
## Demo
### Sample User:
For developters: developer@example.com | Password:123456

For School Administors: schooladmin@example.com | Password:123456

For Students: student@example.com | Password:123456

### Demo Link:
https://threehungrychinese.github.io/MaineCoonUi/
### Instructions & ScreenShots
#### For developer
After login the system, UI will look like this

![developer](/pictures/developer.png)

Try it by clicking edit & New & Delete Button
##### Set up program's data flow
In the Edit/Create dialog's third step, there is something like this

![flow](/pictures/flow.jpg)

* As you can see, there are bubbles (*We call it dots*) on users screen. Blue dots represents this Programs' input which get from student's input and the output score of this flow. So this means the input dots must have a pointer to others and the output must be pointed from other dots.

* Other dots means a algorithm provided by developers. Users can click the add button in the top toobar to and a dot or delete button, then click a dot to delete one.

* If a user click a dot, its input setting table will show on the below. And the dot's color will change to orange, which shows this dot is selected.

* Once a user set all the input of a algorithm, it will change to green, which means this dot is set correctly.

* All dots are dragable, so if one are setting a huge data flow, they will find this feature is really useful.

#### For School Adminisator

After login the system, UI will look like this

![schooladmin](/pictures/schooladmin.png)

Try it by clicking edit & New & Delete Button.

#### For Student
After login the system, UI will look like this

![student](/pictures/student.png)

click start to start a prediction.

## Deploy 
### Dependency
    "core-js": "^3.4.8",
    "vue": "^2.6.10",
    "vue-d3-network": "^0.1.28",
    "vue-material": "^1.0.0-beta-11",
    "vuebars": "^0.1.5",
    "vuelidate": "^0.7.4"
### Set up developing  Environment
#### First: Download a Node.js &  Environment
Check https://www.npmjs.com/get-npm to get instructions about how to install it on your OS

#### Second: Donwload Vue-Cli

(Reference https://cli.vuejs.org/)

`npm install -g @vue/cli`

#### Third: Launch Vue-Cli
Clone this repo.

To open this project, please just change your current dictionary of your terminal to the repo's root dictionary

And then,

`vue ui`

### Deploy on your own server
need a web server, like Apache || Nginx || IIS.

just link the index.html will not work since browser's CROS policy may block some essential resources.

#### Important information about CORS
Check to get information about [CROS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) 
 

# iOSApp


<p align="center">
  <img width="200" height="400" src="/pictures/app1.jpg">
</p>

<p align="center">
  <img width="200" height="400" src="/pictures/app2.jpg">
</p>

<p align="center">
  <img width="200" height="400" src="/pictures/app3.jpg">
</p>

<p align="center">
  <img width="200" height="400" src="/pictures/app4.jpg">
</p>

# MaineCoonApi
 RESTful API for automation admission system
 
 Based on .Net Core 3.0
 
 Provide services to all comptiable client application
 
 ## Check a web application using this Api Service
 
 https://github.com/ThreeHungryChinese/MaineCoonUi
 
 ## Check this projects' readme
 
 https://github.com/ThreeHungryChinese/EC601_Project

# Sprint 1


## Outcome:

·Product Definition Document(Product Mission, Customer(s), MVP user stories)

·All system setup

·Review and analysis industrial products

·Test programs

# Sprint 2

## Outcome:

·Extended to 6 default algorithms.

·Developed web platform, including interface, register and login function, feasible to apply third-party algorithms or choose different default algorithms.

·API for Thrid-Party Developer

·HTTPs request to communicate between different components of system

## Schedule:


Stage #1:(Sep 20th - Oct 4th)

Assignment: Product Definition Document, System Setup and Test Programs.


Stage #2:(Oct 8th - Nov 4th)

Assignment: System architecture (HTTP request to return score, data storage and export function), more algorithms,
            explore feasibility of NLP for LOR, SOP (VMOCK), extension on Telegram (*undecided)


System Architecture:

![System Architecture](/pictures/SystemArchitecture1.png)

# Sprint 3

## Outcome:

·Web Application is abandoned. (In sprint 3, it is replaced by high choesion front-end Vue app and .Net Core Restful Api service.)

·Add a new Web client 'MaineCoonUi', with a elegant, Material Design outward, used Vue.

·Add a back-end service 'MaineCoonApi', it is able to provide a Restful api to other front-end application, used .Net Core 3.0.

·Rewrite Apis for developer & update the SQL Server tables 

·Developed iOS application for students.

·Added a sample algorithm allow user to convert Transcript to average score.

·Improved sample algorithm.


New System Architecture:

![System Architecture](/pictures/picturesSystemArchitecture2.png)

# Product Mission

The product is composed of three main parts: the user interface, the admission assistant
system and data storage structure.

The user interface, i.e. UI, supports users to upload the required documents for applying.
After the result calculated by the admission assistant system is generated, the chance of 
admission is shown on the user interface.

The admission assistant system is a rating system that takes required documents as input
and outputs a potential score as the chance of admission. The system is supported by 
several different algorithms and regard the admission possibility as a supervised learning
problem.

Another feature of this product is that we add a data storage structure. With the help of
this, users in the future can acquire admission data and the corresponding documents for 
statistical use.

# Customers

1.Applicants

2.Admission Officers

3.Developers

# MVP(Minimum Valuable Product) User Story

1.for applicants

Applicants can use this product to evaluate the chance of him/herself being admitted
by some certain university/college.

2.for admission officers

Admission officers can use this product to assist them to comprehensively consider whether
an applicant is qualified to be admitted.

3.for developers

Since we will reserve the API interface and corresponding API standard, developers who 
have developed great evaluating algorithms can test their algorithm reliability via 
our API. For profit purpose, they can consider selling it to universities if the algorithm
performs better than the existing algorithms.

Minimum Valuable Product before Sprint 1:

design a system with:

· an interface that takes in documents and outputs the scores/chance of admission

· an admission assistant system with >=1 algorithm(s) available to generate evaluation scores/chance of admission

· a data storage structure that stores all data



            
