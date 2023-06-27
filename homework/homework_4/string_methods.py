# 'encode',
# 'capitalize', 'casefold', 'swapcase',  'title', 'upper', 'lower',
#
# 'join','removeprefix', 'removesuffix', 'replace', 'splitlines', 'zfill', 'center',
# 'expandtabs', 'count', 'format', 'format_map', 'maketrans', 'translate',
#
# 'find',  'index',  'ljust',  'partition',  'split',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'strip', 'lstrip', 'rstrip',
#
# 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
#  'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'startswith', 'endswith'


# search substring
"aaaaa".count("a")

"some good word".find("o")
"some good word".find("some not existing string")

"some good word".find("o", 2)  # starting from 3rd position
"some good word".find("o", 2)  # starting from 3rd position
"some good word".rfind("o")  # from right to left
"some good word".rfind("o", 0, -3)  # from right to left, ignore last 3 chars

"some good word".index("o")
"some good word".index("o", 2)  # starting from 3rd position
"some good word".index("o", 2)  # starting from 3rd position
"some good word".rindex("o")  # from right to left
"some good word".rindex("o", 0, -3)  # from right to left, ignore last 3 chars


# Play with upper, lower case
"Hi".lower()
"hello world".capitalize()
"Hi".casefold()
"Hi".swapcase()
"hello world".title()
"hello world".upper()


# remove or replace some parts
"  apple    ".strip()
"  apple    ".lstrip()
"  apple    ".rstrip()

"Hello World".replace("Hello", "Hi")
"banana".replace("a", "o")
"banana".replace("a", "o")
"banana".replace("a", "")

"super_item".removeprefix("super_")
"useless".removesuffix("less")

trans_table = str.maketrans({"o": "0",
                             "l": "1",
                             "b": "8",
                             "s": "5"})
"some base password".translate(trans_table)


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
", ".join(["banana", "tomatoes", "apples"])


# split
"banana, tomatoes, apples".split(", ")
"banana, tomatoes, apples".split(", ", maxsplit=1)
"banana tomatoes apples".split()

"val1|val2|val3".partition("|")
"val1|val2|val3".rpartition("|")

"line1\nline2\nline3".splitlines()
"line1\nline2\nline3".splitlines(keepends=True)


# when you need specific width
"apple".ljust(10)
"apple".rjust(10)
"apple".center(10)
"100".zfill(10)


# different checks
"123abc".isalnum()
"123abc!@3".isalnum()
"abc".isalpha()
"123".isalpha()
"&*^".isalpha()
" ".isspace()
"Hi there".istitle()
"HI THERE".isupper()
"hi there".islower()
"HI THERE 123".isupper()
"hi there 123".islower()

"123".isdecimal()  # https://miguendes.me/python-isdigit-isnumeric-isdecimal
"123".isdigit()
"123".isnumeric()

"super task".startswith("super")
"complexity".endswith("ity")

"abc".isascii()
"ß∂åçßå".isascii()

"valid_identifier".isidentifier()
"123_invalid_identifier".isidentifier()

"\n".isprintable()  # end of line
"\\n".isprintable()  # \n
r"\n".isprintable()  # \n
