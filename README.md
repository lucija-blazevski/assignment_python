## Function 'Cheat'

1. [Usage](#usage)
2. [Motivation](#motivation)
4. [Technology](#technology)
5. [Example](#example)
6. [Installation](#installation)


***

# Usage

This package contains one module, which contains the function cheat().
The cheat() function takes one argument specifying which exercise of any previous Python assignments the user wants to cheat on. 
The argument has to be a string.
Given the exercise number, cheat() function tells the user the correct solution.

## Motivation

This is the project created to answer Q.3.2P.9 of Assignment_3_2P.



## Technology

Python 3.9


## Example
```
cheat("Q.1.2P.3")
```

```
Out[1]:

#Python does not make a true copy of the array in the second line 

#To do this properly use:

another_array = np.zeros((2, 4, 6))

new_array = np.copy(another_array)

new_array[1, 2, 2] = 1

print(another_array[1, 2, 2]

print(new_array[1, 2, 2])
```


## Installation

In your Pycharm terminal type: pip install git+https://github.com/lucija-blazevski/assignment_python.git


Then in your Pycharm console type: from cheat import cheat * 


Now you are ready to use the function cheat()


*If the import state is as follows: "import cheat", to use the function cheat() use: cheat.cheat()
