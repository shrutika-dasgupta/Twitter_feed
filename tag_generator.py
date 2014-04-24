from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import string

print "Enter file name"
name=raw_input()
f=open(name,'rb')
final = []
word_list=[]
count_list=[]

for line in f:
    word,count = line.split(',')
    word = word.translate(None,string.punctuation)
    count = int(count.translate(None,string.punctuation))

    word_list.append(word)
    count_list.append(count)


final = zip(word_list,count_list)
tags = make_tags(final, maxsize=80, minsize = 10)

create_tag_image(tags, 'cloud_large.png', size=(1500, 500), fontname='Lobster',background=(255,255,255))
