from typing import List, Dict, Any
from collections import deque

def aging_algorithm(reference_string: List[int], num_frames: int, counter_bits: int = 8, refresh_interval: int = 1) -> Dict[str, Any]:
    """
    Implements Aging algorithm (an enhanced NFU).
    - counter_bits: width of the aging counter in bits (default 8)
    - refresh_interval: how often (in accesses) we perform aging
    """
    frames = [-1] * num_frames
    counters = [0] * num_frames
    ref_bits = [0] * num_frames
    faults = hits = 0

    for t, page in enumerate(reference_string, start=1):
        if page in frames:
            hits += 1
            idx = frames.index(page)
            ref_bits[idx] = 1
        else:
            faults += 1
            # find victim: lowest counter
            if -1 in frames:
                idx = frames.index(-1)
            else:
                idx = min(range(num_frames), key=lambda i: counters[i])
            frames[idx] = page
            counters[idx] = 0
            ref_bits[idx] = 1

        # aging step
        if t % refresh_interval == 0:
            for i in range(num_frames):
                counters[i] = (counters[i] >> 1) | (ref_bits[i] << (counter_bits - 1))
                ref_bits[i] = 0

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }

