# Buffer Overflow Attacks

## Instructions:

### Build and install the vulnerable targets
```
$ cd /home/userx/day1/targets
$ make
$ sudo make install
```
This creates executables `/tmp/target{1,2}` with the `setuid` bit set.

### Build the exploit code
```
$ cd /home/userx/day1/xploits
$ make
```

### Run the exploit code
```
$ cd /home/userx/day1/xploits
$ ./xploit1
$ ./xploit2
```

### Change the exploit code
Edit the xploit{1,2}.c files so that, when run again, they
a. first cause the target executable to crash, e.g., due to a segmentation fault
b. then cause the target executable to yield a root shell.
The "shellcode.h" file available in the `xploits/` directory contains the binary code that, when executed, executes the shell command.  You may want to use the contents of this code in the command-line arguments used while invoking the target executables.


## Solution:

Buffer Overflow attacks are possible when the Stack is set to executable. In this attack, we override the return address of a function to an arbitary position in the stack, which has the shellcode to be executed. This leads to code execution from the program.

To start with the attack, we disable the `randomize_va_space` to make our lives easier and stop the randomization of the stack each time the program is executed. This gives us the opportunity to work with the same address layout while executing the program multiple time.

```bash
# To disable aslr
$> echo 0 > /proc/sys/kernel/randomize_va_space

# To enable aslr
$> echo 2 > /proc/sys/kernel/randomize_va_space

# To verify aslr
$> cat /proc/sys/kernel/randomize_va_space
```

Once our binaries are compiled, we can start working with `gdb`.

#### Target1:
This is the easier of the two binaries provided in the exercise. To get a basic understanding of buffer overflow, we need to have some idea of how the memory is layed out.

<img src="https://gabrieletolomei.files.wordpress.com/2013/10/program_in_memory2.png" align="center" alt="https://gabrieletolomei.files.wordpress.com/2013/10/program_in_memory2.png">

As seen from the above diagram, the stack grows downwards. Inside the stack, the structure is as follows:
<img src="https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/buffer-overflow/Screenshots/Stack_Structure.jpg">

The idea is simple, to overflow the buffer(Argument n in the image) so that it reaches the return address of the function. Then we can return to any point in the stack, which would be inside the buffer which contains the shellcode given in the lab manuals.

To do this we will need three things:

- Size of buffer in the stack
- Size of shellCode
- Memory address of the start of the buffer.


We start by finding the size of the buffer inside the stack, which in our case is `260`. Anymore then these many bytes and the return address is overwritten with the overflow bytes. We can find this by testing the size of the buffer in gdb and checking when exactly the system crashes.

The size of the shell code provided is `45 bytes`, although this changes from shellcode to shellcode.

Last, we need a memory address for the start of the buffer in the memory. This should not be the start of the buffer, but near the start of the buffer.

**Structure of the Exploit:**
```
"\x90"*215 + "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh" + "\xb4\xcf\xff\xff"
```

`\x90` is the hex equivalent of the instruction `NOP` instruction, guiding the program control (instruction counter) to simply jump to the next instruction without any execution.

The second part of the exploit is the shell code, which launches the `/bin/dash`, a shell present in almost every linux architecture.

Last part of the exploit is the address near the start of the buffer, written in little-endian style, as that is what the cpu understands.

##### Output:

Running the exploit successfully gave us the shell access.

![Shell-accessed](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/buffer-overflow/Screenshots/overflow1-1.png)

#### Target2:
This one was a bit trickier than the previous one. Instead of the vulnerable `strcpy` function, we have the `nstrcpy`, a custom implementation of the strcpy command, but insecure nonetheless.

![Code_snippet](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/buffer-overflow/Screenshots/Code_snippet.png)

The buffer size in this case is strictly 200, although for out case, we have taken 201 as the buffer size to cause segmentation fault.

**Structure of Exploit:**
```
'\x90'*147 + '\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh' + '\x74\xcf\xff\xffBBBB'
```

The first part is the NOP slide in the buffer, to route the EIP towards the shellcode. The second part is the shellcode, which opens the `/bin/dash`, same as the first one. This third part is interesting, since the overflow happens of 8 bytes from the last of the buffer, so we need to add the return address then random data. The address is as usual written in little-endian format.

##### Output:

Shell is accessed in through the exploited vulnerability.

![Buffer Overflow](https://raw.githubusercontent.com/justan00b91/WSS22-IITD/main/day1/buffer-overflow/Screenshots/overflow2-2.png)
