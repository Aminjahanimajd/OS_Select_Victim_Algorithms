from typing import List, Dict, Any
from collections import defaultdict

def mfu(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = set()
    freq = defaultdict(int)
    faults = hits = 0

    for page in reference_string:
        freq[page] += 1
        if page in frames:
            hits += 1
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.add(page)
            else:
                # Find the page with maximum frequency
                max_freq_page = max(frames, key=lambda p: freq[p])
                frames.remove(max_freq_page)
                frames.add(page)

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
