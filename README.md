# OS Select‑Victim Algorithms

**Author**: Amin Jahanimajd  
**Date**: 2025  

---

## 📖 Project Overview

This project implements and compares various *victim‑selection (page replacement)* algorithms (used in operating systems) via a unified simulation framework. It allows evaluation of algorithm performance under different workloads and scenarios, and provides visualizations and comparative results.

The following algorithms are implemented:

- FIFO  
- Second Chance  
- Enhanced Second Chance  
- Aging  
- Aging (Optimized)  
- LFU  
- MFU  
- OPT (Optimal)  
- Paging / PagingOptimized  

Additionally:
- A **UnifiedSimulatorFramework** to run simulations in a modular way  
- **plot_results.py** to generate comparative graphs  
- **algorithm_comparison_results.csv** — sample output data  
- **Victim_Selection_Algorithm.pptx** — presentation about the algorithms  

---

## 🛠️ Features

- Modular simulation of multiple page replacement algorithms  
- Easy to add new algorithms  
- Capability to run experiments and generate comparison metrics  
- Visualization of results (plots)  
- CSV output for further analysis  

---

## 📂 Repository Structure

```
.
├── Aging.py  
├── AgingOptimized.py  
├── EnhancedSecondChance.py  
├── EnhancedSecondChanceOptimized.py  
├── FIFO.py  
├── LFU.py  
├── MFU.py  
├── OPT.py  
├── Paging.py  
├── PagingOptimized.py  
├── SecondChance.py  
├── UnifiedSimulatorFramework.py  
├── plot_results.py  
├── algorithm_comparison_results.csv  
├── Victim_Selection_Algorithm.pptx  
└── plots/             ← folder of generated plot images  
```

- **Simulator & Algorithm Files**: Each algorithm in its own `.py` file, plus a central **UnifiedSimulatorFramework**  
- **plot_results.py**: script to convert CSV results into visual charts  
- **plots/**: directory containing graphs (e.g. PNGs) from past runs  
- **algorithm_comparison_results.csv**: sample comparison data  
- **Victim_Selection_Algorithm.pptx**: presentation (slides) describing methods  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+  
- Recommended packages: `numpy`, `matplotlib`, `pandas`  

You can install dependencies via:

```bash
pip install numpy matplotlib pandas
```

### Running Simulations

1. In **UnifiedSimulatorFramework.py**, configure simulation parameters such as:
   - traces or access strings  
   - number of frames  
   - which algorithms to run  

2. Run the simulator:

```bash
python UnifiedSimulatorFramework.py
```

This will output a CSV (or append to existing) with metrics such as hit rate, page fault count, etc.

3. To generate plots from CSV:

```bash
python plot_results.py
```

Resulting graphs will be stored in the `plots/` folder.

---

## 📊 Performance Metrics & Interpretation

Typical metrics evaluated include:

- **Page fault rate / hit rate**  
- **Average time / cost** (if modeled)  
- **Comparative advantage of algorithms under different trace patterns**  

You can use the CSV data to draw insights like:
- Which algorithms perform better under low vs high locality  
- How “optimized” variants improve over naive ones  
- Tradeoffs between complexity and performance  

---

## 🧩 Extending the Project

To add a new algorithm:

1. Create a new `.py` file with the algorithm logic, following the interface used in existing algorithms.  
2. Import it in **UnifiedSimulatorFramework.py** and include it in experiments.  
3. Run simulation and compare results.  
4. (Optional) Add documentation / comments and include in plots.

---

## ✅ Example Usage

```bash
# Run simulation for, say, FIFO, Second Chance, and OPT:
python UnifiedSimulatorFramework.py --algorithms FIFO SecondChance OPT --frames 100 --trace sample_trace.txt

# Then plot results:
python plot_results.py --input algorithm_comparison_results.csv --output plots/
```

*(Adapt flags or parameters as per your implementation.)*

---

## 📝 Notes & Limitations

- The optimal algorithm (OPT) is theoretical and uses knowledge of future references; it’s used only for benchmarking.  
- The simulation does not (currently) model real time latency or I/O costs.  
- For large traces and many algorithms, computation time may grow.  
- “Optimized” variants trade off readability for performance; make sure they’re correct by cross-verification.

---

## 📁 Sample Data & Plots

Sample CSV and plots are already included:

- `algorithm_comparison_results.csv`  
- `plots/` folder with example graphs  

These show how algorithm performance varies under different workloads.

---

## 🧰 Technologies & Libraries

- Python 3.x  
- `numpy` for numerical operations  
- `pandas` (optional) for handling CSV / data  
- `matplotlib` for plotting  

---

## 🎓 For Students & Researchers

This repository is suitable as a teaching or research tool to experiment with page replacement policies, simulate memory management strategies, and analyze their tradeoffs.

---

## 📬 Contact & License

If you have questions or suggestions, feel free to contact:

**Name**: Amin Jahanimajd  
**Email**: *(your email here)*  

---

**License**: *Add a license if applicable (e.g. MIT, Apache 2.0, etc.)*
