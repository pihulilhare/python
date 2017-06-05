#14. Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

import unicodedata    
raw_text = u"here $%6757 dfgdfg"
convert_text = unicodedata.normalize('NFKD', raw_text).encode('ascii','ignore')

