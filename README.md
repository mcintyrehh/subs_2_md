# subs-2-md

This is a small script that takes a file structure containing subtitles and outputs a markdown file for ease of reading/dumping into an LLM.
Currently it only supports `.srt` files matching a specific directory structure.

The script expects a file structure that matches the following pattern:
```
/Test_1
    /Lesson_1_subtitles
        /Introduction.srt
        /Background.srt
    /Lesson_2_subtitles
        /Parsing_Subtitles_4_Dummies.srt
```
The script will set the root directory name as the H1, create H2s for child directories matching `_subtitles` and H3s for the individual `srt` files within.

The output would look like this:

# Test 1

## Lesson 1

### Introduction
`...`

### Background
`...`

## Lesson 2

### Parsing Subtitles 4 Dummies
`...`

