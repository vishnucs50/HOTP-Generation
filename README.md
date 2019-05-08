# HOTP-Generation

Introduction

In this lab, we will implement HOTP, the HMAC-Based One-Time Password protocol. This will be a simple command-line tool written in the programming language of your choice.

Basic Requirements

The program should be invoked as such:
./hotpGen –c 1
The –c switch is the counter value. This allows for some repeatability in runs of the program. The key value that should always be used is 0xfebd2036b04690e307342884d14ba164. The program should print out the 6-digit code. If the –verbose switch is used, intermediate calculations should be printed to the screen. Using the example from the slides, a sample run would look like:
./hotpGen –c 1885 –verbose
HS = 0xe3d8b7d48530de110ea119c838ebf9de4761fb79
Offset = 9
Snum = 0x2119c838
HOTP = 337784

Encryption Algorithms

As in previous labs, you should not be implementing HMAC algorithms from scratch. The only algorithm you need is the SHA-1 HMAC. 
