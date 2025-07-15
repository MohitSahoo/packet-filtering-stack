import tkinter as tk
from tkinter import messagebox


# Store the packet data
packet_list = []

def process_packet():
    packet_data = process_input.get("1.0", tk.END).strip()

    # Handle input that was copied and pasted with newlines
    if packet_data.endswith("\n"):
        packet_data = packet_data[:-1]

    if not packet_data:
        messagebox.showwarning("Input Error", "Please enter packet data.")
        return

    # Split the input into individual lines (each line should be a packet)
    packet_lines = packet_data.split("\n")
    processed_data = []

    for line in packet_lines:
        fields = line.split(",")  # Assuming comma separation
        if len(fields) != 4:
            processed_data.append(f"Invalid packet format: {line}")
            continue

        packet_id, src_ip, dest_ip, action = fields
        result = process_packet_logic(packet_id.strip(), src_ip.strip(), dest_ip.strip(), action.strip())
        processed_data.append(result)

    # Add the processed packet to the list
    packet_list.append("\n".join(processed_data))

    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, "\n".join(processed_data))


def process_packet_logic(packet_id, src_ip, dest_ip, action):
    # Simulate packet processing logic with firewall rules
    rules = [
        {"src_ip": "192.168.1.1", "dest_ip": "192.168.1.2", "action": "allow"},
        {"src_ip": "192.168.1.3", "dest_ip": "192.168.1.4", "action": "allow"},
        {"src_ip": "192.168.1.2", "dest_ip": "192.168.1.3", "action": "block"},

    ]

    # Check if the packet matches any rule
    for rule in rules:
        if rule["src_ip"] == src_ip and rule["dest_ip"] == dest_ip:
            if rule["action"] == "allow":
                return f"Packet {packet_id} from {src_ip} to {dest_ip} is ALLOWED."
            elif rule["action"] == "block":
                return f"Packet {packet_id} from {src_ip} to {dest_ip} is BLOCKED."

    return f"Packet {packet_id} from {src_ip} to {dest_ip} does not match any rules and is BLOCKED by default."


def pop_packet():
    if not packet_list:
        messagebox.showwarning("No Packets", "No packets to pop.")
        return

    # Remove the last packet from the list
    packet_list.pop()

    # Update the result output
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, "Remaining Packets:\n")
    result_output.insert(tk.END, "\n".join(packet_list))


# GUI part remains the same
root = tk.Tk()
root.title("Firewall Packet Processing")
root.configure(bg='#1E1E2F')

heading_label = tk.Label(root, text="FIREWALL PACKET PROCESSOR", font=("Helvetica", 32, "bold"), bg='#1E1E2F',
                         fg='#FFD700')
heading_label.pack(pady=30)

input_label = tk.Label(root, text="Enter Packet Details (Format: ID, Src IP, Dest IP, Action):", bg='#1E1E2F',
                       fg='white', font=("Helvetica", 16))
input_label.pack(pady=10)

process_input = tk.Text(root, height=12, width=60, bg='#2E2E2E', fg='white', font=("Helvetica", 16))
process_input.pack(pady=10)

detect_button = tk.Button(root, text="Process Packet", command=process_packet, height=3, width=25, bg='#FFD700',
                          fg='black', font=("Helvetica", 16, "bold"))
detect_button.pack(pady=15)

clear_button = tk.Button(root, text="Clear All", command=lambda: process_input.delete("1.0", tk.END), height=3,
                         width=25, bg='#FF4500', fg='black', font=("Helvetica", 16, "bold"))
clear_button.pack(pady=10)

pop_button = tk.Button(root, text="Pop Packet", command=pop_packet, height=3, width=25, bg='#FF6347', fg='black',
                       font=("Helvetica", 16, "bold"))
pop_button.pack(pady=10)

output_label = tk.Label(root, text="Result Output:", bg='#1E1E2F', fg='white', font=("Helvetica", 16))
output_label.pack(pady=10)

result_output = tk.Text(root, height=12, width=60, bg='#2E2E2E', fg='white', font=("Helvetica", 16), state=tk.NORMAL)
result_output.pack(pady=10)

root.mainloop()
