from typing import List, Dict, Any
from collections import deque

def fifo(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = set()
    queue = deque()
    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.add(page)
                queue.append(page)
            else:
                victim = queue.popleft()
                frames.remove(victim)
                frames.add(page)
                queue.append(page)

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
