def page_buffering_optimized(reference_string, num_frames, **kwargs):
    from collections import deque, defaultdict

    frames = []
    buffer = deque(maxlen=3)  # Page buffer with capacity 3
    buffer_use = defaultdict(int)

    faults = hits = 0

    for page in reference_string:
        if page in frames:
            hits += 1
        elif page in buffer:
            # Restore from buffer (no real fault)
            buffer.remove(page)
            frames.append(page)
            buffer_use[page] += 1
            hits += 1
        else:
            faults += 1
            if len(frames) < num_frames:
                frames.append(page)
            else:
                # Eviction needed
                # Move LRU or least reused page to buffer
                evicted = frames.pop(0)
                buffer.append(evicted)
                buffer_use[evicted] += 1
                frames.append(page)

    total = len(reference_string)
    return {
        "faults": faults,
        "hits": hits,
        "fault_ratio": faults / total,
        "hit_ratio": hits / total
    }
