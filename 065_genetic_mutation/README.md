A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`,
`'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `start_gene` to a gene string
`end_gene` where one mutation is defined as one single character changed in the gene string.

* For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in
`bank` to make it a valid gene string.

Given the two gene strings `start_gene` and `end_gene` and the gene bank `bank`, return _the
minimum number of mutations needed to mutate from `start_gene` to `end_gene`. If there is no such a
mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.