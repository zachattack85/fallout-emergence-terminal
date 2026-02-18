import os
import time
import random

VAULT_NUMBER = 44


# ---------- Input Helpers ----------

def choose_int(prompt: str, valid_choices: tuple[int, ...]) -> int:
    """Safely ask for an integer choice from a set of valid options."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Choose one of: {valid_choices}\n")
        except ValueError:
            print("Please enter a number.\n")


def choose_yn(prompt: str) -> str:
    """Safely ask for Y/N input."""
    while True:
        ans = input(prompt).strip().upper()
        if ans in ("Y", "N"):
            return ans
        print('Please enter "Y" or "N".\n')


# ---------- UI / Boot ----------

def set_terminal_color():
    # Retro green terminal color (Windows). Harmless on other OS.
    try:
        os.system("color 0A")
    except Exception:
        pass


def terminal_boot_sequence():
    print("\n\nInitializing Vault-Tec™ Terminal Interface...")
    time.sleep(1.5)
    print("Verifying Pip-Boy sync... OK.")
    time.sleep(1)
    print("Authenticating biometric user ID... ACCEPTED.")
    time.sleep(1)
    print("Launching Fallout: Emergence...\n\n\n")
    time.sleep(2)


def print_title():
    print("==============================")
    print("     Fallout: Emergence")
    print("   A Text-Based Adventure")
    print("==============================\n\n\n")
    print(f"Location: Vault {VAULT_NUMBER}, St. Louis, Missouri")
    print("Date: 2292\n\n")
    time.sleep(3)


# ---------- Character Setup ----------

def get_player_name() -> str:
    name = input("Hello Vault Dweller. Please enter your character name into your Vault-Tec Pip-Boy. ").strip()
    print("\n\n")
    if not name:
        name = "Vault Dweller"
    print(
        f"Thank you {name}, your Pip-Boy has now been registered to the Vault {VAULT_NUMBER} "
        f"Vault-Tec Mainframe.\n\n"
    )
    time.sleep(1)
    return name


def assign_stats(name: str) -> dict[str, int]:
    special_assign = choose_yn(
        f'{name}, would you like your Vault-Tec Pip-Boy to assign your S.P.E.C.I.A.L. stats? (Y/N) > '
    )
    print("\n\n")

    if special_assign == "Y":
        stats = {k: random.randint(1, 5) for k in ("S", "P", "E", "C", "I", "A", "L")}
    else:
        stats = {k: 0 for k in ("S", "P", "E", "C", "I", "A", "L")}

    return stats


def display_stats(stats: dict[str, int]):
    print("\nWhat makes you S.P.E.C.I.A.L.?\n\n")
    for stat, value in stats.items():
        print(f"{stat}: {value}", end="  ")
    print("\n\n")
    time.sleep(3)


# ---------- Story Blocks ----------

def intro_story(name: str):
    print("==========")
    print("  INTRO:  ")
    print("==========\n\n")
    time.sleep(2)

    print(
        f"You are {name}, a lifelong resident of Vault {VAULT_NUMBER}, one of the few still-functioning Vault-Tec facilities "
        "buried beneath the ruins of St. Louis, Missouri. Life in the vault has been strictly regulated, monotonous… but safe.\n\n"
    )
    time.sleep(10)

    print("Until today....\n\n")
    time.sleep(3)

    print("A low rumble shakes your bunk. Sirens begin to blare. The lights above flicker. Your Pip-Boy vibrates and flashes:\n\n")
    time.sleep(4)

    print('"EMERGENCY: Reactor instability detected. Containment breach imminent. Vault evacuation recommended."\n\n')
    time.sleep(5)

    print(
        "You zip up your vault-suit with a sharp shhhk, the sound slicing through the tension in the air. "
        "You slam your boots to the ground, one after the other, bracing yourself against the tremors as the Vault rumbles around you. "
        'Heart pounding, you take a steadying breath... "this is it.." Something has gone horribly wrong — and you may not have much time.\n\n'
    )

    print("Yesterday you were a Vault Dweller.\n")
    time.sleep(4)

    print("Today...", end="", flush=True)
    time.sleep(2)
    print(" you become a Wasteland Wanderer.\n")

    print("===========================================\n\n")
    time.sleep(2)


# ---------- Decision 1 ----------

def decision_one(name: str) -> tuple[int, str, bool]:
    """Returns (decision_1, current_path, has_pistol)."""
    print("Decision 1: What's your first move, Wanderer?\n")
    print("   1) Check your locker for supplies.")
    print("   2) Rush to the Overseer's office.")
    print("   3) Head to the main Vault Door control room.\n")

    decision_1 = choose_int("Enter the number of your choice: ", (1, 2, 3))
    print("\n===========================================\n\n")

    current_path = ""
    has_pistol = False

    if decision_1 == 1:
        print("You check your locker, inside you find:\n")
        time.sleep(1.5)
        print("  - A spare Vault 44 jumpsuit")
        time.sleep(1)
        print("  - A 10mm pistol with 4 bullets")
        time.sleep(1)
        print('  - A worn holo-tape labeled "Remember who you are..."\n\n')
        time.sleep(1.2)
        has_pistol = True

        print("You have emptied your locker. Where do you go?\n")
        print("   1) Rush to the Overseer's office.")
        print("   2) Head to the main Vault Door control room.\n")

        decision_1_5 = choose_int("Where do you go? ", (1, 2))
        print("\n\n")

        if decision_1_5 == 1:
            current_path = "the Overseer's office"
            overseer_office()
        else:
            current_path = "the Vault Door control room"
            vault_door_control_room()

    elif decision_1 == 2:
        current_path = "the Overseer's office"
        overseer_office()

    else:
        current_path = "the Vault Door control room"
        vault_door_control_room()

    return decision_1, current_path, has_pistol


def overseer_office():
    print("You run to the Overseer's office.\n")
    time.sleep(2)
    print("The door is cracked open, you slowly walk inside.\n")
    time.sleep(2)
    print("Inside: chaos. Blood on the floor. The Overseer's chair is empty.\n")
    time.sleep(2)
    print("A terminal on the Overseer's desk blinks with corrupted files. A note on the desk reads:\n")
    time.sleep(2)
    print('"Project Chimera was never shut down. Do not trust Vault-Tec."')
    print("\n\n")


def vault_door_control_room():
    print("You walk to the Vault Door control room.\n")
    time.sleep(2)
    print("The heavy door looms before you, sealed tight. A nearby console displays:\n")
    time.sleep(2)
    print('"Power failure. Manual reset required in Reactor Core."')
    print("\n\n")


# ---------- Skill Check 1 ----------

def skill_check(stats: dict[str, int], current_path: str) -> int:
    time.sleep(2)
    print(f"After leaving {current_path}, you find your usual hallway blocked by fallen debris\n")
    time.sleep(1)
    print("A side door is jammed shut. Next to it, a narrow vent is just barely big enough for someone agile to squeeze through.\n")
    time.sleep(1)

    print("Do you:\n")
    time.sleep(0.7)
    print("  1) Try to force the door open")
    print("  2) Crawl through the vent")
    print("  3) Turn around and find another way\n")

    choice = choose_int("Please make your decision: ", (1, 2, 3))
    print("\n")

    if choice == 1:
        if stats["S"] >= 4:
            print("You grunt and shove until the metal creaks open. Shortcut unlocked!\n")
            time.sleep(1)
            print("Your STRENGTH is impressive!\n")
        else:
            print("You strain… but nothing. Your muscles ache.\n")
            time.sleep(1)
            print("Your STRENGTH was too low.\n")

    elif choice == 2:
        if stats["A"] >= 4:
            print("You slide through the vent quickly and quietly. Shortcut unlocked!\n")
            time.sleep(1)
            print("Your AGILITY is impressive!\n")
        else:
            print("You get stuck and must backtrack.\n")
            time.sleep(1)
            print("Your AGILITY was too low.\n")

    else:
        print("You detour through a dark tunnel.\n")

    print("\n")
    time.sleep(2)
    return choice


# ---------- Decision 2 ----------

def decision_two(name: str, stats: dict[str, int], has_pistol: bool, skill_choice: int) -> tuple[int, bool]:
    print("===========================================\n\n")
    print(f"Decision 2: Where do you go from here, {name}?\n")
    print("   1) Reactor Core (Reset the power grid)")
    print("   2) Medlab (Search for healing items or clues)")
    print("   3) Security Wing (Find weapons or files)\n")

    decision_2 = choose_int("Enter the number of your choice: ", (1, 2, 3))
    print("\n\n===========================================\n\n")

    # Light flavor text if the shortcut succeeded
    if decision_2 == 1:
        print("You head toward the Reactor Core...\n")
        time.sleep(1)
        return decision_2, reactor_core(stats, has_pistol)
    if decision_2 == 2:
        medlab(stats)
        return decision_2, False
    if decision_2 == 3:
        security_wing()
        return decision_2, False

    return decision_2, False


def reactor_core(stats: dict[str, int], has_pistol: bool) -> bool:
    """Returns True if game_over triggered here."""
    print(
        "You make your way to the Reactor Core. "
        "The walls hum with unstable energy. A scorched Mr. Handy lies sparking beside a console.\n"
        "Flashing on the console a prompt reads.\n"
    )
    time.sleep(2)

    emergency_reset = choose_yn('"Emergency Reset: [Y/N]" ')
    print("\n")
    time.sleep(1)

    if emergency_reset == "N":
        print("Nothing happens. You'll need to find another way out.\n")
        return False

    # emergency_reset == "Y"
    print(
        "The system reboots… but in the dark, something stirs. "
        "A mutated Chimera hybrid, Vault-Tec's last experiment, awakens. You may have to fight.\n"
    )
    time.sleep(1.5)

    if stats["P"] >= 3:
        print("You have great PERCEPTION and were able to sneak out of the Reactor Core.\n")
        return False

    if stats["S"] >= 3:
        print("The Chimera hybrid charges.\n")
        time.sleep(1)

        if has_pistol:
            print("You pull out your 10mm pistol and aim for the Chimera's head.\n")
            print("CRITICAL HIT!\n")
            print("The Chimera lies motionless on the floor.\n")
        else:
            print("You have no weapon so you'll have to fight bare handed.\n")
            time.sleep(1.5)
            print("Because of your STRENGTH you were able to defeat the Chimera.\n")
        return False

    # Too weak
    print("The Chimera hybrid charges.\n")
    time.sleep(1)
    print("You are too weak to protect yourself.\n")
    time.sleep(1)
    print("The Chimera starts a violent attack.\n")
    time.sleep(1.5)
    print("You were defeated by the Chimera.\n\n")
    print("GAME OVER.")
    return True


def medlab(stats: dict[str, int]):
    print("You hurry towards the Medlab.")
    print("As you reach the Medlab, dim lights reveal rows of ransacked cabinets.\n")
    print("You scavenge:\n")
    time.sleep(1)
    print(" - 2 Stimpaks")
    time.sleep(1)
    print(" - 1 RadAway")
    time.sleep(1)
    print(' - A mysterious syringe labeled “S.P.E.C.I.A.L. - Experimental Use Only”\n')
    time.sleep(1.5)

    syringe = choose_yn("Do you use the mysterious syringe? (Y/N): ")
    print()

    if syringe == "Y":
        chosen_stat = random.choice(list(stats.keys()))
        stats[chosen_stat] += 1
        print("You inject the mysterious serum... Something surges through you!")
        time.sleep(1.2)
        print(f"\nYour {chosen_stat} stat has increased by +1!\n")
    else:
        print("You tuck it away, but it may come in handy later…\n")

    print("Current S.P.E.C.I.A.L. Stats:\n")
    for stat, value in stats.items():
        print(f"{stat}: {value}", end="  ")
    print("\n\n")

    holo = choose_yn("Beside a locked cryo-pod, a holo-tape awaits. Play it? (Y/N): ")
    print("\n")
    if holo == "Y":
        print("The Overseer's voice:\n")
        time.sleep(1)
        print('"Subject 12 is unstable. We froze her. If she wakes up… Vault 44 burns."')
    else:
        print("You stash the holo-tape and move on.")
    print("\n")


def security_wing():
    print("You rush to the Security Wing.\n")
    print("As you enter you notice gear is scattered all across the floor.\n")
    time.sleep(1)
    print("You find:\n")
    time.sleep(1)
    print(" - A security baton")
    time.sleep(1)
    print(" - 6 more 10mm bullets")
    time.sleep(1)
    print(' - A holotape titled “EXIT PROTOCOLS”\n')
    time.sleep(1)

    holo = choose_yn("Play the holo-tape? (Y/N): ")
    print("\n")
    if holo == "Y":
        print("A whisper:\n")
        time.sleep(1)
        print('"To unlock the vault, you\'ll need Overseer biometric ID. She didn\'t make it far."\n')
    else:
        print("You pocket the holo-tape and move on.\n")


# ---------- Decision 3 / Endings ----------

def decision_three(name: str, stats: dict[str, int]) -> bool:
    """Returns True if game_over."""
    time.sleep(2)
    print("\n\n===========================================\n\n")
    print(f"Decision 3: How will you escape Vault {VAULT_NUMBER}, {name}?\n")
    print("   1) Find the Overseer's body to spoof her biometric key.")
    print("   2) Overload the reactor to force the vault door open.")
    print("   3) Sneak through the old maintenance tunnels to the surface.\n")

    decision_3 = choose_int(f"Please make your decision, {name}: ", (1, 2, 3))
    print("\n===========================================\n\n")

    if decision_3 == 1:
        if stats["E"] >= 3:
            print("You track the Overseer's corpse to the backup generator wing.\n")
            print("Using her handprint and Pip-Boy ID, you access the Vault Door terminal.\n")
            time.sleep(2)
            print("A slow hiss builds to a roar as the vault door groans open.\n")
            time.sleep(2)
            print("Blinding light pours in from the Wasteland beyond.\n")
            time.sleep(2)
            print("You step into freedom.\n")
            print("Your life as a Wasteland Wanderer begins.")
            return False
        else:
            print("You track the Overseer's corpse to the backup generator wing.\n")
            print("Using her handprint and Pip-Boy ID, you access the Vault Door terminal.\n")
            time.sleep(2)
            print("As you scan the Overseer's Pip-Boy, a punctured coolant line bursts nearby.\n")
            print("Toxic gas floods the chamber before the vault door can fully open.\n")
            time.sleep(1.5)
            print("You cough violently. Vision blurs. Your body collapses before your fingers leave the keypad.\n")
            time.sleep(1.5)
            print("GAME OVER!\n")
            print("You didn't have the endurance to survive the final moments of Vault 44.")
            return True

    if decision_3 == 2:
        print("You cobble together tools, wires, and raw luck. A risky overload plan...\n")
        time.sleep(2)
        print("You run through the maze of halls towards the Reactor Core.\n")
        time.sleep(2)
        print("You rush to the side of the Core and stare at an access panel with a warning:\n")
        time.sleep(2)
        print('"DANGER: EXTREMELY HIGH VOLTAGE!"\n')
        time.sleep(2)

        if stats["I"] >= 3:
            print("KA-THOOM!!!\n")
            time.sleep(1.5)
            print("The blast throws you backward as the vault door is blasted off its hinges.\n")
            print("Fire. Dust. Silence. The only path is forward.\n")
            time.sleep(2)
            print("You emerge, scarred but free, ready for the unknown.\n")
            return False
        else:
            print("You miscalculate the wire sequence. The reactor overloads faster than expected.\n")
            time.sleep(2)
            print("KA-THOOM!!!\n")
            time.sleep(2.5)
            print("A sudden flash of light... then nothing. The explosion collapses the vault — with you still inside.\n")
            time.sleep(2)
            print("GAME OVER!\n")
            print("You lacked the knowledge to make the overload survivable.")
            return True

    # decision_3 == 3
    print('You rush to a door you\'ve passed many times labeled: "Maintenance"\n')
    time.sleep(2)
    print("You go inside the maintenance area hoping you can find anything that could help you out.\n")
    time.sleep(2)
    print("A tool")
    time.sleep(1)
    print("An override key")
    time.sleep(1)
    print("ANYTHING!!\n")
    time.sleep(2)

    print("Then you spot it in the far corner.\n")
    time.sleep(2)
    print("A crumbling air duct.\n")
    time.sleep(2)
    print("It must have collapsed from all of this rumbling and tremors tearing through the Vault.\n")
    time.sleep(2)
    print("You crawl inside of the air duct.\n")
    time.sleep(2)
    print("The duct leads through winding sub-level tunnels filled with vermin and collapsed walls.\n")
    time.sleep(2)

    if stats["L"] >= 3:
        print("Eventually, you find a rusted hatch. It opens with a creak...\n")
        time.sleep(2)
        print("With a deep breath you crawl through the opening..\n")
        time.sleep(2)
        print("For the first time in your life, you see stars!\n")
        time.sleep(2)
        print("You are no longer a Vault Dweller. You are a Wasteland Wanderer.")
        return False
    else:
        print("As you crawl through a tunnel, the rotted ceiling above you groans... then caves in.\n")
        time.sleep(2)
        print("Crushed beneath rusted rebar and crumbling concrete, you never see the stars.\n")
        time.sleep(2)
        print("GAME OVER!")
        print("You were so close… but luck was not on your side.")
        return True


# ---------- Main ----------

def main():
    set_terminal_color()
    terminal_boot_sequence()
    print_title()

    name = get_player_name()
    stats = assign_stats(name)
    display_stats(stats)

    intro_story(name)

    decision_1, current_path, has_pistol = decision_one(name)
    skill_choice = skill_check(stats, current_path)

    # Decision 2
    decision_2, game_over = decision_two(name, stats, has_pistol, skill_choice)
    if game_over:
        input("\nPress Enter to exit the Vault...")
        return

    # Decision 3 / Ending
    game_over = decision_three(name, stats)

    print("\n\n")
    if game_over:
        input("\nPress Enter to exit the Vault...")
    else:
        print("\nThanks for playing!\n\n")
        input("Press Enter to exit the Vault....")


if __name__ == "__main__":
    main()
