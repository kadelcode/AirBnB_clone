# AirBnB_clone
## Project Description
A full web application: the ***AirBnB clone*** using:
- Python programming language as a backend technology
- HTML/CSS templating
- Database storage
- API
- Front-end integration

## Console Description
The console is used to manage the objects in this project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object form a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

## Usage
- The console can be run in both interactive and non-interactive mode.
- It prints a prompt (hbnb) and waits for the user's input

### Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
