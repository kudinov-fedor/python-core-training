# search substring
"aaaaa".count("a") # 5

"some good word".find("o") # 1
"some good word".find("some not existing string") # -1

"some good word".find("o", 2)  # 6
"some good word".rfind("o")  # 11
"some good word".rfind("o", 0, -3)  # 7

"some good word".index("o") # 1
"some good word".index("o", 2)  # 6
"some good word".rindex("o")  # 11
"some good word".rindex("o", 0, -3)  # 7


# Play with upper, lower case
"Hi".lower() # 'hi'
"hello world".capitalize() # 'Hello world'
"Hi".casefold() # 'hi'
"Hi".swapcase() # 'hI'
"hello world".title() # 'Hello World'
"hello world".upper() #'HELLO WORLD'


# remove or replace some parts
"  apple    ".strip() # 'apple'
"  apple    ".lstrip() # 'apple    '
"  apple    ".rstrip() # '  apple'

"Hello World".replace("Hello", "Hi") # 'Hi World'
"banana".replace("a", "o") # 'bonono'
"banana".replace("a", "") # 'bnn'

"super_item".removeprefix("super_") # 'item'
"useless".removesuffix("less") # 'use'

trans_table = str.maketrans({"o": "0",
                             "l": "1",
                             "b": "8",
                             "s": "5"})
"some base password".translate(trans_table)

# '50me 8a5e pa55w0rd'

# formatting                       https://pyformat.info/

a = "hello"
b = "world"
"%s %s %d" % (a, b, 15)  # old formating, rear used
"{} {}".format(a, b)  # common way to format
f"{a} {b}"  # latest way to format

"{} {}".format("hello", "world")
"{1} {0}".format("world", "hello", "some")
"{second} {first}".format(first="world", second="hello", other="some")

pattern = "{second} {first}".format(first="world", second="hello", other="some")
attrs = {"first": "world", "second": "hello", "other": "some"}
pattern.format(**attrs)


# 'join'
", ".join(["banana", "tomatoes", "apples"]) # 'banana, tomatoes, apples'


# split
"banana, tomatoes, apples".split(", ") # ['banana', 'tomatoes', 'apples']
"banana, tomatoes, apples".split(", ", maxsplit=1) # ['banana', 'tomatoes, apples']
"banana tomatoes apples".split() # ['banana', 'tomatoes', 'apples']

"val1|val2|val3".partition("|") # ('val1', '|', 'val2|val3')
"val1|val2|val3".rpartition("|") # ('val1|val2', '|', 'val3')

"line1\nline2\nline3".splitlines() # ['line1', 'line2', 'line3']
"line1\nline2\nline3".splitlines(keepends=True) # ['line1\n', 'line2\n', 'line3']


# when you need specific width
"apple".ljust(10) # 'apple     '
"apple".rjust(10) # '     apple'
"apple".center(10) # '  apple   '
"100".zfill(10) # '0000000100'


# different checks
"123abc".isalnum() # True
"123abc!@3".isalnum() # False
"abc".isalpha() # True
"123".isalpha() # False
"&*^".isalpha() # False
" ".isspace() # True
"Hi there".istitle() # False
"HI THERE".isupper() # True
"hi there".islower() # True
"HI THERE 123".isupper() # True
"hi there 123".islower() # True

"123".isdecimal()  # True
"123".isdigit() # True
"123".isnumeric() # True

"super task".startswith("super") # True
"complexity".endswith("ity") # True

"abc".isascii() # True
"ß∂åçßå".isascii() # False

"valid_identifier".isidentifier() # True
"123_invalid_identifier".isidentifier() # False

"\n".isprintable()  # False
"\\n".isprintable()  # True
r"\n".isprintable()  # True
