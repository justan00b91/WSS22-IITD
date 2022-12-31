## Instructions:

1. Run 'make' to build and run. The last output line indicates whether the output of the quine program matches quine.c or not.
2. Inside quine.c, add a function definition "void payload(void) { }" and a call to "payload()" from within main(), and potentially modify the string such that it still remains a quine.

## Solution:

A quine is a program that produces a copy of its source code in the output. Given the C program, we need to add a function such that it still remains quine.

```C
#include <stdio.h>
char*s="#include <stdio.h>%cchar*s=%c%s%c;%cvoid payload(void){}int main(void){printf(s,10,34,s,34,10,10);payload();}%c";
void payload(void){}int main(void){printf(s,10,34,s,34,10,10);payload();}
```

In the above program, I have added a function called `payload`, with return type `void`, and takes no parameters. This is an empty function which is called at last in the `main` function.

Inside the char string, the structure of the function is modified and the string is formatted so that it matches the source code.

#### Output:

Here is the output of code passing the `check-quine.sh` script.

![Check-quine](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day4/quine/Screenshots/Quine-check.png)
