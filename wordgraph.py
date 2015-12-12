import json


class WordDictionary:
  def __init__(self):
    pass

  def getDefinitionWords(self, word):
    return []


class JsonWordGraphDictionary(WordDictionary):
  def __init__(self, graphFile):
    WordDictionary.__init__(self)
    self._graph = json.load(graphFile)

  def getDefinitionWords(self, word):
    return self._graph.get(word, [])


class WordNode:
  def __init__(self, word, dist):
    self.word = word
    self.defNodes = dict()
    self.dist = dist

  def updateDist(self, dist):
    if dist < self.dist:
      self.dist = dist

  def addDefNode(self, node):
    self.defNodes[node.word] = node


class WordGraph:
  def __init__(self, wordDict, maxDist):
    self._wordDict = wordDict
    self._maxDist = maxDist
    self._wordNodes = dict()

  def loadWord(self, startWord):
    self._loadWord(startWord, 0)

  def _loadWord(self, word, dist):
    if dist > self._maxDist:
      return
    node = self._getOrAddWord(word, dist)
    defWords = self._wordDict.getDefinitionWords(word)
    pass

  def _getOrAddWord(self, word, dist):
    node = self._wordNodes.get(word)
    if node is not None:
      node.updateDist(dist)
    else:
      node = self._wordNodes[word] = WordNode(word, dist)
    return node
