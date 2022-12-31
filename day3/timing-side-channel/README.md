## Instructions

1. Build using `make`
2. Run "time ./login candidatePassword" multiple times. Record the times taken to try and identify the correct password.

## Solution

This exercise is based on timing attacks, i.e., guessing the password by determining the amount of time taken by the program to respond. In our case, the structure of the code makes it very easy to get the password for the login function.

![Explanation](https://raw.githubusercontent.com/samsepi0x0/IITD-WSS/main/day3/timing-side-channel/Screenshots/timing-explanation.jpg?token=GHSAT0AAAAAAB27OOBVB2YFH3M5MOVWKAJMY5PIRMA)

The first delay is executed if the length of the entered text is same as the length of the password. This gives us enough details to get the exact length of the password. After a few tries, I was able to determine the length of the password by adding in an absurd amount of delay in the code. 

![password-length](https://raw.githubusercontent.com/samsepi0x0/IITD-WSS/main/day3/timing-side-channel/Screenshots/timing-length.png?token=GHSAT0AAAAAAB27OOBV5CJFMKVVKDN2KIXKY5PITJQ)

I checked it quite a few times to ensure that the length is accurate.

Once we get the length, we can then try to bruteforce each character in the password by checking if the delay increases or not. If the delay increases, we can confirm that the letter is in right place, else we can continue to try again and again.
The list of characters I used is: 

```python
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,./<>?;\':\"[]\\{}|`~!@#$%^&*()_+-="
```

Based on this procedure, we got the first letter of the password as scene below:

![output-1](https://raw.githubusercontent.com/samsepi0x0/IITD-WSS/main/day3/timing-side-channel/Screenshots/output-1.png?token=GHSAT0AAAAAAB27OOBUYAIJOG2TTFFC4L3MY5PI7AA)

#### Output:

Running the script takes too much time (an issue yet to be resolved). At the time of writing this README, the output was:

![output-2](https://raw.githubusercontent.com/samsepi0x0/IITD-WSS/main/day3/timing-side-channel/Screenshots/output-2.png?token=GHSAT0AAAAAAB27OOBVXZBEPPBOIXEPJ4WIY5PJBCQ)

Will update accordingly.

