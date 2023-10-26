import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
from PIL import Image, ImageTk

class SJFGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SJF Scheduling with GUI")
        self.process_data = []

        self.load_background_image()

        self.create_widgets()

    def load_background_image(self):
        background_image = Image.open("C:\\Users\\msgok\\Downloads\\_7f0e67a4-e894-4b8a-85c4-6b9bff05911d.jpeg")
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self.root, image=background_photo)
        background_label.place(relwidth=1, relheight=1)

        background_label.image = background_photo

    def create_widgets(self):
        label = tk.Label(self.root, text="Enter the number of processes:")
        label.pack()

        self.process_count_entry = tk.Entry(self.root)
        self.process_count_entry.pack()

        start_button = tk.Button(self.root, text="Start Scheduling", command=self.start_scheduling)
        start_button.pack()

    def start_scheduling(self):
        process_count = int(self.process_count_entry.get())

        for i in range(process_count):
            process_id = i + 1
            arrival_time = float(simpledialog.askfloat("Arrival Time", f"Enter Arrival Time for Process {process_id}:"))
            burst_time = float(simpledialog.askfloat("Burst Time", f"Enter Burst Time for Process {process_id}:"))
            self.process_data.append([process_id, arrival_time, burst_time, 0, burst_time])

        self.scheduling_process()

    def scheduling_process(self):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data = self.process_data

        process_data.sort(key=lambda x: x[1])

        while True:
            ready_queue = []
            normal_queue = []
            temp = []

            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])

                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break

                process_data[k][2] = process_data[k][2] - 1

                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)

            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])

                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break

                process_data[k][2] = process_data[k][2] - 1

                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)

        avg_turnaround_time = self.calculate_turnaround_time(process_data)
        avg_waiting_time = self.calculate_waiting_time(process_data)

        self.print_data(process_data, avg_turnaround_time, avg_waiting_time, sequence_of_process)

    def calculate_turnaround_time(self, process_data):
        total_turnaround_time = 0

        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)

        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculate_waiting_time(self, process_data):
        total_waiting_time = 0

        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)

        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def print_data(self, process_data, avg_turnaround_time, avg_waiting_time, sequence_of_process):
        result_text = "Process_ID  Arrival_Time  Rem_Burst_Time  Completed  Orig_Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time\n"

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                result_text += str(process_data[i][j]) + "\t\t"

            result_text += "\n"

        result_text += f'Average Turnaround Time: {avg_turnaround_time}\n'
        result_text += f'Average Waiting Time: {avg_waiting_time}\n'
        result_text += f'Sequence of Process: {sequence_of_process}'

        self.display_result(result_text)

    def display_result(self, result_text):
        result_window = tk.Tk()
        result_window.title("SJF Scheduling Result")

        result_text_widget = scrolledtext.ScrolledText(result_window, width=120, height=40)
        result_text_widget.insert(tk.INSERT, result_text)
        result_text_widget.pack()

        result_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = SJFGUI(root)
    root.geometry("400x300") 
    root.mainloop()
