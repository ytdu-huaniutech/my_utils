# pip install pyahocorasick

import ahocorasick
A = ahocorasick.Automaton()
for idx, key in enumerate('he her hers she'.split()):
    A.add_word(key, (idx, key))

print('he' in A)  # True

print(A.get('he'))  # (0, 'he')
print(A.get('she')) . # (3, 'she')
print(A.get('cat', 'not exists')  # 'not exists'
print(A.get('cat')) . # Exception

A.make_automaton()
haystack = 'somestring like sher'
for end_index, (insert_order, original_value) in A.iter(haystack):
    start_index = end_index - len(original_value) + 1
    print((start_index, end_index, (insert_order, original_value)))
    assert haystack[start_index:start_index + len(original_value)] == original_value
