def aging_algorithm_optimized(reference_string, num_frames, **kwargs):
    frames = []
    reference_bits = {}
    age_counters = {}
    faults = hits = 0

    for page in reference_string:
        # Set R=1 if hit
        if page in frames:
            hits += 1
            reference_bits[page] = 1
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
                reference_bits[page] = 1
                age_counters[page] = 0
            else:
                # Update all age counters before eviction
                for p in frames:
                    age_counters[p] = (age_counters[p] >> 1) | (reference_bits[p] << 7)
                    reference_bits[p] = 0  # Clear R bit after aging

                # Find page with lowest age
                victim = min(frames, key=lambda p: age_counters[p])
                frames.remove(victim)
                del reference_bits[victim]
                del age_counters[victim]

                frames.append(page)
                reference_bits[page] = 1
                age_counters[page] = 0

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
