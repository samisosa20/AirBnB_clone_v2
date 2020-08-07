<p align="center">
  <img src="https://latorredev.com/assets/Img/Certifications/Holberton.png" alt="HolbertonBnB logo">
</p>

# HOLBERTON BNB

_This project contains a console that can interpret various commands that will be explained here._

## Content of the project 🚀

This is the beginning of the creation of a AirBnB clone app. In the next months this repository will gonna update the code to finish all the backend and frontend; in this currently project we have a functionally console that can interpret commands, store information and reload that same information from any class instances that is stored in an a JSON file.

### Commands of the console 📋

The console can be used interactively or non-interactively. If you want to use it in the non-interactively form you need to echo the command and add a pipe before the command ./console.py 
```
$echo "all" | ./console.py
(hbnb) all
[]
```
But if you want to run it interactively(that's what we recommend) you need to run the console with the command ./console.py and use one of the next commands

* **quit** -> _Quit the console_
```
(hbnb) quit
```
* **EOF** -> _Quit the console_(ctr-d)
```
(hbnb) EOF
```
* **create** -> _Create a instance of the class and show ths class ID_
```
(hbnb) create BaseModel
24418ad1-bc8b-4f44-86de-2046d0f3c632
```
* **show** -> _Prints the string representation of a instance of a given ID_
```
(hbnb) create BaseModel
d216069b-387e-4a36-93f6-37f0c5f67bc6
(hbnb) show BaseModel d216069b-387e-4a36-93f6-37f0c5f67bc6
[BaseModel] (d216069b-387e-4a36-93f6-37f0c5f67bc6) {'id': 'd216069b-387e-4a36-93f6-37f0c5f67bc6', 'created_at': datetime.datetime(2020, 6, 30, 20, 49, 1, 446914), 'updated_at': datetime.datetime(2020, 6, 30, 20, 49, 1, 446948)}
```
* **destroy** -> _Destroy a instance of a given ID_
```
(hbnb) create Place
494b0918-f310-4dc8-b5e1-fdedbe22c1fe
(hbnb) destroy Place 494b0918-f310-4dc8-b5e1-fdedbe22c1fe
```
* **all** -> _Print all instances of a class in a string representation or all classes if no class was given_
```
(hbnb) create City
29e6b6dc-78b4-4802-96f9-2e41d6c54d73
(hbnb) all User
["[User] (b6aa6236-8c74-495a-9a4f-d58849e1892e) {'id': 'b6aa6236-8c74-495a-9a4f-d58849e1892e', 'first_name': 'Mongo', 'updated_at': datetime.datetime(2020, 6, 30, 20, 49, 31, 923005), 'age': 89, 'created_at': datetime.datetime(2020, 6, 30, 20, 41, 4, 580312)}"]
(hbnb) all
["[User] (b6aa6236-8c74-495a-9a4f-d58849e1892e) {'id': 'b6aa6236-8c74-495a-9a4f-d58849e1892e', 'first_name': 'Mongo', 'updated_at': datetime.datetime(2020, 6, 30, 20, 49, 31, 923005), 'age': 89, 'created_at': datetime.datetime(2020, 6, 30, 20, 41, 4, 580312)}", "[City] (29e6b6dc-78b4-4802-96f9-2e41d6c54d73) {'created_at': datetime.datetime(2020, 6, 30, 21, 10, 21, 190818), 'id': '29e6b6dc-78b4-4802-96f9-2e41d6c54d73', 'updated_at': datetime.datetime(2020, 6, 30, 21, 10, 21, 190851)}"]
```
* **count** -> _Number of instances in a class_
```
(hbnb) create User
c530f4f9-eb36-4e23-b41a-7be1f58ec14e
(hbnb) create User
cd13ab5b-60ec-42ce-96c1-c1c05af1a3aa
(hbnb) count User
2
```
* **update** -> _Update a class instance key and value attribute of a given ID_
```
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
```