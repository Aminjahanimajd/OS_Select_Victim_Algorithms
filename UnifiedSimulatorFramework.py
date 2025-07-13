import time
import tracemalloc
import pandas as pd
from typing import List, Dict, Any
from FIFO import fifo
from OPT import optimal
from LFU import lfu
from MFU import mfu
from SecondChance import second_chance
from EnhancedSecondChance import enhanced_second_chance
from Aging import aging_algorithm
from Paging import page_buffering
from AgingOptimized import aging_algorithm_optimized
from EnhancedSecondChanceOptimized import enhanced_second_chance_optimized
from PagingOptimized import page_buffering_optimized

def run_algorithm(algorithm, reference_string: List[int], num_frames: int, **kwargs) -> Dict[str, Any]:
    import time, tracemalloc
    tracemalloc.start()
    start = time.perf_counter()

    result = algorithm(reference_string, num_frames, **kwargs)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    result['execution_time'] = end - start
    result['memory_usage'] = peak
    return result

def generate_reference_string(length: int, max_page: int) -> List[int]:
    import random
    return [random.randint(0, max_page) for _ in range(length)]

def main():
    frame_sizes = [3, 5, 7]
    reference_lengths = [50, 100, 200]
    
    algorithms = {
        "FIFO": fifo,
        "OPT": optimal,
        "LFU": lfu,
        "MFU": mfu,
        "Second Chance": second_chance,
        "Enhanced Second Chance": enhanced_second_chance,
        "Aging (NFU)": aging_algorithm,
        "Page Buffering": page_buffering,
        "Aging Optimized": aging_algorithm_optimized,
        "Enhanced Second Chance Optimized": enhanced_second_chance_optimized,
        "Page Buffering Optimized": page_buffering_optimized
    }

    results = []

    for length in reference_lengths:
        reference_string = generate_reference_string(length, max_page=10)
        for frame_size in frame_sizes:
            for name, algo in algorithms.items():
                print(f"Running {name} - RefLen: {length}, Frames: {frame_size}")
                result = run_algorithm(algo, reference_string, frame_size)
                results.append({
                    "Algorithm": name,
                    "Reference Length": length,
                    "Frame Size": frame_size,
                    "Fault Ratio": result["fault_ratio"],
                    "Hit Ratio": result["hit_ratio"],
                    "Execution Time": result["execution_time"],
                    "Memory Usage": result["memory_usage"]
                })

    # Save or print results
    df = pd.DataFrame(results)
    df.to_csv("algorithm_comparison_results.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()
    