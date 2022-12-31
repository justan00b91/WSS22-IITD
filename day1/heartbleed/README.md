## Hints Given:

1. We print the text only if (text.size() - length) is greater than or equal to zero. Then, why are we able to print the secret?

# Solution:

HeartBleed is a memory leak vulnerability, which can be used to dump the contents of the memory.
In the given question, we exploit the `memcpy` function inside the cpp file.

### Program Flow:
The program has a global array declared which contains the strings we need to capture. Once the execution starts, we are asked to provide 2 parameters,
1st is for choosing which word to pick from the array, and 2nd is the length of characters we want to be returned. Leaving the parameters to default chooses the first word from the list, and the length is taken according to that alone.

This is where the leak happens, when we ask the the `memcpy` function to return more characters from the memory rather than the length of the asked string.

![Code_SS](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/heartbleed/screenshots/Heartbleed.jpg)

### Output:
Overflowing the charaters leads to leak in the memory.

#### Using 1st string:

![Output_SS](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/heartbleed/screenshots/output.jpg)
