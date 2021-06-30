# COMP20008 2021 Semester 1 Assignment 1
Readme file

Name: Elizabeth Wong
Student ID: 1082634

ABOUT THIS PROJECT:

A datascience project for COMP20008 concerning where PART A involves preproccessing data from 
"https://covid.ourworldindata.org/data/owid-covid-data.csv", "Our World in Data COVID-19 dataset", ultimately 
creating two figures: scatter-a.png and scatter-b.png.

PART B consists of performing searches for document ID within a series of text files in the 
'crickets' folder within this repo as well as data preprocessing to format the data.


List of dependencies:

import sys
import os
import csv
import re
from nltk.stem import PorterStemmer
import pandas as pd
import argparse


from partb2 import do_preprocessing
from partb2 import do_preprocessing
from partb3 import csv_to_dict, is_keyword_present
