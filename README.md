# EC601_Project

## Demo
 (Web App): https://threehungrychinese.github.io/MaineCoonUi/
 
 (iOS App): (Checkout screenshots of iOS App) https://github.com/ThreeHungryChinese/iOSApp
 
## Project Info:
Project Name:Automated Admission System

Project Member:Qingxuan Pei, Haoyang Wang, Kefan Zhang

## Project Repos：

https://github.com/ThreeHungryChinese/EC601_Project Main readme of this prjcect by all group members

https://github.com/ThreeHungryChinese/EC601_Project default Algrothim by Kefan Zhang

https://github.com/ThreeHungryChinese/iOSApp iOS Application by Kefan Zhang

https://github.com/ThreeHungryChinese/WebApps [*abandoned*] Web Application (Sprint 1 & Sprint 2) by Haoyang Wang 

https://github.com/ThreeHungryChinese/MaineCoonUi Vue web interface (Sprint 3) by Haoyang Wang 

https://github.com/ThreeHungryChinese/MaineCoonApi Back-end services (Sprint 3) by Haoyang Wang

https://github.com/ThreeHungryChinese/PDFprocess PDF Process Algrothim by Qingxuan Pei

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



            
