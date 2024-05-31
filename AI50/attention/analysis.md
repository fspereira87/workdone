# Analysis

## Layer 1, Head 3

In this attention head, it appears to be focusing on the relationship between verbs and their direct objects. When analyzing the attention diagrams, it seems that this head pays attention to the token following a verb, capturing the syntactic structure of actions. For example, in the sentence "She [MASK] a delicious cake," attention is drawn to "[MASK]" and "a.", as in the sentence "The cat [MASK] a mouse." but in this case, the results where less predictable or logical. This suggests that Layer 1, Head 3 might be instrumental in capturing verb-object relationships.

Example Sentences:

The cat [MASK] a mouse.
She [MASK] a delicious cake.

Results:

The cat was a mouse.
The cat is a mouse.
The cat and a mouse.

She made a delicious cake.
She was a delicious cake.
She had a delicious cake.

## Layer 2, Head 7

Layer 2, Head 7 seems to be playing a role in recognizing and predicting the direct objects of verbs in a sentence.
The clear relationship between "love" and "[MASK]" and "flowers" and "[MASK]" in the sentence "I love the [MASK] flowers" when analyzing Layer 2, Head 7 suggests that this attention head may be specialized in capturing the association between verbs and their direct objects. The same can be said for the relation between the verb "stands" and [MASK] in the sentence The [MASK] building stands.

Example Sentences:
- The [MASK] building stands.
- I love the [MASK] flowers.


Results:

The main building stands.
The original building stands.
The current building stands.

I love the pink flowers.
I love the white flowers.
I love the beautiful flowers.
