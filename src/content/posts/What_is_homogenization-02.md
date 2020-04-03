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

Now, let us imagine that the printer is handed out the original
photograph (which is indeed made of shades of grays, *not black dots*)
alongside the article about the launch of the ocean liner
*Normandie*. He needs to decide on the pattern(s) that will result in
the best reproduction of the photograph as a distribution of dots. To
do so, he needs a rule that relates the size and spacing of dots to
the resulting shade of gray. This is what homogenization is really
about.

More generally, homogenization provides a mapping from the
*microstructure* to the *effective properties*.

Two strategies can be adopted to carry out homogenization. In the
so-called *top-down* approach, the effective properties are *measured*
(in a broad sense). In the example above, we could provide the
observer with a set of cards uniformly coloured with various shades of
blue, and ask him to pick the card which is closest to how the blue
sky looks from far off. The alternate, *bottom-up* approach is often
referred to as *upscaling*. In this approach, the effective properties
are *inferred* (through a mathematical model) from the
microstructure. In the example above, we could *predict* the effective
blue shade of the lithograph\'s sky by some kind of weighted average
of the blue shade of the dots, and the white background.

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
