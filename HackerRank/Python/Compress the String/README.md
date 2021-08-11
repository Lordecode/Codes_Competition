In this task, we would like for you to appreciate the usefulness of the _groupby()_ function of _itertools_ . To read more about this function, [Check this out](https://docs.python.org/2/library/itertools.html#itertools.groupby) .

You are given a string <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"></span>. Suppose a character '<span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"></span>' occurs consecutively <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"></span>times in the string. Replace these consecutive occurrences of the character '<span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-4-Frame"></span>' with <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-5-Frame"></span>in the string.

For a better understanding of the problem, check the explanation.

**Input Format**

A single line of input consisting of the string <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-6-Frame"></span>.

**Output Format**

A single line of output consisting of the modified string.

**Constraints**

All the characters of <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-7-Frame"></span>denote integers between <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-8-Frame"></span>and <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-9-Frame"></span>.

<span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-10-Frame"></span>

**Sample Input**

    1222311

**Sample Output**

    (1, 1) (3, 2) (1, 3) (2, 1)

**Explanation**

First, the character <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-11-Frame"></span>occurs only once. It is replaced by <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-12-Frame"></span>. Then the character <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-13-Frame"></span>occurs three times, and it is replaced by <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-14-Frame"></span>and so on.

Also, note the single space within each compression and between the compressions.

<div class="right-pane">

<aside class="theme-m-content fullscreen-hide challenge-sidebar">

<div class="challenge-sidebar-container">

<div class="sidebar-problem-difficulty challenge-sidebar-help">

<div class="difficulty-block">

Author

<div class="ui-tooltip-wrapper">[anuj_95](/profile/anuj_95)</div>

</div>

<div class="difficulty-block">

Difficulty

Medium

</div>

<div class="difficulty-block">

Max Score

20

</div>

<div class="difficulty-block">
