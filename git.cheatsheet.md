# Useful Git commands 

This is just stuff that I have put down that I find I use a lot of the time for my own reference.

## Latest changes from repo to your machine

```shell
$ git pull
```

## Add tracking information to your work

Assuming that you are working on the master branch then

```shell
$ git branch --set-upstream-to=origin/master
```

You can set it to whatever branch you want to track changes for

```shell
$ git branch --set-upstream-to=origin/<branch>
```

This will mean you can just do `git pull` and the latest changes will be pulled to your `origin`

## What branch?

`$ git branch` shows what branch you're on

`$ git branch -r` shows remote branches

`$ git branch -a` shows all branches

## Create a PR [[Pull Request](https://spences10.github.io/2017/01/05/git-and-github.html)]

Fork other users repo in GitHub, then clone to your machine.

```shell
$ git clone https://github.com/YourUserName/awesome-awesome-repo
```

Add the remote repo 

```shell
$ git remote add upstream https://github.com/OtherUserName/awesome-awesome-repo
```

Create your branch 

```shell
$ git branch your-awesome-branch
```

Check it out

```shell
$ git checkout your-awesome-branch
```

If adding a folder use.

```shell
$ git add nameOfFolder/\\*
```

Make your commit and push to your new branch.

```shell
$ git add .
$ git commit -m 'initial commit'
$ git push origin your-awesome-branch
```

Manage the rest of the PR via GitHub

## Check remotes

```shell
git remote -v
```

## [Sync a remote fork](https://help.github.com/articles/syncing-a-fork/) on your machine

First configure the local to point to the remote upstream

```shell
$ git remote -v
$ git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
$ git remote -v
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
```

You then use `git merge` to update any branch on the upstream repository:

```shell
$ git merge upstream/dev
```

## Sync a remote fork on Github

1. Open your fork on GitHub.
2. Click on Pull Requests.
3. Click on New Pull Request. By default, GitHub will compare the original with your fork, and there shouldn’t be anything to compare if you didn’t make any changes.
4. Click on Try `switching the base`. Now GitHub will compare your fork with the original, and you should see all the latest changes.
5. Click on Click to create a pull request for this comparison and assign a predictable name to your pull request (e.g., Update from original).
6. Click on Send pull request.
7. Scroll down and click Merge pull request and finally Confirm merge. If your fork didn’t have any changes, you will be able to merge it automatically.

## 2fa

Using two factor authentication? Then use the following so you're not adding in your auth token each time you want to `push` your code.

```shell
git remote set-url origin https://yourgithubuser:your-token@github.com/yourgithubuser/yourrepo.git
```

## Change `origin` url

If you want to change the origin url you can use the `set-url` command 

```shell
git remote set-url origin https://github.com/user/new-repo-name
```

## [Add code on your machine to new repo](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)

Via terminal navigate to your code folder.

```shell
$ git init
```

Add your files.

```shell
$ git add .
```

Adding a folder use the following syntax or it'll get added as a BLOB.

```shell
$ git add nameOfFolder/\\*
```

Commit to local repo.

```shell
git commit -m 'some detailed message'
```

To add your files to the remote repo, [first add your remote repo](https://help.github.com/articles/adding-a-remote/)

```shell
$ git remote add origin [remote repository URL]
# Sets the new remote
$ git remote -v
# Verifies the new remote URL
$ git push origin master
```

## Delete local branch

```shell
$ git branch -D use-dotenv
```

## Merge two repos

If you want to merge project-a into project-b:

```shell
cd path/to/project-b
git remote add project-a path/to/project-a
git fetch project-a
git merge --allow-unrelated-histories project-a/master # or whichever branch you want to merge
git remote remove project-a
```

## Stop tracking a file

If you have `.env` files that are tracked by Git and want to ignore them so your API keys don't get added to GitHub use:

```shell
$ git update-index --assume-unchanged <file>
```

## Start tracking a previously un-tracked file

```shell
$ git update-index --no-assume-unchanged <file>
```

## Cloning a repo from someone else's GitHub and pushing it to a repo on my GitHub

So you make a clone, make some changes then realise that you need to add it to your GitHub account before making a pull

```shell
$ git remote -v
origin  https://github.com/OtherUser/OtherUserRepo (fetch)
origin  https://github.com/OtherUser/OtherUserRepo (push)
```

You just need to set the `origin` to yours then add the `upstream` as the original `origin` make sense?

So change `origin` to yours:

```shell
$ git remote set-url origin http://github.com/YourUser/YourRepo
```

Then add `upsrtream` as theirs:

```shell
$ git remote add upstream https://github.com/OtherUser/OtherUserRepo
```

Now it should look something like this:

```shell
$ git remote -v
origin  http://github.com/YourUser/YourRepo (fetch)
origin  http://github.com/YourUser/YourRepo (push)
upstream        https://github.com/OtherUser/OtherUserRepo (fetch)
upstream        https://github.com/OtherUser/OtherUserRepo (push)
```

## Clone a repo and give it a different name

```shell
$ git clone https://github.com/user/repoNameYouToChange NameYouWantToGiveToRepo
```

## Using Husky?

If you are pushing right after a commit, you can use `$ git push --no-verify` to avoid running all the tests again.

If you make a trivial change and want to commit `$ git commit -m 'some detailed message' --no-verify` will skip your `precommit` and `prepush` scripts.

## How to read last commit comment?

`$ git show` is the fastest to type, but shows you the diff as well.

`$ git log -1` is fast and simple.

`$ git log -1 --pretty=%B` if you need just the commit message and nothing else.

## Remove commit from pull request

Read [this](http://stackoverflow.com/questions/34519665/how-to-move-head-back-to-a-previous-location-detached-head/34519716#34519716) for more detail on how to revert.

This was the simplest approach I found:

```shell
# Checkout the desired branch
git checkout <branch>

# Undo the desired commit
git revert <commit>

# Update the remote with the undo of the code
git push origin <branch>
```

Rather than use the last part I unstaged the changes in VSCode which I think did the same thing.

## Show `.gitconfig` details

```shell
git config --list --show-origin
```

## If you want to rename a branch while pointed to any branch, do:

```sh
git branch -m <oldname> <newname>
```

If you want to rename the current branch, you can do:

```sh
git branch -m <newname>
```

A way to remember this, is `-m` is for "move" (or `mv`), which is how you rename files.