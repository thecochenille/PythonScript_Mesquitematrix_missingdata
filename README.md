
Calculate percentage of missing data and unapplicable characters in morphological matrices in Nexus format for phylogenetic analyses
======================

##Summary
This script is a "dirty" rapid way to assess the percentage of missing data and non-application characters in your morphological matrix. It also provides the percentage of taxa that was not scored for a given character.


###Program

This script was written in Python so it can be run with your Terminal but make sure that Python is installed.


###Files

This repository includes the script: `missing.py` and an example of nexus file: `example.nex`. The example file is a random matrix created with Mesquite.

###Input file

You will need your morphological matrix to be in Nexus format. Also, there shouldn't be any molecular data. If not in Nexus or if there is molecular data, there will be an error message.

_Attention_: This script identifies the nexus format by looking for `#NEXUS` in the file. For identifying morphological matrices, the script looks for `datatype=STANDARD` which is in `begin data;` section. Finally, all information in `begin data;` have to be in capital letters. 
The easiest way to have those conditions met is to have your matrix created or imported in [Mesquite](http://mesquiteproject.org/mesquite/download/download.html) and export the file as nexus.

If you do not have datatype, you can add it in your matrix before running the script.


###How to use

Put `missing.py` and you nexus file in the same directory then type:

`python missing.py <filename.nex>`

##Output

There is no output file in this version of the script but print in the Terminal will first list the name of your taxon as well as percentage of missing data and non-applicable characters.
The second list will be the character number with the percentage of taxa for which it has been scored. Finally, for each list, the taxa or characters are ordered by increasing number of missing data.See Example section for a look at the output.


##Example
Command line in Terminal:

`python missing.py example.nex`

##Disclosure
This script was written for a morphological matrix that I built and specifically for morphological characters and not flexible at identifying if your matrix is in the correct format (See Input file section for details). 
Therefore, feel free to modify this script to your liking or to make it more generic (for other formats etc...)



