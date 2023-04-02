from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1