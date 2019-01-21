## Purpose:
    This repo contains the files necessary to parse Python and all derivatives of C,
    and return the amount of comments and lines of code contained in a file.

## To Parse a File on your computer:
    In the python folder, run "custom_parser.py <filename>"

## To Scrape github:
    First, generate an API key for github. Instructions can be found here:
        https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

    In the python folder, create a file named private.py. In this file create the following variable:
        GITHUB_API_KEY = "<Your_API_key_here>"

    Now, run "scraper.py" to begin scrapping Github and Parsing files!
