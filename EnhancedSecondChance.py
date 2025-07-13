from typing import List, Dict, Any
import random

def enhanced_second_chance(reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    """
    Enhanced Second Chance Algorithm with simulated modify bits.
    modify_bits: not passed explicitly, simulated randomly per page reference.
    """
    frames = [-1] * num_frames
    ref_bits = [0] * num_frames
    mod_bits = [0] * num_frames
    pointer = 0
    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
            idx = frames.index(page)
            ref_bits[idx] = 1
            mod_bits[idx] = random.randint(0, 1)
        else:
            victim = None
            passes = 0
            while victim is None:
                for _ in range(num_frames):
                    r = ref_bits[pointer]
                    m = mod_bits[pointer]
                    if r == 0 and m == 0:
                        victim = pointer
                        break
                    elif r == 0 and m == 1:
                        if victim is None:
                            victim = pointer
                    else:
                        ref_bits[pointer] = 0
                    pointer = (pointer + 1) % num_frames

                passes += 1
                if victim is not None or passes >= 2:
                    break

            if victim is None:
                
                victim = pointer  # fallback victim to guarantee termination

    # Replace victim
    frames[victim] = page
    ref_bits[victim] = 1
    mod_bits[victim] = random.randint(0, 1)
    pointer = (victim + 1) % num_frames
    faults += 1
            
    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
