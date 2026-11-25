# Regular Expressions in Python

## Example #1

Are they bots?

The company that you are working for asked you to perform a sentiment analysis using a dataset with tweets. First of all, you need to do some cleaning and extract some information.
While printing out some text, you realize that some tweets contain user mentions. Some of these mentions follow a very strange pattern. A few examples that you notice: @robot3!, @robot5& and @robot7#

To analyze if those users are bots, you will do a proof of concept with one tweet and extract them using the .findall() method.

You write down some helpful metacharacters to help you later:

* `\d`: digit
* `\w`: word character
* `\W`: non-word character
* `\s`: whitespace

The text of one tweet was saved in the variable sentiment_analysis. You can use print(sentiment_analysis) to view it in the IPython Shell.

```python

sentiment_analysis = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

```

---

## Example #2

Find the numbers  

While examining the tweet text in your dataset, you detect that some tweets carry more information. The text contains the number of retweets, user mentions, and likes. You decide to extract this important information that is given as in this example:

Agh,snow! User_mentions:9, likes: 5, number of retweets: 4

You pull a list of metacharacters:\d digit,\w word character,\s whitespace.

Always indicate whitespace with metacharacters.

The variable sentiment_analysis containing the text of one tweet and the re module were loaded in your session. You can use print() to view it in the IPython Shell.

```python
import re

sentiment_analysis = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

# Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.
print(re.findall(r"likes:\s{1}\d", sentiment_analysis))

# Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis.
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

```

---

## Example #3

Match and split

Some of the tweets in your dataset were downloaded incorrectly. Instead of having spaces to separate words, they have strange characters. You decide to use regular expressions to handle this situation. You print some of these tweets to understand which pattern you need to match.

You notice that the sentences are always separated by a special character, followed by a number, the word break, and after that, another special character, e.g &4break!. The words are always separated by a special character, the word new, and a normal random character, e.g #newH.

The variable sentiment_analysis containing the text of one tweet, as well as the re module were already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell.

```python

sentiment_analysis = 'He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'

# Write a regex that matches the pattern separating the sentences in sentiment_analysis, e.g. &4break!.
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, ' ', sentiment_analysis)

# Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH.
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, ' ', sentiment_sub)
print(sentiment_final)

```

---

## Example #4

Everything clean

Back to your Twitter sentiment analysis project! There are several types of strings that increase your sentiment analysis complexity. But these strings do not provide any useful sentiment. Among them, we can have links and user mentions.

In order to clean the tweets, you want to extract some examples first. You know that most of the times links start with http and do not contain any whitespace, e.g. https://www.datacamp.com. User mentions start with @ and can have letters and numbers only, e.g. @johnsmith3.

You write down some helpful quantifiers to help you: * zero or more times, + once or more, ? zero or once.

The list sentiment_analysis containing the text of three tweets are already loaded in your session. You can use print() to view the data in the IPython Shell.

```python
# Import re module
import re

# Import re module
import re

for tweet in sentiment_analysis:
    print(tweet)
    # Write regex to match http links and print out result
    print(re.findall(r"https?://\S+", tweet))

    # Write regex to match user mentions and print out result
    print(re.findall(r"@\w+\d+\w+", tweet))
```

---

## Example #5

Some time ago

You are interested in knowing when the tweets were posted. After reading a little bit more, you learn that dates are provided in different ways. You decide to extract the dates using .findall() so you can normalize them afterwards to make them all look the same.

You realize that the dates are always presented in one of the following ways:

27 minutes ago

4 hours ago

23rd june 2018

1st september 2019 17:25

The list sentiment_analysis containing the text of three tweets, as well as the re module are already loaded in your session. You can use print() to view the data in the IPython Shell.

```python

# Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

# Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))

```

---

## Example #6

Getting tokens

Your next step is to tokenize the text of your tweets. Tokenization is the process of breaking a string into lexical units or, in simpler terms, words. But first, you need to remove hashtags so they do not cloud your process. You realize that hashtags start with a # symbol and contain letters and numbers but never whitespace. After that, you plan to split the text at whitespace matches to get the tokens.

You bring your list of quantifiers to help you: * zero or more times, + once or more, ? zero or once, {n, m} minimum n, maximum m.

The variable sentiment_analysis containing the text of one tweet as well as the re module are already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell.

```python

import re

sentiment_analysis = 'ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever'

# Regular expression for hashtags.
regex = r"#\w+"

# Replace all the matches of the regex with an empty string "". Assign it to no_hashtag variable.
no_hashtag = re.sub(regex, '', sentiment_analysis)

# Split the text in the no_hashtag variable at every match of one or more consecutive whitespace.
print(re.split(r"\s+", no_hashtag))

```

---

## Example #7

Finding files

You are not satisfied with your tweets dataset cleaning. There are still extra strings that do not provide any sentiment. Among them are strings that refer to text file names.

You also find a way to detect them:

They appear at the start of the string.
They always start with a sequence of 2 or 3 upper or lowercase vowels (a e i o u).
They always finish with the txt ending.
You are not sure if you should remove them directly. So you write a script to find and store them in a separate dataset.

You write down some metacharacters to help you: ^ anchor to beginning, . any character.

The variable sentiment_analysis containing the text of two tweets as well as the re module are already loaded in your session. You can use print() to view it in the IPython Shell.

```python

# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"
# regex = r"^[aeiouAEIOU]{2,3}.+\.txt$"

for text in sentiment_analysis:
    print(text)

    # Find all matches of the regex
    print(re.findall(regex, text))

    # Replace all matches with empty string
    print(re.sub(regex, '', text))

```

---

## Example #8

Give me your email

A colleague has asked for your help! When a user signs up on the company website, they must provide a valid email address.

The company puts some rules in place to verify that the given email address is valid:

* The first part can contain:
    - Upper A-Z or lowercase letters a-z
    - Numbers
    - Characters: `!`, `#`, `%`, `&`, `*`, `$`, `.`
* Must have `@`
* Domain:
    - Can contain any word characters
    - But only .com ending is allowed

The project consists of writing a script that checks if the email address follow the correct pattern. Your colleague gave you a list of email addresses as examples to test.

The list emails as well as the re module are loaded in your session. You can use print(emails) to view the emails in the IPython Shell.

```python

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*$\.]+@\w+\.com"

for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   

```

---

## Example #9

Invalid password

The second part of the website project is to write a script that validates the password entered by the user. The company also puts some rules in order to verify valid passwords:

* It can contain lowercase a-z and uppercase letters A-Z
* It can contain numbers
* It can contain the symbols: *, #, $, %, !, &, .
* It must be at least 8 characters long but not more than 20

Your colleague also gave you a list of passwords as examples to test.

The list passwords and the module re are loaded in your session. You can use print(passwords) to view them in the IPython Shell.

```python

# Write a regex to check if the password is valid
regex = r"[a-zA-Z0-9*#$%!&.]{8,20}"

for example in passwords:
    # Scan the strings to find a match
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
        print("The password {pass_example} is invalid".format(pass_example=example))

```

---

## Example #10

Understanding the difference between Greedy Match & Non-greedy Match

You need to keep working and cleaning your tweets dataset. You realize that there are some HTML tags present. You need to remove them but keep the inside content as they are useful for analysis.

Let's take a look at this sentence containing an HTML tag:

I want to see that <strong>amazing show</strong> again!.

You know that to get the HTML tag you need to match anything that sits inside angle brackets < >. But the biggest problem is that the closing tag has the same structure. If you match too much, you will end up removing key information. So you need to decide whether to use a greedy or a lazy quantifier.

The string is already loaded as string to your session.

```python

string = 'I want to see that <strong>amazing show</strong> again!'

string_notags = re.sub(r"<.+?>", "", string)
print(string_notags)

```


Explanation

```python
# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<\/?\w+>", "", string)

# Print out the result
print(string_notags)
```

Here the pattern `<\/?\w+>` is actually fine for simple tags like `<strong>` and `</strong>`.  
With `re.sub()` it would work too.  
It just wouldn't handle tags with attributes like `<a href="x">`.

```python
import re

string = "I want to see that <strong>amazing show</strong> again!"

# Greedy
string_notags = re.sub(r"<.+>", "", string)
print(string_notags)
# I want to see that  again!

# Non-greedy
string_notags = re.sub(r"<.+?>", "", string)
print(string_notags)
# I want to see that amazing show again!
```

---

### Greedy vs. non-greedy (lazy)  

- **Greedy** (`+`, `*`, `?`): match **as much as possible**
- **Lazy** (`+?`, `*?`, `??`): match **as little as possible**

Using `.+` between the angle brackets:

```python
string = "I want to see that <strong>amazing show</strong> again!"

re.findall(r"<.+>", string)
# ['<strong>amazing show</strong>']   greedy: one huge match
```

Greedy `.+` runs all the way to the end of the string, then backs up to the **last** `>`. So it swallows `<strong>amazing show</strong>` as a single match. Removing it would delete the content you wanted to keep.

```python
re.findall(r"<.+?>", string)
# ['<strong>', '</strong>']           lazy: two small matches
```

Lazy `.+?` stops at the **first** `>` it finds, so each tag is matched separately.

---

### Visual

```plaintext
I want to see that <strong>amazing show</strong> again!
                   ^___________________________^   greedy  <.+>
                   ^______^            ^_______^   lazy    <.+?>
```

---

### Alternative to lazy: a negated class

```python
re.sub(r"<[^>]+>", "", string)
```

`[^>]+` means "one or more characters that are not `>`", so it can't run past the first closing bracket. This is often faster and clearer than lazy matching.

---

> 💡 **Rule of thumb:** when you match "anything between two delimiters" and the delimiter can repeat, use a lazy quantifier (`.+?`) or a negated class (`[^>]+`). Use `re.sub()` to remove, `re.findall()` to extract, and `re.match()` only when the pattern must be at the start of the string.

---

## Example #11

Greedy matching  

Next, you see that numbers still appear in the text of the tweets. So, you decide to find all of them.

Let's imagine that you want to extract the number contained in the sentence I was born on April 24th. A lazy quantifier will make the regex return 2 and 4, because they will match as few characters as needed. However, a greedy quantifier will return the entire 24 due to its need to match as much as possible.

The re module as well as the variable sentiment_analysis are already loaded in your session. You can use print(sentiment_analysis) to view it in the IPython Shell.

```python

sentiment_analysis = 'Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left'

# Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

```

---

## Example #12

Lazy approach

You have done some cleaning in your dataset but you are worried that there are sentences encased in parentheses that may cloud your analysis.

Again, a greedy or a lazy quantifier may lead to different results.

For example, if you want to extract a word starting with a and ending with e in the string I like apple pie, you may think that applying the greedy regex a.+e will return apple. However, your match will be apple pie. A way to overcome this is to make it lazy by using ? which will return apple.

The re module and the variable sentiment_analysis are already loaded in your session.

```python

import re

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying)."

# Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
sentences_found_lazy = re.findall(r"\(.+?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

```

---

## Example #13

Try another name

You are still working on your Twitter sentiment analysis. You analyze now some things that caught your attention. You noticed that there are email addresses inserted in some tweets. Now, you are curious to find out which is the most common name.

You want to extract the first part of the email. E.g. if you have the email marysmith90@gmail.com, you are only interested in marysmith90.
You need to match the entire expression. So you make sure to extract only names present in emails. Also, you are only interested in names containing upper (e.g. A,B, Z) or lowercase letters (e.g. a, d, z) and numbers.

The list sentiment_analysis containing the text of three tweets as well as the re module were loaded in your session. You can use print() to view it in the IPython Shell.

```python

import re

sentiment_analysis = [
    'Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
    'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',
    'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com',
]

# Write a regex that matches email
regex_email = r"([\da-zA-Z]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))

```

---

## Example #14

Flying home

Your boss assigned you to a small project. They are performing an analysis of the travels people made to attend business meetings. You are given a dataset with only the email subjects for each of the people traveling.

You learn that the text followed a pattern. Here is an example:

Here you have your boarding pass LA4214 AER-CDB 06NOV.

You need to extract the information about the flight:

* The two letters indicate the airline (e.g LA),
* The 4 numbers are the flight number (e.g. 4214).
* The three letters correspond to the departure (e.g AER),
* The destination (CDB),
* The date (06NOV) of the flight.

All letters are always uppercase.

The variable flight containing one email subject was loaded in your session. You can use print() to view it in the IPython Shell.

```python

import re

flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

# Complete the regular expression to match and capture all the flight information required. Only the first parenthesis were placed for you.

regex = r"([A-Z]{2})([0-9]{4})\s([A-Z]{3})-([A-Z]{3})\s([0-9]{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

print(flight_matches)
# [('IB', '3723', 'AMS', 'MAD', '06OCT')]

#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

```

---

## Example #15

Love it!

You are still working on the Twitter sentiment analysis project. First, you want to identify positive tweets about movies and concerts.

You plan to find all the sentences that contain the words love, like, or enjoy and capture that word. You will limit the tweets by focusing on those that contain the words movie or concert by keeping the word in another group. You will also save the movie or concert name.

For example, if you have the sentence: I love the movie Avengers. You match and capture love. You need to match and capture movie. Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

### Completed code

```python
import re

sentiment_analysis = [
    "I totally love the concert The Book of Souls World Tour. It kinda amazing!",
    "I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.",
    "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."
]

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))
```

**Output:**  

```plaintext
Positive comments found [('love', 'concert', 'The Book of Souls World Tour')]
Positive comments found [('enjoy', 'movie', 'Wreck-It Ralph')]
Positive comments found [('like', 'movie', 'Wish Upon a Star')]
```

---

### How each blank is filled

**1. The regex: `(love|like|enjoy).+?(movie|concert)\s(.+?)\.`**

| Part | Meaning |
|---|---|
| `(love\|like\|enjoy)` | Group 1: captures one of the three words (`\|` means "or") |
| `.+?` | Lazy match of the text in between (` the `, ` totally love the ` etc.) |
| `(movie\|concert)` | Group 2: captures the word movie or concert |
| `\s` | One whitespace after it |
| `(.+?)` | Group 3: captures the name, lazily |
| `\.` | Literal dot that ends the match (escaped, since a bare `.` means any character) |

**2. The function: `re.findall(regex_positive, tweet)`**

`re.findall(pattern, string)` takes the pattern first, then the string. When the pattern has **multiple groups**, it returns a list of **tuples**, one value per group.

**3. The `.format()`:** `{}` is the placeholder, and `positive_matches` is passed into `.format()`.

---

### Why lazy `.+?` matters here

In the original template, the blank sits inside `.+?`, so the lazy version is intended. With a greedy `(.+)` as the last group, the match would run to the **last** dot in the tweet. For the third tweet it would capture `Wish Upon a Star. Too bad Disney doesn't show it anymore` instead of just `Wish Upon a Star`.

---

> 💡 **Remember:** `findall` returns the whole match when there are no groups, a list of strings when there is one group, and a list of tuples when there are two or more groups.

---

## Example #16

Ugh! Not for me!

After finding positive tweets, you want to do it for negative tweets. Your plan now is to find sentences that contain the words hate, dislike or disapprove. You will again save the movie or concert name. You will get the tweet containing the words movie or concert but this time, you don't plan to save the word.

For example, if you have the sentence: I dislike the movie Avengers a lot.. You match and capture dislike. You will match but not capture the word movie. Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets as well as the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

sentiment_analysis = [
    "That was horrible! I really dislike the movie The cabin and the ant. So boring.",
    "I disapprove the movie Honest with you. It's full of cliches.",
    "I dislike very much the concert After twelve Tour. The sound was horrible.",
]

# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)

    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))

```

---

## Example #17

Parsing PDF files

You now need to work on another small project you have been delaying. Your company gave you some PDF files of signed contracts. The goal of the project is to create a database with the information you parse from them. Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). You decide to use capturing groups to extract this information. Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept.

The variable contract containing the text of one contract and the re module are already loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

contract = "Provider will invoice Client for Services performed within 30 days of performance.  Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. It is understood that payments to Provider for services rendered shall be made in full as agreed, without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001."

# Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"

dates = re.search(regex_dates, contract)

print(dates)

# Assign to each key the corresponding match
signature = {
    "day": dates.group(2),
    "month": dates.group(1),
    "year": dates.group(3)
}

# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))

```

---

## Example #18

Close the tag, please!

In the meantime, you are working on one of your other projects. The company is going to develop a new product. It will help developers automatically check the code they are writing. You need to write a short script for checking that every HTML tag that is open has its proper closure.

You have an example of a string containing HTML tags:

<title>The Data Science Company</title>

You learn that an opening HTML tag is always at the beginning of the string. It appears inside <>. A closing tag also appears inside <>, but it is preceded by /.

You also remember that capturing groups can be referenced using numbers, e.g \4.

The list html_tags, containing three strings with HTML tags, and there module are loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

html_tags = [
    '<body>Welcome to our course! It would be an awesome experience</body>',
    '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>',
    '<nav>About me Links Contact me!'
]

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)

    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))

```

---

## Example #19

Reeepeated characters

Back to your sentiment analysis! Your next task is to replace elongated words that appear in the tweets. We define an elongated word as a word that contains a repeating character twice or more times. e.g. "Awesoooome".

Replacing those words is very important since a classifier will treat them as a different term from the source words lowering their frequency.

To find them, you will use capturing groups and reference them back using numbers. E.g \4.

If you want to find a match for Awesoooome. You first need to capture Awes. Then, match o and reference the same character back, and then, me.

The list sentiment_analysis, containing the text of three tweets, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

sentiment_analysis = [
    "@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times",
    "Staying at a friends house...neighborrrrrrrs are so loud-having a party",
    "Just woke up an already have read some e-mail"
]

# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1+\w*"

for tweet in sentiment_analysis:
    # Find if there is a match in each tweet 
    match_elongated = re.search(regex_elongated, tweet)

    if match_elongated:
        # Assign the captured group zero 
        elongated_word = match_elongated.group(0)

        # Complete the format method to print the word
        print("Elongated word found: {word}".format(word=elongated_word))
    else:
        print("No elongated word found")

```

**`regex_elongated = r"\w*(\w)\1+\w*"` is correct** for matching a word that contains a character repeated at least twice in a row (for example, `"oo"` in `"sooo"` gives 1 capture + 1 backreference = 2 total, and `"ooo"` in `"Awesoooome"` gives 1 capture + 2 backreferences = 3 total).

---

### Step-by-Step Breakdown of `r"\w*(\w)\1+\w*"`

1. **`\w*`** — Matches **zero or more** word characters (letters, digits, or underscores) *before* the repeated character. For `"Awesoooome"`, this matches `"Awes"`. Because it uses `*` (zero or more), it also works if a word starts right away with the repeated character (like `"oooh"`).
2. **`(\w)`** — A **capturing group** that matches a single word character and saves it as group `1`. In `"Awesoooome"`, this captures the first `"o"`.
3. **`\1+`** — A **backreference** to capturing group `1` followed by `+` (one or more). This requires the *exact same character* to appear at least one more time immediately after the captured character. Combined with `(\w)`, `(\w)\1+` matches **two or more** identical consecutive characters (`"oo"` or `"ooo"`).
4. **`\w*`** — Matches **zero or more** remaining word characters *after* the repeated run so the entire word is captured. For `"Awesoooome"`, this matches `"me"`.

---

* **`re.search(regex_elongated, tweet)`** scans each tweet for the first match of the pattern and returns a `Match` object (or `None` if no elongated word is present).
* **`match_elongated.group(0)`** returns the entire substring matched by the regex (group `0` is always the full match; group `1` would be only the single character captured by `(\w)`).

---

## Example #20

Surrounding words

Now, you want to perform some visualizations with your sentiment_analysis dataset. You are interested in the words surrounding python. You want to count how many times a specific word appears right before and after it.

Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression. Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.

The variable sentiment_analysis, containing the text of one tweet, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.

# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.
# Positive lookbehind
# look_behind = re.findall(r"(?<=python\s|Python\s)\w+", sentiment_analysis)
look_behind = re.findall(r"(?<=[pP]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)

```

---

## Example #21

Filtering phone numbers

Now, you need to write a script for a cell-phone searcher. It should scan a list of phone numbers and return those that meet certain characteristics.

The phone numbers in the list have the structure:

Optional area code: 3 numbers
Prefix: 4 numbers
Line number: 6 numbers
Optional extension: 2 numbers
E.g. 654-8764-439434-01.

You decide to use .findall() and the non-capturing group's negative lookahead (?!) and negative lookbehind (?<!).

The list cellphones, containing three phone numbers, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

```python

import re

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

# Get all cell phones numbers that are not preceded by the optional area code.
for phone in cellphones:
    number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
    # OR
    # number = re.findall(r"(?<!\d{3}-)(?<!\d)\d{4}-\d{6}(?:-\d{2})?", phone)

    print(number)

# Get all the cell phones numbers that are not followed by the optional extension.
for phone in cellphones:
    # Get all phone numbers not followed by optional extension
    number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
    print(number)

```
