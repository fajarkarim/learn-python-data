Write a function called find_bigrams that takes a sentence or paragraph of strings and returns a list of all bigrams.

Example:

**Input :**

```python
sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""
```

**Output :**
```python
def find_bigrams(sentence) ->

 [('have', 'free'),
 ('free', 'hours'),
 ('hours', 'and'),
 ('and', 'love'),
 ('love', 'children?'),
 ('children?', 'drive'),
 ('drive', 'kids'),
 ('kids', 'to'),
 ('to', 'school,'),
 ('school,', 'soccer'),
 ('soccer', 'practice'),
 ('practice', 'and'),
 ('and', 'other'),
 ('other', 'activities.')]
```