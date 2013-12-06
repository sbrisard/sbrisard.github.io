*********************
Some gruesome details
*********************

Formulas on this website are typeset in :math:`\LaTeX` and rendered with `MathJax <http://www.mathjax.org/>`_. Activating this feature is very simple. The first thing you need to do is edit the model of your blog, and insert in the header the following lines

.. code-block:: html

  <script src='http://cdn.mathjax.org/mathjax/latest/MathJax.js'
          type='text/javascript'>
      MathJax.Hub.Config({extensions: ["tex2jax.js", "TeX/AmsMath.js", "TeX/AMSsymbols.js"],
                          jax: ["input/TeX", "output/HTML-CSS"],
                          tex2jax: {inlineMath: [['$','$']],
                                    displayMath: [['$$','$$']],
                                    processEscapes: true,},
                          "HTML-CSS": {availableFonts: ["TeX"]}});
  </script>

Et voilà! Then, typing ``$$(a+b)^2 = a^2+2ab+b^2$$`` produces the desired result

.. math:: (a+b)^2 = a^2+2ab+b^2

As for inline math ``$(a+b)^2 = a^2+2ab+b^2$`` renders to :math:`(a+b)^2 = a^2+2ab+b^2`.

NOTA: MathJax can also render MathML. You can even mix MathML and :math:`\LaTeX` in the same webpage! To render MathML as well, you just need to paste the following lines to some place in the ``<header>...</header>`` section of your webpage

.. code-block:: html

  <script src='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML' type='text/javascript'></script>

and you're done! MathML blocks must be enclosed in a script

.. code-block:: xml

  <script type='math/mml'>
      <math xmlns='http://www.w3.org/1998/Math/MathML'>
          ...
      </math>
  </script>
