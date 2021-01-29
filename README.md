<p align="center">
  <img src="https://raw.githubusercontent.com/Rodrigo-Weich/command-processor/main/content/logo.png">
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3-blue.svg">
  </a>
  <a href="https://github.com/Rodrigo-Weich/command-processor">
    <img src="https://img.shields.io/badge/Release-1.X-red.svg">
  </a>
    <a href="https://opensource.org">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

<p align="center">
  It is a system developed in python 3 that handles terminal entries. It differentiates text from commands and also executes them.
</p>

## How to Install
```bash
# Get this repository
$ git clone git@github.com:Rodrigo-Weich/command-processor.git

# Go into the repository
$ cd command-processor/

# Run
$ python3 init.py
```

## How to Use

You can define commands according to your need, for that, just follow the steps below

#### In commands.py file:
```python
# First, create the role you want to add to the system. Example:
def name(name):
  return print(f"Name: {name}")

# Then, add the command line to the command list
commands = {
  "@name": "@name <name>|1|name(arguments[0])"
}
# Or else
commands["@name"] = "@name <name>|1|name(arguments[0])"
```
### Important
The commands are formed by a string of parameters, where:

| Arguments  | Information |
| ------------- |:-------------:|
|"@name"|Is the key that identifies the command in the list|
|"@name <name>|Is the command syntax|
|1|Is the number of parameters that the function will have
|name(arguments[0])"|Is the function itself|

#### Warning
To add parameters to the function, you must use arguments[array_index]
For a function without parameters, use only name()
For a function with a parameter, use name(arguments[0])
For a function with two parameters, use name(arguments[0], arguments[1])
And so on...

## License

The Command Processor is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).