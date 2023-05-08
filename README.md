# README

Paper link:
*https://scholar.google.com/citations?view_op=view_citation&hl=en&user=bToAUHMAAAAJ&sortby=pubdate&citation_for_view=bToAUHMAAAAJ:9LpHyFPp1DQC*

## An Efficient and Secure Post-Quantum Multi-Authority Ciphertext-Policy Attribute-Based Encryption Method Using Lattice

This project contains the implemented codebase for the methods and procedures described in above paper.

**How to Run:**  
`python main.py`

**Set parameters in config.py:**
* (N) number of authorities
* (f) degree of polynomial - power of 2
* (q) large prime number
* (m) positive integer of form $\lfloor(\log_b(q) + 1)\rfloor + 2$
* (attr) number of attributes
* (V) parameter for linear combination of z

## Algorithms

1. AA.py - Authoriy
    * AASetup
    * SecretKey
    * Decryption

2. KGC.py - Key Generation Center
    * Setup

3. User.py
    * Access Control
    * Encryption

4. algo
    * TrapGen (proxy to be replaced)


