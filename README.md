# wordgraph
starting with a word, look at the words used in its definition recursively to create a directed graph and find cycles.

## terminology
* word: a word in english (or whatever other language might be supported at some point later)
* node: a node in the constructed graph, identified by a word (abstract interface)
  * ...
  * including fields for the links from that word to the words used in its definition

## process
* define empty wordTable (key: word, value: node for that word, or placeholder node)
* given a startWord and maxDistance
* process startWord (see below), with dist=0

### process for each word, with dist=distance from startWord
* look up node for word in wordTable
* if node already exists, skip
* get definition of word
* split and normalize the definition into defWords
* for each defWord:
  * look up defNode for defWord
  * if defNode is not found:
    * if dist >= maxDistance:
      * insert a placeholder node into the table
  * if defNode is found and is a real node:
    * ...
