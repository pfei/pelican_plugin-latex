# -*- coding: utf-8 -*-
"""
Latex Plugin For Pelican

https://github.com/pfei/pelican_plugin-latex/blob/master/latex.py

This plugin allows you to write mathematical equations in your articles using Latex.
It uses the MathJax Latex JavaScript library to render latex that is embedded in
between `$..$` for inline math and `$$..$$` for displayed math. It also allows for
writing equations in by using `\begin{equation}`...`\end{equation}`.

credit:
https://github.com/barrysteyn/pelican_plugin-render_math/blob/master/render_math.py
https://github.com/jakevdp/pelican_plugin-latex/blob/master/latex.py
https://github.com/wittawatj/pelican_blog/blob/master/plugins/latex.py
"""

from pelican import signals

latexScript = """
    <script async type= "text/javascript"
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
       MathJax.Hub.Config({
           config: ["MMLorHTML.js"],
           jax: ["input/TeX","input/MathML","output/HTML-CSS","output/NativeMML"],
           TeX: { extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"], equationNumbers: { autoNumber: "AMS" } },
           extensions: ["tex2jax.js","mml2jax.js","MathMenu.js","MathZoom.js"],
           tex2jax: {
               inlineMath: [ [\'$\',\'$\'] ],
               displayMath: [ [\'$$\',\'$$\'] ],
               processEscapes: true },
           "HTML-CSS": {
               styles: { ".MathJax .mo, .MathJax .mi": {color: "black ! important"}}
           }
       });
    </script>
"""

def addLatex(gen, metadata):
    """
        The registered handler for the latex plugin. It will add
        the latex script to the article metadata
    """
    if 'LATEX' in gen.settings.keys() and gen.settings['LATEX'] == 'article':
        if 'latex' in metadata.keys():
            metadata['latex'] = latexScript
    else:
        metadata['latex'] = latexScript

def register():
    """
        Plugin registration
    """
    signals.article_generator_context.connect(addLatex)
    signals.page_generator_context.connect(addLatex)
