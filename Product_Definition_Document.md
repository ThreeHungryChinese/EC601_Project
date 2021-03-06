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
