# Regex

Mini language to search for text patterns

## re.compile()

- to create a regex object

## re.search()

- returns the first match object
- also if match object exists or not
- mo.group() gives the match found
- if match object 

## re.findall()

- returns a list of all matches

## regex groups and pipe character

- to create groups use parenthesis ()
- the whole match  is group(0)
- the first group is group 1
- if you need to match parenthesis you  need to escape them
- the pipe character can be used to match many possible groups

## repetition in regex pattern ,greedy / non greedy matching

- match certain number of repetition of groups
- (pattern)? zero or one, may be the pattern in optional
- (pattern)+ one or more time
- (pattern)* zero or more time
- (pattern){2, 3} - atleast 2 and atmost 3
- (pattern){,2} - atleast zero and atmost 2
- (pattern){2,} - atleast two or more
- by default curly brances in (pattern){2, 3} look for longest
  string matching the pattern ie 3 this is known as greedy matching
- for non greedy match put a question mark after pattern
  (pattern){2,3}?
- to look for patterns containing ?, *, + , you need to escape them
- with findall use only zero or one grouping if possible
  if two or more groups are used, find all returns a list of tuples

## character classes
- \d = digit, same as saying (0|1|2|3|4|5|6|7|8|9)
- \w = word character , numbers, alphabets and underscore
       does not include punctuation marks
- \s tab, space or new line
- \D non digit
- \W non word
- \S non space
- custom character classes are in square brackets
- (a|e|i|o|u|A|E|I|O|U) is same as [aeiouAEIOU]
- look for pattern that has 2 vowerls [aeiou]{2}
- other character classes [a-zA-Z], [0-9]
- negative character classes [^aeiou]

## dot star and carrot characters
-  r'^helloo'
-  r'world!$'
-  r'^\d+$' - 123456789, 123456x789101
-  wild card dot char - . = any char except new line
-  r '.at'
-  r'(.*)' - any pattern (greedy mode)
-  (.*?) - non greedy mode
-  re.search(r'.*', re.DOTALL) // Includes new line as well
-  re.search(r'[AEIOU]', re.I) // IGNORECASE / CASE INSENSITIVE

## sub method and verbose mode
- re.sub(ro or patter, 'replace_with', string)
- \1 \2 to subsiste group in regex pattern
- re.VERBOSE with re.compile
- use verbose with r'''to add new line'''
- multiple options re.DOTALL | re.IGNORECASE | re.VERBOSE
