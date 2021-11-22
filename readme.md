# Manchester Bioinformatics Course 
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rrr-uom-projects/ManchesterBioinformaticsCourse_Student/blob/master/notebooks/Index.ipynb)

The materials in this repository are what you will need to complete the python lectures and assessments. 

## Installation
We suggest you clone this repository to your machine, and create a branch with yours and your partner's names as the branch name. Commit your code there as you work through the course, and make sure to sync with the main repo fairly often (git push).

I made a short video to show how to create the branch if you're not familiar, you can watch it [here](https://youtu.be/72Sf03n5KZY)


I recommend you set up a virtual environment for this course, so that it doesn't mess up any other python installation you've got. This is very simple to do by following the instructions [here](https://docs.python.org/3/tutorial/venv.html). a very condensed version:

0. In a folder, e.g. `C:\Users\Andrew\code` on Windows or `/home/andrew/code` on linux
1. Create the environment with a command like this:  
    `python3 -m venv bioinformatics-course`
2. Activate the environment. On windows, open a command prompt and run:

    `cd C:\Users\Andrew\code & bioinformatics-course\Scripts\activate.bat`

    On linux, something like:

    `cd /home/andrew/code && source bioinformatics-course/bin/activate`

    This activates the virtual environment. You will need to do it every time you want to work on your code.

3. Install the required python modules. To do this, you can use the requirements.txt file from the repository. Something like:

    `cd C:\Users\Andrew\code\ManchesterBioinformaticsCourse_Student && python3 -m pip install -r requirements.txt`

    __IMPORTANT__ PyAudio will hopefully be installed automatically, but on windows it may fail. If this is the case, open requirements.txt and delete the line where PyAudio is mentioned, then re-run this step. If you plan to work on the extensions (in this case the one turining breathing traces into horrible sounds), fololow the instructions [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14) to install PyAudio separately.

4. Run the test script to verify that everything is installed and ready to go:
    
    `python3 test_installation.py`

    (Assuming you're still in the BioinformaticsCourse_Student directory)

We will also go through this at the start of the monday practical, so don't worry!


## How the course will work

__Note: things are weird because of Covid. This is the first time I've done a completely online course so some things may be a little bit interesting for the wrong reasons!__

We will have a series of pre-recorded and live lectures on python, accompanied by four afternoon practicals in which you will be asked to complete a series of assignments. There are two key parts of the assignments, which you must complete top get your marks. The first comes on the Tuesday afternoon where you will be given a set of breathing traces and sked to process them - processing and visualising a physiological signal is a key outcome of the curse, so don't miss this one! This task isn't formally assessed, but does need to be done to a good standard to hit your key outcome.

The second part of the assessment comes from the final two afternoons, in which you will be developing an image registration tool to align a pair of coronal images of the lungs, and then extracting a tumour regression curve from them. We have provided a step-by step guide for you to follow, but the code must come from you! While there is a component of the mark that will come from you having completed all of the assignments, we are more concerned with the quality of the code you write along the way. This will be covered in more depth in the lectures, but includes writing and using your own functions, quality and quantity of comments, variable names, clarity of code structure etc. We will have a short interview where you will be asked to go through and explain/describe your code and what it is doing. We may also ask some difficult questions to see how well you know your stuff!

You should have been asked to complete the University's introduction to python course before you started this one. That course covers pretty much everything you need to know about python, which we will test in the first assignment - a very simple series of tasks in a jupyter notebook. This is not assessed, but should give you a chance to practise your python skills on an unseen task that is sort-of related to what we'll be doing in other parts of the course

Some of the lectures are pre-recorded, and you can work on them at your own pace. All the lectures have accompanying notebooks which you will work through as the lecture progresses. Since the pre-course work is focused on basic python, we spend more time on image processing specifics and debugging, which form the majority of the course. For live lectures, we will be on Zoom, and I will take questions as we go (please use the raise hand thing so it doesn't degenerate into chaos). For pre-recorded lecutres, I will be on the course slack to take questions, if something is complicated, we can hop on zoom to discuss it.

Throughout the course you will work in pairs on your python assignments. To facilitate this, we will be sending zoom links to all of you (TBC: we're still figuring this bit out). There will be a slack channel for you to ask questions and we hope that to a large extend your peers will be able to answer most questions, however, we will have a team of demonstrators on hand to answer any questions that everyone is struggling with. Demonstrators will also be able to join your zoom sessions if needed to talk through any problems.

At the end of the course, you will be asked to link your github repo to me so I can look at your code while doing your assessment. Sneaky commits after the end of the course will not be counted!
