from random import sample

text = 'abv'
size = int(input('Какой размер ->'))
new_list =[]
for i in range(size):
    change_text = sample(text, 3)
    new_list.append(''.join(change_text))
print(' '.join(new_list))

sec_list = list(filter(lambda x: text not in x, new_list))
print(' '.join(sec_list))
