## Instructions:

Attempt the problems in the following order:
1. fuzzing
2. memrchr

## Solution:

### Fuzzing:

The code is given of the American Fuzzy Lop, aka, AFL fuzzer, to find bugs in the program `fuzzgoat`, which is also given in the lab exercise.
Due to github issues, I was unable to upload the Fuzzing directory in the github repo, but will upload as soon as git LFS starts working on my system.

![Sample_screenshot](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/Fuzzing-sample.png)

Here is a screenshot of the afl-fuzzer running on the code. It finds on which inputs the program crashes and identifies the unique inputs from them for us to analyse further.

Expected input of fuzzgoat is JSON FILE, so we will mention the contents of the JSON files which crashes the code.

Here are some cases, where the fuzzer was able to crash the fuzzgoat.

- **{"":""}**
This error occurs because the object name and string provided is null, thereby causing a segmentation fault in the code.

![Output_1](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_1.png)

- **"{"**
This error occurs because of incorrect structure of the JSON file, when it as expecting an object, a single string was provided causing the program to crash.

![Output_2](ttps://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_2.png)

- **{"":5}**
This error occurs because the input JSON had an empty string and an int object, causing segmentation fault.

![Output_3](ttps://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_3.png)

- **[]>**
This is not a valid JSON data, thereby unable to parse the data. The program ended successfully, but since the execution was abruptly stopped, fuzzer recored it as a crash.

![Output_4](ttps://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_4.png)

- **["",",^"]**
This causes an error as the name of the string is valid, and techically the second part is also correct, but it was unable to free the pointer of that node, thereby aborting the program.

![Output_5](ttps://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_5.png)

- **"\f"**
The string entered was an escape sequence, thereby causing program crash.

![Output_6](ttps://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day2/Screenshots/input_6.png)

The fuzzer was able to identify more than 30 unique crashes, there are only a few of those.
