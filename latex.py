#!/usr/bin/python
# coding: utf-8
"""
A simple conversion script for html -> latex
The conversions are specifically made to adjust to 
Janus Rehabilitation formatting of reports.
It is used in Janus Manager to convert text typed into
html textfields to latex for pdf reports.
"""
from bs4 import BeautifulSoup
from html_conversions import html_delete,html_2_latex_simple
from html_conversions import html_special_cases,html_color,html_shuffles
import re

def html_2_latex(html_text):
    latex = html_text
    for i in html_delete:
        latex = re.sub(i,'',latex,re.UNICODE)
    for i in html_special_cases:
        latex = re.sub(i[0],i[1],latex,re.UNICODE)
    html = BeautifulSoup(latex,'html.parser')
    latex_out = html.prettify()
    for key,val in html_2_latex_simple.items():
        latex_out = latex_out.replace(key,val)
    back_of_the_class=[]
    re_struct = []
    reading_table = False
    for line in re.split(r'(\n)',latex_out):
        if '<' in line:
            if re.search(r'</',line):
                try:
                    in_again = re.sub(r'</[a-zA-Z]+.*>',back_of_the_class.pop(),line,re.UNICODE)
                except IndexError as e:
                    print line
                    print e
                    raise
                re_struct.append(in_again)
            else:
                into_the_front = []
                to_the_back = []
                the_color = re.search(html_color[0][0],line)
                the_back_color = re.search(html_color[1][0],line)
                if the_color:
                    the_color = the_color.group(1).upper()
                    st_color = html_color[0][1].format(the_color)
                    into_the_front.insert(0,st_color)
                    line = re.sub(html_color[0][0],r'',line,re.UNICODE)
                    to_the_back.insert(0,html_color[0][-1])
                if the_back_color:
                    the_back_color = the_back_color.group(1).upper()
                    st_color = html_color[1][1].format(the_back_color)
                    into_the_front.insert(0,st_color)
                    line = re.sub(html_color[1][0],r'',line,re.UNICODE)
                    to_the_back.append(html_color[1][-1])
                for out,in_front,in_back in html_shuffles:
                    if re.search(out,line):
                        to_the_back.insert(0,in_back)
                        into_the_front.insert(0,in_front)
                        line = re.sub(out,r'',line,re.UNICODE)
                into_the_front.append(line)
                re_struct.append(r' '.join(into_the_front))
                back_of_the_class.append(r''.join(to_the_back))
        else:
            re_struct.append(line)
    latex_print = u''.join(re_struct).replace(u'\xa0',u'')
    for i in re.finditer(r'\n\s*\\end{center}\s*\n\s*\\begin{center}\s*\n',latex_print):
        latex_print = latex_print.replace(i.group(),u'')
    r = r'(\n(?=\s*\n)(?:\s*\n)+)'
    for i in re.finditer(r,latex_print):
        try:
            n = round(float(len(i.group()))/10,2)
        except ZeroDivisionError:
            continue
        t = u'\n\n\\vspace{{{}em}}\n'.format(n)
        latex_print = re.sub(i.group(),t,latex_print,re.UNICODE)
    latex_print = latex_print.replace(u'\x0b',u'\\v').replace(u'\x08',u'\\b')
    latex_print = re.sub(r'<p><!-- pagebreak --></p>',r'\\newpage ',latex_print)
    return latex_print
