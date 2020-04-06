Title: What is homogenization? Part 2: top-down and bottom-up strategies
Date: 2020-04-03
Category: Homogenization
UseKaTeX: True

In the [previous
instalment]({filename}20200402-What_is_homogenization-01.md) of this
series, we introduced homogenization and the separation of scales. In
the present post, we will discuss two possible strategies that can be
adopted to carry out homogenization: the *top-down* and the
*bottom-up* approaches. To do so, we will again use the analogy with
the halftoning technique.

Remember that we considered the following picture, reproduced from *Le
Journal* (thursday, may 30<sup>th</sup>, 1935).

![The first cruise of the ocean liner Normandie.]({static}What_is_homogenization-01/Normandie.jpg){.figure}

Taking a closer look at the prow:

![Close-up of the prow]({static}What_is_homogenization-01/Normandie-400x300.png){.figure}

we realized that what *looked like* shades of gray in the photograph
was actually a *dotted* structure. This dotted structure will be
called the *microstructure*; its typical length-scale is the
*microscopic* length-scale $L\_\mu$ that was introduced before.

Now, let us imagine what happened when this photograph was actually
printed alongside the article about the launch of the ocean liner
*Normandie*. The printer was handed out the original photograph (which
is indeed made of shades of grays, *not black dots*) and had to pick
the dot pattern(s) that would result in the best halftone reproduction
of the photograph. To do so, he needed a rule that relates the dot
pattern to the resulting shade of gray.

This is what homogenization is really about: homogenization provides a
mapping from the *microstructure* to the *effective properties*.

Our friend the printer first performed the required homogenization
step experimentally. As the problem at hand is about human perception,
he asked the apprentice to be the subject of his experiment. He gave
the apprentice a set of cards, uniformly coloured with various shades
of gray. Then, he showed him various dot patterns. Foor each of these
patterns, the printer asked the apprentice to pick the card that was
closest to how he percieved the pattern. The printer was then able to
build a chart that related the pattern to the shade of gray (and
vice-versa). But then, the printer realized that this experiment is
fundamentally subjective. In order to be *statistically
representative*, he needed to repeat this experiment with many
subjects, and compute some kind of average. He thought that this was
quite tedious, and maybe there was another strategy.

In fact, there *is* another strategy, which is called *up-scaling* (or
*bottom-up approach*). In this approach, the effective properties are
*inferred* (through a mathematical model) from the microstructure. In
the case of halftoning, the mathematical model is rather simple, as it
boils down to a simple average.

These two strategies should not be seen as competing, but rather as
complementary approaches to the same problem. While the top-down
approach always delivers the “correct” answer (provided that the
experiments are performed correctly), efficient bottom-up approaches
have the ability to be *predictive*: given the microstructure, the
effective properties can be computed with no need to actually *build*
the microstructure. This is particularly desirable in an industrial
context, where numerical modelling is gradually supplanting physical
testing.

In my research, I preferably resort to bottom-up approaches. The
remainder of this series will therefore be devoted to homogenization
through upscaling.

<!-- -*- coding: utf-8; fill-column: 80 -*- -->
