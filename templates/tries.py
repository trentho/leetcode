from __future__ import annotations

from leetcode_classes.trie import Trie


def build_trie(words: list[str]) -> Trie:
    trie = Trie()
    for w in words:
        trie.insert(w)
    return trie


def word_exists(words: list[str], query: str) -> bool:
    trie = build_trie(words)
    return trie.search(query)
