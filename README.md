# Mashup Generator Web Application

## Assignment Overview

This project is developed as part of the Mashup Assignment.

It consists of:

-  Program 1: Command Line Python Program
-  Program 2: Web Service for Mashup Generation

The application downloads YouTube videos of a singer, converts them to audio, trims them, merges them, and sends the final mashup via email.

---

#  Program 1 – Command Line Mashup Generator

### Description

This program:

1. Downloads **N YouTube videos** of a singer.
2. Converts videos to audio.
3. Trims the first **Y seconds** of each audio file.
4. Merges all trimmed audios into one final mashup file.

###  How to Run

Use Python 3.11:
py -3.11 102303601.py "Singer Name" 12 30 output.mp3

# Program 2 – Web Application
##Description

The web application allows users to:

Enter singer name

Enter number of videos

Enter duration

Enter email ID

After submission:

The mashup is generated

Output is zipped

ZIP file is sent via email
