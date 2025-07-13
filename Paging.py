from typing import List, Dict, Any
from collections import deque

def page_buffering(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = deque(maxlen=num_frames)
    buffer_size = num_frames  # or set to another appropriate value
    free_pool = deque(maxlen=buffer_size)
    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
        elif page in free_pool:
            hits += 1
            free_pool.remove(page)
            frames.append(page)
        else:
            faults += 1
            if len(frames) == num_frames:
                victim = frames.popleft()
                free_pool.append(victim)
            frames.append(page)

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
