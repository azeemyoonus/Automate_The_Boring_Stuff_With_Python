Practice Questions


1.What is the function that creates Regex objects?

A.

	re.compile()


2.Why are raw strings often used when creating Regex objects?

A.

	Because  backslashes will be escaped.



3.What does the search() method return?

A.

	Match objects



4.How do you get the actual strings that match the pattern from a Match object?

A.

	By using group() method it will return strings of the matched text


5.In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

A.

	Group 0 covers the entire match,

	Group 1 covers the first set of  parenthesis  (\d\d\d)

	Group 2 covers the second set of parenthesis (\d\d\d-\d\d\d\d)


6.Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

A.

	By using escape sequence


7.The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

A.

	If the regex has no groups then list of strings is returned.If the regex has group then list of tuples of strings is returned



8.What does the | character signify in regular expressions?

A.

	It is pipe signifies matching "either, or" between two groups.


9.What two things does the ? character signify in regular expressions?

A.

	The ? character flags the group that precedes it an as an optional part of the the pattern


10.What is the difference between the + and * characters in regular expressions?

A.

	+ matches one or more 

	* matches zero or more



11.What is the difference between {3} and {3,5} in regular expressions?

A.

	{3} matches exactly three instances of the preceeding group.

	{3,5} matches between three and five instances .



12.What do the \d, \w, and \s shorthand character classes signify in regular expressions?

A.

	\d matches single digit

	\w matches word

	\s matches space 



13.What do the \D, \W, and \S shorthand character classes signify in regular expressions?

A.

	\D matches which is not single digit

	\W matches which is not word

	\S matches which is not space




14.What is the difference between .* and .*??

A.

	*  performs greedy match 

	*? performs non-greedy match




15.What is the character class syntax to match all numbers and lowercase letters?

A.

	Either [0-9a-z] or [a-z0-9]




16.How do you make a regular expression case-insensitive?

A.

	By passing re.I (or re.IGNORECASE) as the second argument to re.compile()




17.What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

A.

	The . character matches any character except the newline.If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters



18.If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

A.

	It will return the string 'X drummers, X pipers, five rings, X hens'.



19.What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

A.

	It will allows you to add whitespaces and comments to the string passed to re.compile().



20.How would you write a regex that matches a number with commas for every three digits? It must match the following:



	'42'

	'1,234'

	'6,368,745'


but not the following:


	'12,34,567' (which has only two digits between the commas)

	'1234' (which lacks commas)


A.

	re.compile(r'^\d{1,3}(,\d{3})*$')



21.How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:


	'Haruto Watanabe'

	'Alice Watanabe'

	'RoboCop Watanabe'



but not the following:



	'haruto Watanabe' (where the first name is not capitalized)

	'Mr. Watanabe' (where the preceding word has a nonletter character)

	'Watanabe' (which has no first name)

	'Haruto watanabe' (where Watanabe is not capitalized)



A.


	re.compile(r'[A-Z][a-z]*\sWatanable')




22.How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:


	'Alice eats apples.'

	'Bob pets cats.'

	'Carol throws baseballs.'

	'Alice throws Apples.'

	'BOB EATS CATS.'



but not the following:



	'RoboCop eats apples.'

	'ALICE THROWS FOOTBALLS.'

	'Carol eats 7 cats.'


A.

	re.compile(r'(Alice|bob|carol|)\s(eats|pets|throws)\s(apples|cats|baseballs)\',re.I)




	




