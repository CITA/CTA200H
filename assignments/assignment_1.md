# Assignment 1
## Due by 1PM (before class) on Wednesday May 4th

This assignment will have you practice using the linux command line as well as have you setup a Github repository.

1. Make a new repository on your Github account called `CTA200 Homework`. Clone the new repository to somewhere in your `scratch-lustre` space. Add a `README.md` file with the header `CTA200 Homework`.

2. Inside the local version of the repository, add a folder called `assignment_1`. All of the material for this assignment will go in this folder.

3. Do the following on the CITA machine. At the end, you will submit both the files produced throughout theexercise as well as a list of the commands you typed to do them.

    1.  Somewhere in Norm's (username `murray`) home directory, there are two files named `cta200.c` and `cta200.py`. Find them and copy them to the `assignment_1` folder you created in your repo. You can use `find` to help you search for them.

    2. Rename your version of the files `cta200_your_last_name.c/py`.

    3. Compile the C code using `gcc` (you will need to load a module for this). Name the executable `cta200.x`.

    4. Run the C program and the Python program to see what they do.

    5. Using `vi`, edit both programs so that they now print `Hello, <Your Full Name> from <Language (C/Python)>`. 

    6. Run the updated C and Python programs. Pipe the output of the C program to a file called `output_c.txt` and the output from the Python program to a file called `output_python.txt`.

4. Commit the changed versions of the C and Python programs to your git repo. Also commit the `output_.txt` files.

5. If you have not done so yet, save your command history to a file and commit it to your repo. You can get your command line hisory using the `history` command. You can pipe the result of this to a file to save it.