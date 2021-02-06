                                                                            
re                                                                                
 - search for a pattern/substring with in a given string                          
 - validate a given substring like password                                       
 - operations include match, search, findall, split, sub                          
                                                                                  
Sequence Characters                                                               
                                                                                  
digit         \d opp \D                                                           
space         \s opp \S                                                           
alphanumeric  \w opp \W                                                           
word boundary \b word boundary or space around words                              
                                                                                  
match at beg  \A                                                                  
of sting                                                                          
                                                                                  
match at end  \Z                                                                  
of string                                                                         
                                                                                  
Quantifiers:                                                                      
+ one or more                                                                     
? zero or one                                                                     
* zero or more                                                                    
{m} exactly m occurences of preceding regex                                       
{m,n} range of min -m amd max -n                                                  
                                                                                  
Special Characters                                                                
\ - escape, to look for special characters                                        
. - any character except new line                                                 
^ - match given regex at the beinning                                             
$ - match given regex at end of string                                            
[...] - range of val                                                              
[^...] - all chars except range                                                   
[A-Z]                                                                             
[a-z]                                                                          
[^A-Za-z]                                                                      
[^b]                                                                           
(..) - provide regex patter inside par, use groups()                           
(R | S) - match regex r or s                                                   
[ab] means a or b, single chracter                                             
[^abc] means not a or b or c                                                                                                                 
""" 
some_str = "oneHi, bring one idea to the table. Leave oneday"                  
                                                                               
# Find all occurences=, return a list, empty list if nothing found             
print(re.findall(r'o\w\w', some_str))                                          
                                                                               
# Check in the beginning only,returns None if not found                        
print(re.match(r'o\w\w', some_str))                                            
print(re.match(r'o\w\w', some_str).group())                                    
                                                                               
# Check for a pattern if exists, finds the one in beginning too else           
# returns None                                                                 
                                                                               
print(re.search(r'o\w\w', some_str))                                           
print(re.search(r'o\w\w', some_str).group())                                   
                                                                               
# split                                                                        
x = "HelloWorld\nHowareyou?"                                                   
print(re.split(r'\d',x))                                                       
print(re.split(r'\s',x))                                                       
                                                                               
# sub/replaceAll                                                               
x = "Hello, Hello again Again again!"                                          
print(re.sub(r'Hello','Bye', x))                                               
print(x) 

