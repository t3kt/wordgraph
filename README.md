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

### process for each word, with currentDist=distance from startWord
* look up currentNode for word in wordTable
* if currentNode already exists, skip
* get definition of word
* split and normalize the definition into defWords
* for each defWord:
  * look up defNode for defWord
  * if defNode is not found:
    * if currentDist >= maxDistance:
      * insert a placeholder node into the table, including currentDist
      * set defNode = the placeholder
    * else (dist < maxDistance):
      * look up and process the defWord, with dist = currentDist - 1
      * set defNode = the resulting node
  * else if defNode is found:
    * if defNode is a real node:
      * add a link in currentNode pointing to defNode
      * set defNode.dist = min(defNode.dist, currentDist)
    * else (defNode is a placeholder):
      * if currentDist < maxDistance:
        * look up defWord and replace the placeholder with the resulting node
        * add a link in currentNode pointing to defNode
    
