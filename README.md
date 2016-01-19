# PASSWORD GENERATOR
Very simple python password genarators using a dictionary files to produce passhrases out of known words

### passwords.py
uses a dictionary of 240.000+ common/and uncommon Icelandic words* to generate a passphrase
```python
# Usage:
# python passwords.py n
# Where n is a number between 1 and 10
python passwords.py 4

Your password is
===========================================
biðskýlum fræðanna hófsamri sumartískunni
```

### passphrase.py
uses three dictionary files, nouns (6185 word), verbs (493 word) and adjectives (1288 words) to structure a statement like passphrase
```python
# Usage:
# python passphrase.py

Your password is
===========================================
faglegur heimskautaúlfur treysta girðing
```


*Note that the python files and the dict files have to be in the same directory, any UTC-8 dict file will do,
dict file should though be a list of words with one word in each line. Any other format will produce
an unpredictable outcome.*

*http://islenska.org/download - Íslensk Orðaskiptilýsing*