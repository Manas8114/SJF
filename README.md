# SJF

Shortest Job First (SJF) CPU scheduling algorithm implementations — C++ console and Python/Flask web demo.

## Structure

```
SJF/
├── CPU-Scheduling-Algorithms-main/     # C++ implementation (copied from external source)
│   ├── CPU-Scheduling-Algorithms-main/
│   │   └── strf.cpp                    # Shortest Remaining Time First (preemptive SJF)
│   └── strf.cpp                        # Duplicate at root level
└── python/
    ├── SJF.py                          # Core SJF scheduling logic
    ├── models.py                       # Process data model
    ├── views.py                        # Flask routes
    ├── scheduling.html                 # Input form
    ├── results.html                    # Gantt chart + metrics output
    └── osapp/                          # Flask app package
```

## C++ Version (`strf.cpp`)

Preemptive Shortest Remaining Time First (SRTF) scheduler.

```cpp
// Input: n processes with arrival_time, burst_time
// Output: Gantt chart, waiting time, turnaround time, avg WT/TAT
```

Compile & run:
```bash
g++ strf.cpp -o sjf
./sjf
```

## Python/Flask Web Demo

### Files

| File | Role |
|------|------|
| `models.py` | `Process` class (pid, arrival, burst, completion, tat, wt) |
| `SJF.py` | `sjf_scheduling(processes)` → returns (scheduled_list, gantt_chart) |
| `views.py` | Flask routes: `/` (input), `/result` (compute + render) |
| `scheduling.html` | Form: dynamic process count, arrival/burst inputs |
| `results.html` | Table + Gantt chart (CSS bars), avg WT/TAT |

### Run

```bash
cd python
pip install flask
python views.py
# Open http://localhost:5000
```

### Algorithm (Non-preemptive SJF)

1. Sort by arrival time
2. At each completion, pick available process with shortest burst
3. Compute completion, TAT = completion - arrival, WT = TAT - burst
4. Generate Gantt chart segments: (pid, start, end)

## Screenshots

- Input: `scheduling.html` — dynamic form
- Output: `results.html` — process table + colored Gantt bars + averages

## Notes

- C++ version is SRTF (preemptive); Python version is non-preemptive SJF
- `CPU-Scheduling-Algorithms-main/` appears to be a forked/copied repo (nested duplicate folder)
- Academic / OS course project (2023)