shelf = {}

for z in range(3):
    for x in range(6):
        cube_id = f"CUBE-{x}-{z}"
        shelf[cube_id] = {
            "position": (x, z),
            "dimensions": (1, 1, 1),
            "occupied": False,
            "contents": None
        }

def place_box(x, z, label="Box"):
    cube_id = f"CUBE-{x}-{z}"
    if cube_id not in shelf:
        print(f"❌ No cube at ({x}, {z})")
        return
    if shelf[cube_id]["occupied"]:
        print(f"⚠️ Spot at ({x}, {z}) is already taken.")
        return
    shelf[cube_id]["occupied"] = True
    shelf[cube_id]["contents"] = label
    print(f"✅ Placed {label} at ({x}, {z})")

def remove_box(x, z):
    cube_id = f"CUBE-{x}-{z}"
    if cube_id not in shelf or not shelf[cube_id]["occupied"]:
        print(f"🚫 Nothing to remove at ({x}, {z})")
        return
    shelf[cube_id]["occupied"] = False
    shelf[cube_id]["contents"] = None
    print(f"🧽 Removed box from ({x}, {z})")

def print_shelf():
    print("\n📦 Shelf View:\n")
    for z in reversed(range(3)):
        row = f"Tier {z}: "
        for x in range(6):
            cube = shelf[f"CUBE-{x}-{z}"]
            row += "[■] " if cube["occupied"] else "[ ] "
        print(row)
    print()

print("✅ Shelf system loaded.")
print("Type commands like: add x z, remove x z, print, quit")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "quit":
        print("👋 Exiting.")
        break

    elif cmd == "print":
        print_shelf()

    elif cmd.startswith("add "):
        try:
            _, x, z = cmd.split()
            place_box(int(x), int(z), f"Box-{x}-{z}")
        except:
            print("❗ Usage: add x z")

    elif cmd.startswith("remove "):
        try:
            _, x, z = cmd.split()
            remove_box(int(x), int(z))
        except:
            print("❗ Usage: remove x z")

    else:
        print("❓ Unknown command. Try: add x z, remove x z, print, quit")
