import random
from typing import List, Dict, Any

def enhanced_second_chance_optimized(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    frames = [-1] * num_frames
    reference_bits = [0] * num_frames
    modify_bits = [0] * num_frames  # simulate write access
    pointer = 0
    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
            idx = frames.index(page)
            reference_bits[idx] = 1
            modify_bits[idx] = random.randint(0, 1)
        else:
            candidate = None
            iterations = 0
            max_iterations = num_frames * 2  # safety limit to avoid infinite loop

            while True:
                r = reference_bits[pointer]
                m = modify_bits[pointer]

                if r == 0 and m == 0:
                    # Ideal victim found
                    break
                elif r == 0 and m == 1:
                    # Candidate victim if no ideal found
                    if candidate is None:
                        candidate = pointer
                else:
                    # Clear reference bit
                    reference_bits[pointer] = 0

                pointer = (pointer + 1) % num_frames
                iterations += 1

                if iterations >= max_iterations:
                    # If no perfect victim found, use candidate or current pointer
                    if candidate is not None:
                        pointer = candidate
                    break

            # Evict page at pointer
            frames[pointer] = page
            reference_bits[pointer] = 1
            modify_bits[pointer] = random.randint(0, 1)
            faults += 1
            pointer = (pointer + 1) % num_frames

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
