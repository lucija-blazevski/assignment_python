

def cheat(question):

    """This function return the answer to any assignment question.
    Note: Argument question has to be a string."""

    if not isinstance(question, str):
        raise ValueError("The question number has to be a string")

    elif question == "Q.1.2P.1":
        print("import numpy as np")

    elif question == "Q.1.2P.2":
        print("print(another_array[0, 3, -1])")

    elif question == "Q.1.2P.3":
        print("# Python does not make a true copy of the array in the second line\n"
              "# To do this properly use:\n"
              "another_array = np.zeros((2, 4, 6))\n"
              "new_array = np.copy(another_array)\n"
              "new_array[1, 2, 2] = 1\n"
              "print(another_array[1, 2, 2]\n"
              "print(new_array[1, 2, 2])")

    elif question == "Q.1.2P.4":
        print("This function does not work in a script because it is not a Python function")

    elif question == "Q.1.2P.5":
        print("# %cd - change the working directory\n"
              "# %pwd - print the working directory\n"
              "# %ls - list the contents of the working directory\n"
              "# %who - list current workspace variables\n"
              "# Alternate answer:\n"
              "# %whos - list current workspace variables")

    elif question == "Q.1.2P.6":
        print("# pip install pip-install-test")

    elif question == "Q.1.2P.7":
        print("sample_scores = np.array([1, 6, 7, 8, 9, np.nan])\n"
              "print(np.mean(sample_scores))\n"
              "# Numpy computes the sum of a NaN number as NaN\n"
              "# Correct answer\n"
              "print(np.nanmean(sample_scores))\n"
              "# 6.2")

    elif question == "Q.1.2P.8":
        print("square_array = np.reshape(np.arange(1, 17) ** 2, (2, 2, 2, 2))\n"
              "# Note that square_array is in a different order to Q1.1.31 in R")

    elif question == "Q.1.2P.9":
        print("insect_sprays = pd.read_csv('InsectSprays.csv').to_dict() \n"
              "pd.DataFrame.to_dict()\n"
              "insect_sprays.keys()")

    elif question == "Q.1.2P.10":
        print("np.random.seed(1234)  # Set the random seed\n"
              "speed_sec = np.zeros(10)\n"
              "sim_speed = np.random.uniform(size=5)  # Speed simulation in seconds\n"
              "speed_sec[::2] = sim_speed * 10\n"
              "speed_sec[1::2] = sim_speed\n"
              "all_data = {'language': np.tile(np.array(['R', 'Python']), 5),'code_type':\n"
              "np.repeat(np.array(['forloop1', 'forloop2', 'forloop3','forloop4', 'forloop5']), 2), 'speed_sec': speed_sec}\n"
              "my_data = pd.DataFrame(all_data)\n"
              "print(my_data)")

    elif question == "Q.2.2P.1":
        print("two_dice = np.random.choice(np.arange(1,7), 2, replace = True)\n"
              "score = 0\n"
              "if sum(two_dice)%2 == 0:\n"
              "score = sum(two_dice)*min(two_dice)\n"
              "print(score) #I added this just so it is easier for me to check if it code works later.\n"
              "else:\n"
              "score = sum(two_dice)*-3\n"
              "print(score)")

    else:
        return "There is no available answer to this question"
