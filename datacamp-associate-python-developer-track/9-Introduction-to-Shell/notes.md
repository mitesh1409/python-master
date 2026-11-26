# Introduction to Shell

**Index**  

1. How does the shell compare to a desktop interface?
2. How can I move up a directory?

---

## #1 How does the shell compare to a desktop interface?

An operating system like Windows, Linux, or Mac OS is a special kind of program. It controls the computer's processor, hard drive, and network connection, but its most important job is to run other programs.

Since human beings aren't digital, they need an interface to interact with the operating system. The most common one these days is a graphical file explorer, which translates clicks and double-clicks into commands to open files and run programs. Before computers had graphical displays, though, people typed instructions into a program called a command-line shell. Each time a command is entered, the shell runs some other programs, prints their output in human-readable form, and then displays a prompt to signal that it's ready to accept the next command. (Its name comes from the notion that it's the "outer shell" of the computer.)

Typing commands instead of clicking and dragging may seem clumsy at first, but as you will see, once you start spelling out what you want the computer to do, you can combine old commands to create new ones and automate repetitive operations with just a few keystrokes.

Q: What is the relationship between the graphical file explorer that most people use and the command-line shell?

A: They are both interfaces for issuing commands to the operating system.

### Exercise #1

Where am I?

The filesystem manages files and directories (or folders). Each is identified by an absolute path that shows how to reach it from the filesystem's root directory: `/home/repl` is the directory `repl` in the directory `home`, while `/home/repl/course.txt` is a file `course.txt` in that directory, and `/` on its own is the root directory.

To find out where you are in the filesystem, run the command `pwd` (short for "print working directory"). This prints the absolute path of your current working directory, which is where the shell runs commands and looks for files by default.

Open your CLI and run `pwd`. Check where are you right now.

### Exercise #2

How can I identify files and directories?

`pwd` tells you where you are. To find out what's there, type `ls` (which is short for "listing") and press the enter key. On its own, `ls` lists the contents of your current directory (the one displayed by `pwd`). If you add the names of some files, `ls` will list them, and if you add the names of directories, it will list their contents. For example, `ls /home/repl` shows you what's in your starting directory (usually called your home directory).

Open your CLI. Use `ls` with an appropriate argument to list the files in the directory.

### Exercise #3

How else can I identify files and directories?

An absolute path is like a latitude and longitude: it has the same value no matter where you are. A relative path, on the other hand, specifies a location starting from where you are: it's like saying "20 kilometers north".

As examples:

* If you are in the directory `/home/repl`, the relative path `seasonal` specifies the same directory as the absolute path `/home/repl/seasonal`.

* If you are in the directory `/home/repl/seasonal`, the relative path `winter.csv` specifies the same file as the absolute path `/home/repl/seasonal/winter.csv`.

The shell decides if a path is absolute or relative by looking at its first character: If it begins with `/`, it is absolute. If it does not begin with `/`, it is relative.

### Exercise #4

How can I move to another directory?

Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command `cd` (which stands for "change directory").

If you type `cd seasonal` and then type `pwd`, the shell will tell you that you are now in `/home/repl/seasonal`. If you then run `ls` on its own, it shows you the contents of `/home/repl/seasonal`, because that's where you are. If you want to get back to your home directory `/home/repl`, you can use the command `cd /home/repl` or `cd ..`.

### Commands Learned

`pwd`  
"print working directory".  
It prints your present/current working directory (absolute path).  
That way you can know your current location on the file system.

`ls`  
It lists the contents of your current directory (the one displayed by `pwd`).
`ls /home/mitesh`  
You can also provide absolute or relative path after `ls`,  
it will show contents of that directory.  

`cd`
Lets you change directory.  
`cd /home/projects`  
You can provide abosolute or relative path after `cd`,  
it will change the directory accordingly.

---

## #2 How can I move up a directory?

The parent of a directory is the directory above it. For example, /home is the parent of /home/repl, and /home/repl is the parent of /home/repl/seasonal. You can always give the absolute path of your parent directory to commands like cd and ls. More often, though, you will take advantage of the fact that the special path .. (two dots with no spaces) means "the directory above the one I'm currently in". If you are in /home/repl/seasonal, then cd .. moves you up to /home/repl. If you use cd .. once again, it puts you in /home. One more cd .. puts you in the root directory /, which is the very top of the filesystem. (Remember to put a space between cd and .. - it is a command and a path, not a single four-letter command.)

A single dot on its own, ., always means "the current directory", so ls on its own and ls . do the same thing, while cd . has no effect (because it moves you into the directory you're currently in).

One final special path is ~ (the tilde character), which means "your home directory", such as /home/repl. No matter where you are, ls ~ will always list the contents of your home directory, and cd ~ will always take you home.

### Commands Learned

`cd ..`  
Takes you one level up from the current directory.

`cd ~`  
Takes you to your home directory.

