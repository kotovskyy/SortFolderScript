# Sort Your Folder

This tiny script sorts any folder you pass to it.
Currently it has been tested on Linux only.

## Functionality 

It's main functions are:

- For directories:
    1. Remove all empty directories in given path
- For regular files:
    1. Get every file's extension
    2. Create folders for every extension
    3. Move files to matching folders

## How to use

### Python Script

You can always use it as a python script. In terminal window write:

`python sortFolder.py /dir/to/sort`

### Bash Command

More useful way to use this script (in my humble opinion) is creation
of custom Linux command, so we can invoke the script with just writing
it's name. Here is how we you can do it:

- **Setting up path variable**
1. In your home directory create 'bin' directory:
`mkdir ~/bin`
2. Update path variable to include '~/bin/' directory. In order to do this
in your *home* directory open *.bash_profile* or *.profile* and paste this 
code:<br>
`if [ -d "$HOME/bin" ] ; then PATH="$HOME/bin:$PATH"; fi`

- **Creating bash script**

1. In *~/bin* folder create a script *sortFolder.sh* (you can choose whatever
name you want it to be):<br>
`touch ~/bin/sortFolder.sh`
2. Give execute permission to the script:
`chmod +x ~/bin/sortFolder.sh`
3. Put this code into the script (remember to use actual path to the script):

```bash
#!/bin/sh
python /path/to/python/script $1
```

4. Save your scipt file

Now from any directory you can simply use:
`sortFolder.sh /path/to/dir`

## Important notes

- All files in given folder must have extensions. Otherwise script
throws *IndexError*
- If path is not specified **current directory** will be sorted.