# 0x00. AirBnB clone - The console

This repository contains a full web application, the AirBnB clone.
The console is a command interpreter that is used to manage objects in the file storage.
It is used to create, destory, show and update objects in the [file storage](./models/engine/file_storage.py).

## Start

run the console:

```bash
python3 console.py
```

## Usage/Examples

### create

create an object

Usage: `create <class name>`

```code
(hbnb) create User
fb15b40d-28ec-499c-84c6-f246acd613e2
(hbnb) create City
7c984cea-24b6-4029-aa3e-590c787b65fc
```

### show

show an object

Usage: `show <class name> <id>`

```code
(hbnb) show City 7c984cea-24b6-4029-aa3e-590c787b65fc
[City] (7c984cea-24b6-4029-aa3e-590c787b65fc) {'updated_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277), 'id': '7c984cea-24b6-4029-aa3e-590c787b65fc', 'created_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277)}
```

### destroy

destroy an object

Usage: `destroy <class name> <id>`

```code
(hbnb) destroy City 7c984cea-24b6-4029-aa3e-590c787b65fc
(hbnb)
```

### update

update an object

Usage: `destroy <class name> <id> <attribute name> "<attribute value>"`

```code
(hbnb) update User fb15b40d-28ec-499c-84c6-f246acd613e2 first_name 'John Doe'
(hbnb)
```

### all

list all the objects in the file storage

Usage: `all` or `all <class name>`

```code
(hbnb) all
["[User] (fb15b40d-28ec-499c-84c6-f246acd613e2) {'updated_at': datetime.datetime(2022, 9, 4, 22, 12, 4, 371618), 'id': 'fb15b40d-28ec-499c-84c6-f246acd613e2', 'created_at': datetime.datetime(2022, 9, 4, 22, 12, 4, 371618)}", "[City] (7c984cea-24b6-4029-aa3e-590c787b65fc) {'updated_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277), 'id': '7c984cea-24b6-4029-aa3e-590c787b65fc', 'created_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277)}"]
(hbnb) all City
["[City] (7c984cea-24b6-4029-aa3e-590c787b65fc) {'updated_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277), 'id': '7c984cea-24b6-4029-aa3e-590c787b65fc', 'created_at': datetime.datetime(2022, 9, 4, 22, 12, 7, 955277)}"]
```

## Authors

- **Kalab Sisay** [@KalabSisaySE](https://github.com/KalabSisaySE)

