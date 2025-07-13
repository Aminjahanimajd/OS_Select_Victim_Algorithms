from typing import List, Dict, Any

def second_chance(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = [-1] * num_frames
    ref_bits = [0] * num_frames
    pointer = 0
    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
            ref_bits[frames.index(page)] = 1
        else:
            faults += 1
            while True:
                if ref_bits[pointer] == 0:
                    frames[pointer] = page
                    ref_bits[pointer] = 0
                    pointer = (pointer + 1) % num_frames
                    break
                else:
                    ref_bits[pointer] = 0
                    pointer = (pointer + 1) % num_frames

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
