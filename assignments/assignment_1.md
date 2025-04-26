# Assignment 1
## Due by 1PM (before class) on Thursday May 9th

This assignment will have you practice using the linux command line as well as have you setup a Github repository.


### Part 1: Linux Command Line

1. Go to your scratch-lustre (`/fs/lustre/scratch/USERNAME`) folder on CITA. Create a folder called `CTA200_2024`. Inside this folder, make a folder called `assignment_1` and also add a file called `README.md`. Add the title `# CTA200 2024` to the `README.md` file using vi.

2. Somewhere in Norm's (username `murray`) home directory, there are two files named `Hello_world.c` and `Hello_world.py` (note that the H is capitalized). Find them and copy them to the `assignment_1` folder you created in step 1. You can use `find` to help you search for them.

3. Rename your version of the files `Hello_world_your-last-name.c/py`.

4. Compile the C code using `gcc` (you will need to load a module for this). Name the executable `Hello_world.x`.

5. Run the C program and the Python program to see what they do.

6. Using `vi`, edit both programs so that they now print `Hello, <Your Full Name> from <Language (C/Python)>`. 

7. Run the updated C and Python programs. Pipe the output of the C program to a file called `output_c.txt` and the output from the Python program to a file called `output_python.txt`.

8. Pipe the commands you used to do steps 1-7 to a text file by using the `history` command. Call the file `history.txt` and place it in the `assignment_1` folder.


### Part 2: Git

1. Initialize a git repository in your `CTA200_2024` folder.

2. Add and commit the `README.md` file.

3. Also add and commit the changed versions of the C and Python programs to your git repo. Also commit the `output_.txt` files and the `history.txt` file.

4. Make a new repository on your Github account called `CTA200_2024`. Add the Github repository as a remote for your local repository.

5. Push the changes from your local repository to the remote repository.

### How to submit

Make sure that all of the files are visible in your Github repository. Send a link to your repository to Daven (d dot cocroft at mail dot utoronto dot ca) before the due date.
