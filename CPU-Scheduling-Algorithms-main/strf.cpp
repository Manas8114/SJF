#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct Process {
  int id;
  int arrivalTime;
  int burstTime;
  int waitingTime;
  int turnaroundTime;
};
bool arrivalTimeComparator(const Process &a, const Process &b) {
  return a.arrivalTime < b.arrivalTime;
}
int main() {
  int processCount;
  cout << "Enter the number of processes: ";
  cin >> processCount;
  vector<Process> processes(processCount);
  for (int i = 0; i < processCount; i++) {
    cout << "Enter the arrival time of process " << i + 1 << ": ";
    cin >> processes[i].arrivalTime;
    cout << "Enter the burst time of process " << i + 1 << ": ";
    cin >> processes[i].burstTime;
    processes[i].id = i + 1;
  }
  sort(processes.begin(), processes.end(), arrivalTimeComparator);
  int totalBurstTime = 0;
  for (int i = 0; i < processCount; i++) {
    totalBurstTime += processes[i].burstTime;
  }
  int currentTime = 0;
  vector<int> ganttChart(totalBurstTime);
  while (totalBurstTime > 0) {
    int shortestJobIndex = -1;
    for (int i = 0; i < processCount; i++) {
      if (processes[i].arrivalTime <= currentTime && processes[i].burstTime > 0) {
        if (shortestJobIndex == -1 || processes[i].burstTime < processes[shortestJobIndex].burstTime) {
          shortestJobIndex = i;
        }
      }
    }
    if (shortestJobIndex == -1) {
      currentTime++;
    } else {
      ganttChart[currentTime] = processes[shortestJobIndex].id;
      processes[shortestJobIndex].burstTime--;
      totalBurstTime--;
      for (int i = 0; i < processCount; i++) {
        if (i != shortestJobIndex && processes[i].arrivalTime <= currentTime) {
          processes[i].waitingTime++;
        }
      }
      if (processes[shortestJobIndex].burstTime == 0) {
        processes[shortestJobIndex].turnaroundTime = currentTime + 1 - processes[shortestJobIndex].arrivalTime;
      }

      currentTime++;
    }
  }
  for (int i = 0; i < processCount; i++) {
    cout << "Process " << processes[i].id << " (AT: " << processes[i].arrivalTime << ")\n";
    cout << "Waiting Time: " << processes[i].waitingTime << ", Turnaround Time: " << processes[i].turnaroundTime << "\n\n";
  }
  cout << "P0 is free space\n";
  cout << "Gantt Chart: ";
  for (int i = 0; i < ganttChart.size(); i++) {
    cout << "P" << ganttChart[i] << " ";
  }
  return 0;
}