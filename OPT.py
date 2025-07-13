from typing import List, Dict, Any
from collections import deque

def optimal(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = set()
    faults = hits = 0

    for i, page in enumerate(reference_string):
        if page in frames:
            hits += 1
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.add(page)
            else:
                next_use = {}
                for f in frames:
                    try:
                        next_use[f] = reference_string[i+1:].index(f)
                    except ValueError:
                        next_use[f] = float('inf')
                victim = max(next_use, key=next_use.get)
                frames.remove(victim)
                frames.add(page)

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
