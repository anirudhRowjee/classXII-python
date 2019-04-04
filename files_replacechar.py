# character replacer

def replace_char_by_char(source, char_tbr, repl_char):
    f = open(source, 'r+')
    chars = f.read()
    replace(chars, char_tbr, repl_char)
    f.write(chars)
    f.close()

source = input("enter file path>>")
c_tbr = input("enter character to be replaced")
c_repl = input("enter character to replace above character")

replace_char_by_char(source, c_tbr, c_repl)
