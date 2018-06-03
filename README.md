**Project Title**

wordcount-project

**Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See Running the tests for notes on how to deploy the project on a live system.
You can use this website to compute the characters easily.

#Prerequisites

Django is a free and open source web application framework, written in Python. A web framework is a set of components that helps you to develop websites faster and easier.
##Installing Django
> pip install Django==2.0.5
You can also refer to the below link on how to install all the three options to get Django [Download Django](https://www.djangoproject.com/download/).

##Installing python3
> brew install python3
You can also refer to the below link on how to [install python3](http://programwithus.com/learn-to-code/install-python3-mac/)

**Running the tests**
1. Download the source code to your macBook, unzip the file.
2. Access to the directory where the project(project name: wordcount-project) is, you can see two sub-folders (templates and wordcount) and manage.py file.
3. run the command line *python3 manage.py runserver* via terminal, then the server starts running. Please check the below output:

> JOYIN-M-L2GU:wordcount-project-master joyin$ python3 manage.py runserver
> Performing system checks...

> System check identified no issues (0 silenced).
> June 03, 2018 - 10:43:39
> Django version 2.0.5, using settings 'wordcount.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CONTROL-C.
4. You can go to the server http://127.0.0.1:8000/ to test the website. When you input characters in the textarea, then click the "count!" button, the output should just be like below:

```
There are 22 words in your text
Start Again
Your Text:
You are testing the wordcount website here. Hope you like this website here. It is so simple for you to use it.
Word Count:
website - 2 
here. - 2 
you - 2 
You - 1 
are - 1 
testing - 1 
the - 1 
wordcount - 1 
Hope - 1 
like - 1 
this - 1 
It - 1 
is - 1 
so - 1 
simple - 1 
for - 1 
to - 1 
use - 1 
it. - 1 
```
**License**

This project is licensed under the MIT License.
