# 🔒 Packet Filtering Stack

A **C and Python-based firewall packet processor** that uses a **stack (LIFO)** data structure to simulate packet filtering. This project also includes a simple **Tkinter-based GUI** for user-friendly interaction.

Ideal for showcasing your understanding of **Data Structures**, **Networking**, and **GUI development**.

---

## 📁 Project Structure

packet-filtering-stack/
├── dsa.c # Packet stack logic using C (LIFO)
├── guidsa.py # Python GUI using Tkinter
├── packets.txt # Sample input packets
├── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## 🧠 Features

- 🔁 Stack operations: `push`, `pop`, `peek`
- 🧱 Packet structure in C using `struct`
- 📦 Packet processing rules (ALLOW / BLOCK)
- 🎨 Tkinter GUI for entering or viewing packet data
- 📝 Sample input via `packets.txt`
- ❌ Handles invalid or unmatched packets

---

## ⚙️ How It Works

### ✅ C Program (`dsa.c`)

- Uses a static array stack to store packets.
- Each `Packet` includes:
  - ID
  - Source IP
  - Destination IP
  - Action (`ALLOW` or `BLOCK`)
- Processes packets in **Last In First Out** order using stack logic.

### ✅ Python GUI (`guidsa.py`)

- User can input packet data or simulate loading from file.
- Packets are compared against a basic firewall rule list:
  
```python
rules = [
    {"src_ip": "192.168.1.1", "dest_ip": "192.168.1.2", "action": "allow"},
    {"src_ip": "192.168.1.3", "dest_ip": "192.168.1.4", "action": "allow"},
    {"src_ip": "192.168.1.2", "dest_ip": "192.168.1.3", "action": "block"},
]
GUI shows whether each packet matches any rule or not.

📝 Sample Input (packets.txt)
txt
Copy
Edit
# Format: ID SourceIP DestinationIP Action
1 192.168.1.1 192.168.1.2 ALLOW
2 192.168.1.2 192.168.1.3 BLOCK
3 192.168.1.3 192.168.1.4 ALLOW
4 10.0.0.1 10.0.0.2 BLOCK
5 172.16.0.5 172.16.0.10 ALLOW
🚀 How to Run
Compile and Run the C File:
bash
Copy
Edit
gcc dsa.c -o dsa_stack
./dsa_stack
Run the Python GUI:
bash
Copy
Edit
python guidsa.py
✅ Python 3 and Tkinter must be installed.

📸 GUI Screenshots
(Add a screenshot here later by saving one in assets/ and linking it)

✨ Future Enhancements
Read firewall rules from external config

Add queue-based (FIFO) version

Export processed packets to CSV/log file

Better GUI styling with themes and logs

Combine C + Python interaction using sockets or subprocess (bonus)

👨‍💻 Author
Mohit Sahoo
GitHub: @MohitSahoo
