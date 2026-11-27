# Chapter #2: Manipulating data

**Index**  

1. How can I view a file's contents?
2. How can I view a file's contents piece by piece?
3. How can I look at the start of a file?
4. How can I type less?
5. How can I control what commands do?
6. How can I list everything below a directory?
7. How can I get help for a command?
8. How can I select columns from a file?
9. What can't cut do?
10. How can I repeat commands?
11. How can I select lines containing specific values?

---

## #1 How can I view a file's contents?

Before you rename or delete files, you may want to have a look at their contents. The simplest way to do this is with `cat`, which just prints the contents of files onto the screen. (Its name is short for "concatenate", meaning "to link things together", since it will print all the files whose names you give it, one after the other.)

```bash
cat agarwal.txt

name: Agarwal, Jasmine
position: RCT2
start: 2017-04-01
benefits: full
```

---

## #2 How can I view a file's contents piece by piece?

You can use `cat` to print large files and then scroll through the output, but it is usually more convenient to **page** the output. The original command for doing this was called `more`, but it has been superseded by a more powerful command called `less`. (This kind of naming is what passes for humor in the Unix world.) When you `less` a file, one page is displayed at a time; you can press `spacebar` to page down or type `q` to quit.

If you give `less` the names of several files, you can type `:n` (colon and a lower-case 'n') to move to the next file, `:p` to go back to the previous one, or `:q` to quit.

Note: If you view solutions to exercises that use `less`, you will see an extra command at the end that turns paging off so that we can test your solutions efficiently.

---

## #3 How can I look at the start of a file?

The first thing most data scientists do when given a new dataset to analyze is figure out what fields it contains and what values those fields have. If the dataset has been exported from a database or spreadsheet, it will often be stored as comma-separated values (CSV). A quick way to figure out what it contains is to look at the first few rows.

We can do this in the shell using a command called `head`. As its name suggests, it prints the first few lines of a file (where "a few" means 10), so the command:

`head seasonal/summer.csv`  

displays:

```bash
Date,Tooth
2017-01-11,canine
2017-01-18,wisdom
2017-01-21,bicuspid
2017-02-02,molar
2017-02-27,wisdom
2017-02-27,wisdom
2017-03-07,bicuspid
2017-03-15,wisdom
2017-03-20,canine
```

What does `head` do if there aren't 10 lines in the file? (To find out, use it to look at the top of `people/agarwal.txt`.)

Display as many lines as there are.  

```bash
$ head people/agarwal.txt 
name: Agarwal, Jasmine
position: RCT2
start: 2017-04-01
benefits: full
$ 
$ 
```

---

## #4 How can I type less?

One of the shell's power tools is **tab completion**. If you start typing the name of a file and then press the tab key, the shell will do its best to auto-complete the path. For example, if you type `sea` and press `tab`, it will fill in the directory name `seasonal/` (with a trailing slash). If you then type `a` and `tab`, it will complete the path as `seasonal/autumn.csv`.

If the path is ambiguous, such as `seasonal/s`, pressing `tab` a second time will display a list of possibilities. Typing another character or two to make your path more specific and then pressing `tab` will fill in the rest of the name.

---

## #5 How can I control what commands do?

You won't always want to look at the first 10 lines of a file, so the shell lets you change `head`'s behavior by giving it a command-line flag (or just "flag" for short). If you run the command:

`head -n 3 seasonal/summer.csv`  

`head` will only display the first three lines of the file. If you run `head -n 100`, it will display the first 100 (assuming there are that many), and so on.

A flag's name usually indicates its purpose (for example, `-n` is meant to signal "number of lines"). Command flags don't have to be a `-` followed by a single letter, but it's a widely-used convention.

Note: it's considered good style to put all flags before any filenames, so in this course, we only accept answers that do that.

---

## #6 How can I list everything below a directory?

In order to see everything underneath a directory, no matter how deeply nested it is, you can give `ls` the flag `-R` (which means "recursive"). If you use `ls -R` in your home directory, you will see something like this:

```bash
backup          course.txt      people          seasonal

./backup:

./people:
agarwal.txt

./seasonal:
autumn.csv      spring.csv      summer.csv      winter.csv
```

This shows every file and directory in the current level, then everything in each sub-directory, and so on.

To help you know what is what, `ls` has another flag `-F` that prints a `/` after the name of every directory and a `*` after the name of every runnable program. Run `ls` with the two flags, `-R` and `-F`, and the absolute path to your home directory to see everything it contains. (The order of the flags doesn't matter, but the directory name must come last.)

```bash

ls -R -F /home/repl

```

Output  

```bash
$ pwd
/home/repl
$ cd ~
$ pwd
/home/repl
$ ls -R -F /home/repl
/home/repl:
backup/  bin/  course.txt  people/  seasonal/

/home/repl/backup:

/home/repl/bin:

/home/repl/people:
agarwal.txt

/home/repl/seasonal:
autumn.csv  spring.csv  summer.csv  winter.csv
$ 
$ 
```

---

## #7 How can I get help for a command?

To find out what commands do, people used to use the `man` command (short for "manual"). For example, the command `man head` brings up this information:

```bash
HEAD(1)               BSD General Commands Manual              HEAD(1)

NAME
     head -- display first lines of a file

SYNOPSIS
     head [-n count | -c bytes] [file ...]

DESCRIPTION
     This filter displays the first count lines or bytes of each of
     the specified files, or of the standard input if no files are
     specified.  If count is omitted it defaults to 10.

     If more than a single file is specified, each file is preceded by
     a header consisting of the string ``==> XXX <=='' where ``XXX''
     is the name of the file.

SEE ALSO
     tail(1)
```

`man` automatically invokes `less`, so you may need to press `spacebar` to page through the information and `:q` to quit.

The one-line description under `NAME` tells you briefly what the command does, and the summary under `SYNOPSIS` lists all the flags it understands. Anything that is optional is shown in square brackets `[...]`, either/or alternatives are separated by `|`, and things that can be repeated are shown by `...`, so `head`'s manual page is telling you that you can either give a line count with `-n` or a byte count with `-c`, and that you can give it any number of filenames.

The problem with the Unix manual is that you have to know what you're looking for. If you don't, you can search Stack Overflow, ask a question on DataCamp's Slack channels, or look at the `SEE ALSO` sections of the commands you already know.

---

## #8 How can I select columns from a file?

`head` and `tail` let you select rows from a text file. If you want to select columns, you can use the command `cut`. It has several options (use `man cut` to explore them), but the most common is something like:

`cut -f 2-5,8 -d , values.csv`

which means "select columns 2 through 5 and columns 8, using comma as the separator". `cut` uses `-f` (meaning "fields") to specify columns and `-d` (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

What command will select the first column (containing dates) from the file `spring.csv`?

```bash

$ head seasonal/spring.csv 
Date,Tooth
2017-01-25,wisdom
2017-02-19,canine
2017-02-24,canine
2017-02-28,wisdom
2017-03-04,incisor
2017-03-12,wisdom
2017-03-14,incisor
2017-03-21,molar
2017-04-29,wisdom
$ 
$ 
$ cut -f 1 -d , seasonal/spring.csv 
Date
2017-01-25
2017-02-19
2017-02-24
2017-02-28
2017-03-04
2017-03-12
2017-03-14
2017-03-21
2017-04-29
2017-05-08
2017-05-20
2017-05-21
2017-05-25
2017-06-04
2017-06-13
2017-06-14
2017-07-10
2017-07-16
2017-07-23
2017-08-13
2017-08-13
2017-08-13
2017-09-07
$ 
$ 
$ cut -d , -f 1 seasonal/spring.csv 
Date
2017-01-25
2017-02-19
2017-02-24
2017-02-28
2017-03-04
2017-03-12
2017-03-14
2017-03-21
2017-04-29
2017-05-08
2017-05-20
2017-05-21
2017-05-25
2017-06-04
2017-06-13
2017-06-14
2017-07-10
2017-07-16
2017-07-23
2017-08-13
2017-08-13
2017-08-13
2017-09-07
$ 
$ 
```

---

## #9 What can't cut do?

`cut` is a simple-minded command. In particular, it doesn't understand quoted strings. If, for example, your file is:

everyone.csv  

```plaintext
Name,Age
"Johel,Ranjit",28
"Sharma,Rupinder",26
```

then:

```bash
cut -f 2 -d , everyone.csv
```

will produce:

```bash
Age
Ranjit"
Rupinder"
```

rather than everyone's age, because it will think the comma between last and first names is a column separator.

What is the output of `cut -d : -f 2-4` on the line:

```bash
first:second:third:
```

(Note the trailing colon.)

Output  

```bash
$ cut -d : -f 2-4
first:second:third:
second:third:
```

---

## #10 How can I repeat commands?

One of the biggest advantages of using the shell is that it makes it easy for you to do things over again. If you run some commands, you can then press the up-arrow key to cycle back through them. You can also use the left and right arrow keys and the delete key to edit them. Pressing return will then run the modified command.

Even better, `history` will print a list of commands you have run recently. Each one is preceded by a serial number to make it easy to re-run particular commands: just type `!55` to re-run the 55th command in your history (if you have that many). You can also re-run a command by typing an exclamation mark followed by the command's name, such as `!head` or `!cut`, which will re-run the most recent use of that command.

---

## #11 How can I select lines containing specific values?

`head` and `tail` select rows, `cut` selects columns, and `grep` selects lines according to what they contain. In its simplest form, `grep` takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text. For example, `grep bicuspid seasonal/winter.csv` prints lines from `winter.csv` that contain "bicuspid".

`grep` can search for patterns as well; we will explore those in the next course. What's more important right now is some of `grep`'s more common flags:

* `-c`: print a count of matching lines rather than the lines themselves
* `-h`: do not print the names of files when searching multiple files
* `-i`: ignore case (e.g., treat "Regression" and "regression" as matches)
* `-l`: print the names of files that contain matches, not the matches
* `-n`: print line numbers for matching lines
* `-v`: invert the match, i.e., only show lines that don't match

Print the contents of all of the lines containing the word "molar" in `seasonal/autumn.csv` by running a single command while in your home directory. Don't use any flags.

```bash
$ 
$ grep molar seasonal/autumn.csv 
2017-02-01,molar
2017-05-25,molar
$ 
$ 
```

Invert the match to find all of the lines that don't contain the word "molar" in `seasonal/spring.csv`, and show their line numbers. Remember, it's considered good style to put all of the flags before other values like filenames or the search term "molar".

```bash
$ 
$ 
$ grep -v -n molar seasonal/spring.csv 
1:Date,Tooth
2:2017-01-25,wisdom
3:2017-02-19,canine
4:2017-02-24,canine
5:2017-02-28,wisdom
6:2017-03-04,incisor
7:2017-03-12,wisdom
8:2017-03-14,incisor
10:2017-04-29,wisdom
11:2017-05-08,canine
12:2017-05-20,canine
13:2017-05-21,canine
14:2017-05-25,canine
16:2017-06-13,bicuspid
17:2017-06-14,canine
18:2017-07-10,incisor
19:2017-07-16,bicuspid
20:2017-07-23,bicuspid
21:2017-08-13,bicuspid
22:2017-08-13,incisor
23:2017-08-13,wisdom
$ 
$ 
```

Count how many lines contain the word "incisor" in `autumn.csv` and `winter.csv` combined. (Again, run a single command from your home directory.)

```bash
$ 
$ 
$ grep -c incisor seasonal/autumn.csv seasonal/winter.csv 
seasonal/autumn.csv:3
seasonal/winter.csv:6
$ 
$ 
```

---

## #12 Why isn't it always safe to treat data as text?

The `SEE ALSO` section of the manual page for `cut` refers to a command called `paste` that can be used to combine data files instead of cutting them up.

Read the manual page for `paste`, and then run `paste` to combine the "autumn" and "winter" data files in a single table using a comma as a separator.  

What's wrong with the output from a data analysis point of view?

The last few rows have the wrong number of columns.

```bash
$ 
$ 
$ paste -d , seasonal/autumn.csv seasonal/winter.csv 
Date,Tooth,Date,Tooth
2017-01-05,canine,2017-01-03,bicuspid
2017-01-17,wisdom,2017-01-05,incisor
2017-01-18,canine,2017-01-21,wisdom
2017-02-01,molar,2017-02-05,molar
2017-02-22,bicuspid,2017-02-17,incisor
2017-03-10,canine,2017-02-25,bicuspid
2017-03-13,canine,2017-03-12,incisor
2017-04-30,incisor,2017-03-25,molar
2017-05-02,canine,2017-03-26,incisor
2017-05-10,canine,2017-04-04,canine
2017-05-19,bicuspid,2017-04-18,canine
2017-05-25,molar,2017-04-26,canine
2017-06-22,wisdom,2017-04-26,molar
2017-06-25,canine,2017-04-26,wisdom
2017-07-10,incisor,2017-04-27,canine
2017-07-10,wisdom,2017-05-08,molar
2017-07-20,incisor,2017-05-13,bicuspid
2017-07-21,bicuspid,2017-05-14,wisdom
2017-08-09,canine,2017-06-17,canine
2017-08-16,canine,2017-07-01,incisor
,2017-07-17,canine
,2017-08-10,incisor
,2017-08-11,bicuspid
,2017-08-11,wisdom
,2017-08-13,canine
$ 
$ 
```
