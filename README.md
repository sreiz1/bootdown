BootDown
========

REALLY lazy static sites with Bootstrap and Markdown.

## Quickstart

Note that this project now has a dependency on the [Project ThoughtStorms](http://project.thoughtstorms.info) libraries. 

    pip install thoughtstorms markdown pyyaml
    
then :

    git clone https://github.com/interstar/bootdown.git
    cd bootdown/example/
    python ../bootdown.py example.md
    firefox example/index.html


Compare what's in the example.md file (your entire site), with the produced static site.

## Philosophy

Basically it's a Markdown to HTML processor with some extra tricks added to it

  * A header section that lets you define a menu, footer, projectname, bootswatch, head_extra (extra code to put in page headers)
  * A "page-break" option (lines beginning with ////) so that your single .md file becomes a number of HTML pages
  * A very light-weight markup for defining divs with classes and ids using &lbrack;.CLASSNAME#ID and .&rbrack;
  * A markup for including CSV files as tables, embedding YouTube videos, BandCamp albums and SoundCloud albums. This is now based on, and kept in sync with the [Project ThoughtStorms wiki-engine](https://github.com/interstar/ThoughtStorms).
  
Unlike most static site systems that are built around templating engines, with BootDown you write both your page content, and the structure in a single source file. Using &lbrack;. .&rbrack; for divs. This gives you all the flexibility you need to layout your pages any way you like, within the BootStrap grid.


## Aims and Features

  * To be the quickest, laziest way to make an "acceptable" flat site.
  * Emphasis on the "acceptable". Comes with several off-the-shelf Bootstrap / [Bootswatches](https://bootswatch.com/) to choose from.
  * But strongly discourages you trying to write your own CSS or other styling. No templates! 
    * (Well, actually you CAN put a custom template in but it's a hack.)
  * Write your entire site in a single .md file. No faffing with managing multiple source files. 
    * (Unless you really want to, in which case put further .md files in an extra_pages subdirectory.)
  * Suitable for landing pages, documentation sites, guides, handbooks, portfolios etc.
  
  

## Dependencies

Needs [ThoughtStorms](https://pypi.org/project/thoughtstorms/) and Python's Markdown, YAML and CSV libraries installed.

## Update notes after forking
* Converted the code from Python 2 to Python 3;
* Added the generated folder with static files example/example to the repo to facilitate a quick peek at the results.
* Added a Flask runner for the example/example static files, run with python app-example.py, then in your browser open http://localhost:5000/index.html
