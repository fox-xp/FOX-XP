import time, random, os, sys

# ============ COLORS ============
R = "\033[91m"   # Red
W = "\033[97m"   # White
B = "\033[90m"   # Black
G = "\033[92m"   # Green
C = "\033[96m"
Y = "\033[93m"
X = "\033[0m"

LEVEL = 1
XP = 0
SCORE = 0

def clear():
    os.system("clear")

def slow(t, d=0.02):
    for c in t:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

def load(msg="Processing"):
    for i in range(0, 101, 10):
        sys.stdout.write(f"\r{msg} {i}%")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def gain(p):
    global XP, LEVEL, SCORE
    XP += p
    SCORE += p * 2
    if XP >= LEVEL * 100:
        LEVEL += 1
        XP = 0
        slow(G + f"[LEVEL UP] Level {LEVEL}" + X)

def banner():
    clear()
    print(G + r"""
███████╗ ██████╗ ██╗  ██╗   ██╗██████╗ 
██╔════╝██╔═══██╗╚██╗██╔╝   ██║██╔══██╗
█████╗  ██║   ██║ ╚███╔╝    ██║██████╔╝
██╔══╝  ██║   ██║ ██╔██╗    ██║██╔═══╝ 
██║     ╚██████╔╝██╔╝ ██╗██╗██║██║     
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝╚═╝     
        FOX.XP – ADVANCED SIMULATOR
        EDUCATIONAL PURPOSE ONLY
""" + X)
    print(C + f"LEVEL: {LEVEL} | XP: {XP} | SCORE: {SCORE}" + X)
    print()

def fake_packet():
    return random.choice([
        "GET /admin 403",
        "GET /api/data 302",
        "POST /login 200 OK",
        "POST /upload 201",
        "PUT /session 200"
    ])

def fake_flood(target, auto=False):
    banner()
    slow(C + f"[TARGET] {target}" + X)
    slow(Y + "[MODE] Fake Data Flood" + X)
    rounds = 50 if auto else 20
    for i in range(1, rounds + 1):
        slow(G + f"[SENT] {fake_packet()} #{i}" + X, 0.01)
    load("Flooding")
    slow(G + "[DONE] Simulation Completed" + X)
    gain(20)
    input(Y + "ENTER to menu..." + X)

def fake_sql(target):
    banner()
    slow(C + f"[SQLi] Target: {target}" + X)
    for p in ["' OR '1'='1", "UNION SELECT NULL--", "'; DROP TABLE users--"]:
        slow(G + f"[PAYLOAD] {p}" + X)
    load("Injecting")
    slow(R + "[VULN] SQL Injection (SIMULATED)" + X)
    gain(30)
    input(Y + "ENTER to menu..." + X)

def lock_server(target):
    banner()
    slow(R + f"[LOCK SERVER] {target}" + X)
    for s in ["Analyzing load", "Freezing services", "Blocking requests"]:
        slow(G + "[INFO] " + s + X)
    load("Locking")
    slow(R + "[LOCKED] Server locked (SIMULATED)" + X)
    gain(25)
    input(Y + "ENTER to menu..." + X)

def menu(target):
    while True:
        banner()
        print(G + "[1] Fake Data Flood" + X)
        print(G + "[2] Auto Flood" + X)
        print(G + "[3] SQL Injection (Fake)" + X)
        print(G + "[4] Lock Server (Simulation)" + X)
        print(R + "[5] Exit" + X)
        c = input(Y + "FOX.XP > " + X).strip()
        if c == "1": fake_flood(target)
        elif c == "2": fake_flood(target, auto=True)
        elif c == "3": fake_sql(target)
        elif c == "4": lock_server(target)
        elif c == "5": sys.exit()
        else: slow(R + "Invalid option!" + X)

def main():
    banner()
    target = input(C + "Enter target (example.com): " + X).strip()
    if target:
        menu(target)

if __name__ == "__main__":
    main()
