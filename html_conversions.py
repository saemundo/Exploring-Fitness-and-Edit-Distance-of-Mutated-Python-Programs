"""
This file holds a collection of different formatting replacements for 
html to latex.


simple html to latex replacements
"""
html_2_latex_simple = {'<!-- pagebreak -->':'\\newpage',
                       u'&nbsp;': u' ',
                       u'\xa0':u' ',
                       '<br>':'\n\\vspace{-0.1em}',
                       '<br/>':'\n\\vspace{-0.1em}',
                       r'%':r'\%',
                       '\r\n':'\n',
                       u'_':u'\_'
                       }
"""
html_shuffles (pattern, in_front, in_back)
"""
html_shuffles = [
   (r'\s+class\s*=\s*"wysiwyg-text-align-center"\s*',u'\\begin{center}',r'\end{center}'),
   (r'\s+class\s*=\s*"wysiwyg-text-align-right"\s*',u'\\begin{flushright}',r'\end{flushright}'),
   (r'\s+class\s*=\s*"wysiwyg-color-blue"\s*',r'\textcolor{blue}{',r'}'),
   (r'\s+class\s*=\s*v"wysiwyg-color-green"\s*',r'\textcolor{green}{',r'}'),
   (r'\s+class\s*=\s*"wysiwyg-color-red"\s*',r'\textcolor{red}{',r'}'),
   (r'<h2\s+style\s*=\s*"text-align: center;">',r'''\begin{center}
   \subsection*{''',r'}\n\end{center}'),
   (r'<h1\s+style\s*=\s*"text-align: center;">',r'\begin{center}\section*{',r'}\end{center}'),
   (r'<h3\s+style\s*=\s*"text-align: center;">',r'\begin{center}\subsubsection*{',r'}\end{center}'),
   (r'\s+style\s*=\s*"text-align: right;"\s*',u'\\begin{flushright}',r'\end{flushright}'),
   (r'\s+style\s*=\s*"text-align: left;"\s*',u'\\begin{flushleft}',r'\end{flushleft}'),
   (r'\s+style\s*=\s*"text-align: center;"\s*',u'\\begin{center}',r'\end{center}'),
   (r'\s+style\s*=\s*"text-align: justify;"\s*',r'{\justify',r'}'),
   (r'\s+style="text-decoration: underline;"\s*',r'\underline{',r'}'),
   (r'\s+style="text-decoration: line-through;"\s*',r'\st{',r'}'),
   (r'style=".*"',r'',r''),
   (r'<sub>',r'\[',r'\]'),
   (r'<sup>',r'\{',r'\}'),
   (r'<div.*>',r'',r'\n'),
   (r'<ul.*>',u'\\begin{itemize}',r'\end{itemize}'),
   (r'<ol.*>',u'\\begin{enumerate}',r'\end{enumerate}'),
   (r'<li.*>',r'\item ',r''),
   (r'<p\s*>',r'',r''),
   (r'<b\s*>',u'\\textbf{',r'}'),
   (r'<strong>',u'\\textbf{',r'}'),
   (r'<i>',r'\emph{','}'),
   (r'<em>',r'\emph{','}'),
   (r'<span>',r'',r''),
   (r'<h1.*>',r'\section*{',r'}'),
   (r'<h2.*>',r'\subsection*{',r'}'),
   (r'<h3.*>',r'\subsubsection*{',r'}'),
   (r'<h[45].*>',r'{\small ',r'}'),
   (r'<h6.*>',r'{\\tiny ',r'}'),
   (r'<.*>',r'',r'')
]
"""
colour codings
"""
html_color = [(r'<span style="color: #([0-9A-Fa-f]+);">',
               u'\\textcolor[HTML]{{{}}}{{',
               r'}'),
             (r'<span style="background-color: #([0-9A-Fa-f]+);">',
              u'\\colorbox[HTML]{{{}}}{{',
               r'}')]

"""
html_delete: remove without replacement
"""
html_delete = [r'\s*class\s*=\s*"wysiwyg-clear-(both|left|right)"\s*',   
                r'\s*class\s*=\s*"wysiwyg-color-(aqua|black|fuchsia|gray|lime|maroon|navy|olive|purple|silver|teal|white|yellow)"\s*',   
                r'\s*class\s*=\s*"wysiwyg-font-size-(large[r]{0,1}|medium|small(er){0,1}|x{1,2}-(large|small))"\s*',
                r'\s*class\s*=\s*"wysiwyg-float-(left|right)"\s*',
                r'\s*class\s*=\s*"wysiwyg-text-align-left"\s*'
               ]
"""
Special cases of manual known manual formatting attempts, like number spaces to right adjust text 
"""
html_special_cases = [(r'(&nbsp;){10,}[\s]*',r'\n\hfill ')]



