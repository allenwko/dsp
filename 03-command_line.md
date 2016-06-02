# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cd - navigate - ~, /dir/dir1, ..
pwd
env
ls
cp
mv
rm
find
man
exit

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls - lists the contents of the current directory
flags:
  -a: shows hidden files
  -l: shows a lot of additional information about the files
  -h: makes the output human readable
  -t: sorts by date last modified
  -G: does NOT display group information
  -p: adds "/" character to end of all directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

 -d: displays only directories
 -R: displays subdirectories
 -u: displays files by access time
 -x: displays by rows
 -1: display each entry by line

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is used to handle extremely large arguments, typically long filenames/directories

example:
 $ find . -name tempfiles | xargs rm -rf
 

