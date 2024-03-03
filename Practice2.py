# Regex training with Corey Schafer
import re

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ()

coreyms.com

__

321-555-4321
123.555.1234
321*555*4321
800.555.1234
900.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat 
bat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
mohamedyoyo55@gmail.com
kishouagg@outlook.com
electrocrab14@gmail.com

4
4.0O0
-1.00
+4.54

'''
sentence = 'Start a sentence and thrn bring it to an end'

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

"""
test_text="""
5
1.414
+.5486468
0.5.0
1+1.0
0
"""
pattern = re.compile(r'.+@.+\.(\w+)')
trial= re.compile(r'^[-+]?\d*\.{1}\d+',re.MULTILINE)



x=trial.findall(test_text)
print(x)


