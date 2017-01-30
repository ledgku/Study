# -*- coding: utf-8 -*-
def simple_html_tag(tag, msg):
    print('<{0}>{1}<{0}>'.format(tag, msg))

simple_html_tag('h1', 'simple heading title')

print('-' * 30)

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)
print_h1('first heading title')
print_h1('second heading title')

print_p = html_tag('p')
print_p('first paragraph')
