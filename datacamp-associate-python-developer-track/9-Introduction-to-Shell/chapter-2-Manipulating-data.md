# Chapter #2: Manipulating data

**Index**  

1. How can I view a file's contents?
2. How can I view a file's contents piece by piece?

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
