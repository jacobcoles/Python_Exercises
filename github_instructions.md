# Helpful Links

Here are a couple of links to help get started with Git. It somewhat relies on an understanding of the command-line (i.e. terminal), but don't be scared away by the initially tricky syntax. It takes time to master it, but there are a handful of commands you can use for basic usage. 

- https://webtuu.com/blog/04/a-laymans-introduction-to-git
- https://learngitbranching.js.org/
- https://git-scm.com/

# Simple Setup

### Cloning the repository

To 'clone' (i.e. make a copy) of a Git repository on your local machine, first find the link to your Github page. This link can be found by clicking the green 'Code' button on the website (in your Github repository).

Use the following command in your terminal:
```
git clone INSERT_YOUR_LINK
```

Then, move into that directory (folder) where DIRECTORY_NAME is the name of the github repository:
```
cd DIRECTORY_NAME
```

### Committing your changes

Before you syncronise with the remote repository you must commit all your changes. In laymans terms, a 'commit' is just "creating a new version". This just means that you're going to manually indicate that there is a new version of the repository (i.e. a new version of the code in your folder). Do do this, you need to add the specific files with changes you would like to 'commit'.

You can 'stage' (prepare) a file to be committed (added to the next version):
```
git add C://path/to/specific/file
```

...or you can add all files in the current folder (which have been changed since the last version) by using a dot:
```
git add .
```

Then you can commit these changes (locally) as a new commit (version) with a custom message under the -m flag:
```
git commit -m "Here are some changes I made"
```

Once you are happy with the new commit (version), you can 'push' (upload) the commit to the remote repository (i.e. your Github page).
```
git push
```

# Advanced Setup and Fixes

These setup instructions can be skipped if using the simplified instructions above.

To start a repository first locally, you can use the following commands:
```
git init
git commit -m "first commit"
git branch -M main
```

This can be linked to a remote repository:
```
git remote add origin INSERT_YOUR_LINK
```

You can then attempt to sync with an existing remote repository:
```
git pull
git add .
git commit -m "second commit"
git push -u origin main
```

## Troubleshooting

If you have issues merging with the remote repository:

** 1.** Create a ".gitattributes" file in the root (top-level) of your folder. 
Type the following (inside the file) and save it:
```
.gitignore merge=union
```


** 2.**  Run each of the following in sequence in your terminal:
```
git init
git add .gitignore .gitattributes
git commit -m "First commit"
git branch -M main
git remote add origin YOUR-GITHUB-REPO-LINK-HERE
git fetch origin
git merge --allow-unrelated-histories -X theirs origin/main
git push -u origin main
```

You may encounter additional 'merge' conflicts. This happens if there are two diverging versions (of files with the same filename) in the remote repo as well as locally. The solution is to allow git to decide how to 'merge' each of these divergent versions of files by accepting its suggestions. To do this, go through each of your files for which there is a 'conflict' and 'accept' the changes. VSCode should provide you the option to open each file in the 'merge editor' where you can accept the suggested fixes and save it. After this try t

If you encounter any other specific issues not mentioned here, then the terminal may provide some suggestions. Try to follow the instructions given if they're directly actionable.

If you want to delete the existing local copy of your git repository, you can use the following: (NOTE: Will not delete your actual code)
```
rm -Recurse -Force .git
```


