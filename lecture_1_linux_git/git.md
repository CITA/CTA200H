# Git

Git is a version control system for tracking changes to files. It is widely used in software development. Each change to each file is stored, so that a history of all iterations of the code are kept.

Keeping a history of your code development has multiple advantages. You can track when new features are added or bugs are fixed, and if pieces of code are removed or substantially modified, you still have access to the previous versions. If a new bug is introduced, this also makes it possible to revisit earlier versions of the code to find out which change introduced it, which in turn makes it easier to find and fix the bug.

Typical usage of git is to have a main repository for the code, with each developer grabbing (or `clone') a copy for themselves to use locally. They can edit the code and make some changes to their local copy, then commit and push those changes back to the main repository. [Github](https://github.com/) is one option to store repositories online so that they can be accessed from anywhere. This design model is advantageous for collaborative efforts to develop software since everyone has their own copy of the code, but can push their changes to the central repository so that everyone else can get (pull) them.

One aspect of git is that not only is there a central repository, but also every local copy is its own repository. Thus you can commit multiple changes to your local copy before pushing them to the central repository. For example, if you're developing a complex new feature for your code, you could work throughout the week implementing it and commit incremental changes to your own copy, then once its finished and polished, push the finalised version to the central repository for everyone else to use.

## Git Basic Usage

The majority of the time you only use the same few git commands. Use `git clone` to create a local copy of an existing repository. You've already used this in the first lecture to create a local copy of the course material, that is,

`git clone https://github.com/CITA/CTA200H.git`

With this you then have all the files that are part of this project and also the history of each file. 

Now that you have cloned a repository, how do you commit changes you make? Say you've already invested a couple of hours editing the code, adding new functions, fixing bugs, and introducing new bugs by accident. To save your changes and store them on the central repository, use the commands `git add`, `git commit`, and `git push`.

`git add` tells git which files you want to be part of the commit. This command adds the specified files to the list of files to be committed. You may wonder why git doesn't just add all changed files, but possibly you have changed multiple things and you only want to commit specific files.

`git commit` adds those changes to your local repository. As mentioned in the introduction, each local copy is also its own repository. Each commit requires a message to explain the changes that have been made. This then is a record for yourself, but also for everyone else who uses the code to quickly understand what you've changed.

`git push` adds the committed changes to the central repository. Then everyone else has access to your changes and can update their own copy of the code with them.

`git pull` is the reverse of git push. Instead of sending your updates to the central repository with `git push`, you use `git pull` to obtain the updates other people have pushed to the central repository. This should be done regularly so that you are working with the same version as everyone else.

#### Example

First update to the latest version of code using `git pull`, then add the file(s) you want to commit, commit them with a message explaining your changes, and finally push them to the central repository.

```console
git pull
git add fileread.cpp
git commit -m "Fixed bug in file read for large files"
git push
```

## Best Practices for git commit

- **Keep your commits atomic.** 

An atomic commit only contains one addition or fix. Use atomic commits to keep each commit related to only one task. This improves readability of commit messages since they are focused and short, and importantly helps in tracking down bugs. When each commit changes only one thing, it becomes easier to identify which commit broke your code. If each commit is large and changes multiple areas of the code, then it becomes difficult to disentangle changes to track down the bug. 

If you've made several changes and forgotten to commit them individually, don't fret. Use `git add -p` (meaning patch) to commit individual parts of a file.

- **Keep commit messages precise.** 

This is easier if you are making atomic commits. Avoid vague commit messages such as "_Fixed bug_". Instead, write a clear messages like "_Fixed temperature function to avoid sqrt of negative number_".

- **Make commits as you are developing.**

Avoid letting changes pile up. Don't make "Friday end of day" commits storing all the work you did for the week. Instead, make atomic commits as you are developing and writing your code. 


## Additional Useful Commands

`git log` displays the history of the code repository, showing when the commit was made, who made it, and the message attached. Use `git log --stat` to show the files that were modified in each commit.

`git status` gives the list of all modified files and files which are not stored (tracked) in the repository.

`git diff` shows the differences between your copy of the files and the copy stored in the repository. Use this to see the changes you've made.

## Creating a New Remote git Repository

Creating a new repository on github or other online git repositories is easy. Just log in to your account, start a new project, and afterwards use `git clone` on your computer to obtain a local copy. You can then use `git add`, `git commit`, `git push` to add the files to your online repository.


## Dealing with Commit Conflicts: git stash

One common scenario is that you have forgotten to do a `git pull` for a while. Since your last pull, changes have been pushed to the central repository, but you've also been editing the code in your local copy. If you've modified some of the same files that have been changed on the central repository, how do you reconcile the difference?

That's where `git stash` comes in. Using this you can temporarily store the changes you've made. This reverts the files back to their original state, allowing you to do a `git pull`. After you have the central repository version of those files, you can un-stash your changes (`git stash pop`), applying them to newly updated code version. From here, you can proceed as normal with `git add`, `git commit`, `git pull`. 

Note that `git stash` only saves your changes locally for you. It does not transfer them to the central repository.

### Example of git stash

I have not done a `git pull` in a while, and have made some important changes to the code. I try to do a `git pull` before I commit, but get the following error

```console
remote: Counting objects: 18, done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 18 (delta 14), reused 0 (delta 0)
Unpacking objects: 100% (18/18), done.
From https://github.com/...
   18700d3..a47e057  master     -> origin/master
Updating 18700d3..a47e057
error: Your local changes to the following files would be overwritten by merge:
	src/main.cpp
Please commit your changes or stash them before you can merge.
Aborting
```

This warns me that the changes I've made to main.cpp would be lost if `git pull` proceeded since this file on the repository has been new modifications.

Let's use `git stash` to get both sets of changes. First, use `git stash` to store our local changes, followed by `git pull` to update to the latest version, then `git stash pop` to apply our stashed changes.

```console
$> git stash
Saved working directory and index state WIP on master: 18700d3 ... in src/main.cpp
HEAD is now at 18700d3 ... in src/main.cpp

$> git pull
Updating 18700d3..a47e057
Fast-forward
 src/main.cpp | 17 +++++------------
 1 file changed, 7 insertions(+), 10 deletions(-)
 
$> git stash pop
Auto-merging src/main.cpp
On branch master
Your branch is up-to-date with 'origin/master'.
```

Now we have main.cpp which has both the changes we've made and the most recent changes pushed to the repository.


## Non-trivial Conflicts

In the previous example, `git stash pop` was able to auto-merge our changes with the changes on the central repository. Git can do this when the changes are in unrelated parts of the file. 

However, if changes are in the same part of the code, then git cannot auto-merge the two. Wherever there are conflicting lines of code, git will insert both and leave it up to you to merge them by hand. The merged file can then be committed afterwards.

### Example

Let's say I have already performed a `git stash` and `git pull`. Now I try to pop my stashed changes.

```console
$> git stash pop
Auto-merging src/main.cpp
CONFLICT (content): Merge conflict in src/main.cpp
```

Git has warned me that there is a merge conflict. I now need to edit this file to fix the conflict. I can view what git has done using `git diff`

```console
$> git diff
diff --cc src/main.cpp
index 02d4c12,918a3de..0000000
--- a/src/main.cpp
+++ b/src/main.cpp
                
++<<<<<<< Updated upstream
+              di = h * h * mode * pos * pos * invsigma
++=======
+              di = h * h * mode * pos * 2.0
++>>>>>>> Stashed changes
```

Only you can fix this code.

## Revisiting older versions of the code: git checkout

We can use `git checkout` to revert code to an earlier version. Each commit has an individual id which is a 40 character alphanumeric string. 

```console
$> git log
commit 082e65c854370abccb802640e8f682d15ec75dbc
Author: Terrence Tricco <ttricco@cita.utoronto.ca>
Date:   Fri Apr 13 14:54:39 2018 -0400

    Added description to main.cpp

commit 46f55f92fb3e050e8de61fead3bd631653f32373
Author: Terrence Tricco <ttricco@cita.utoronto.ca>
Date:   Wed Mar 21 11:34:13 2018 -0400

    Updated default command line arguments
```

Nobody can remember these, so git accepts shorthand commit ids which are just the first 7 characters. Instead of writing 082e65c854370abccb802640e8f682d15ec75dbc, you can just use 082e65c and git will understand which commit you mean. In the previous examples you can see that they used this shorthand id.

Note that you should avoid developing on an older commit. 

## Branches

One of the more powerful features git implements is branches. Branches are multiple versions of a code, with each branch essentially an independent line of development. Every git repository starts with one branch, the master branch (you can see this referenced in examples above). 

Branches help isolate your work from the original code base, and can help keep questionable code out of the master repository. If you're working on a new feature, you can do all your development on your own branch, then commit the final working version to the master branch keeping the intermediate (still buggy) steps out of the main code. 

`git branch` can be used to list, create and delete branches. Just like switching between different commits, we can use `git checkout` to switch between different branches. 

If you run `git branch` by itself, it will list all current branches and show you which branch your code is on. New branches can be created by just specifying a name for the new branch, for example, `git branch newbranch`. 


### Example of Branches

Let's say I want to add a new function to my code. I can create a new branch, develop and test my function on this branch, and once finished and I'm happy that it's bug free, merge my branch back into the master branch for everyone to use. Let's see how to do this.

First, let's create a new branch called 'newbranch' (or something more appropriate for your case). Remember that running `git branch` by itself lists all current branches. 

```console
$> git branch
* master

$> git branch newbranch

$> git branch
* master
  newbranch
```

The last command shows that we are still on the master branch. Let's change branches.

```console
$> git checkout newbranch
Switched to branch 'newbranch'
```

Now we can develop our new function in isolation on this branch, remembering that we use the best practices of atomic commits, precise commit messages, and committing our work as we develop.

When we finish, we can merge our branch back into master. To do this, switch back to the master branch, then use `git merge` to merge your newbranch into master.

```console
$> git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.

$> git merge newbranch
Updating a47e057..6e20506
Fast-forward
 src/main.cpp | 3 +++
 1 file changed, 3 insertions(+)
```

## Complicated git

This tutorial only covers the basics of git and commonly encountered scenarios. Each command has more optional arguments that can be used (see the documentation), and you may run into scenarios that are not covered in this tutorial. Google is a friend in those situations.

You can also read more about git at the documentation: Documentation: [https://git-scm.com/docs](https://git-scm.com/docs)