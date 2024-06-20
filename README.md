# Flask-REST_API

NAME: VED VISHAL MIRJANKAR <br/>
PROJECT: BUILDING A REST API <br/>

ABSTRACT: <br/>
This project aims to build a mock Youtube API by building a RESTful API using Flask and Python to create, retrieve, update, and delete video records in a SQLite database. It uses SQLAlchemy for database interactions and Flask-RESTful for creating the API endpoints. </br>

BRIEF PROCESS DESCRIPTION:<br/>
main.py:<br>
•	Imported all the necessary modules.<br>
•	Defined a class for the Database Model.<br>
•	Defined two request parsers to specify the arguments for PUT and PATCH requests.<br>
•	Defined a dictionary (resource_fields) which specfies that the instances should be serialized.<br>
•	Defined a class which contains all the functions for the resources i.e. GET, PUT, PATCH, DELETE<br>
test.py:<br>
•	Used for testing the API<br>

IMAGES:<br>
1. Running two terminals (one for main.py and one for test.py). In this image, it shows how I am using PUT method to put data into the database but the data with the same ID already exists. After that, I am using GET method to get data for a specified video ID but the video ID does not exist: <br>
![image](https://github.com/vmirjankar/Flask-REST_API/assets/111427005/7b5cd067-2a9e-49fa-bb1a-9c87e1c93119) <br>
2. In this image, I am using the UPDATE method to update some value in the database:<br>
![image](https://github.com/vmirjankar/Flask-REST_API/assets/111427005/8855b8ac-fb8d-4eb4-b414-bcba2a450c56) <br>
3. Shows test.py code:<br>
![image](https://github.com/vmirjankar/Flask-REST_API/assets/111427005/393a13cb-0543-45ea-b3d5-9d925103a839)<br>









