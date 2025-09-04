import os
import sys


def main():
    print("Copying programs to Raspberry Pi devices...")

    data_dir = os.path.dirname(os.path.abspath(__file__).replace("src", "data"))

    with open(f"{data_dir}/list-of-rpis", "r") as file:
        rpi_list = file.readlines()

    if not rpi_list:
        print("No Raspberry Pi devices found in rpi-list.")
        return

    with open(f"{data_dir}/list-of-programs", "r") as file:
        program_list = file.readlines()

    if not program_list:
        print("No programs found in program list.")
        return

    for rpi in rpi_list:
        rpi = rpi.strip()
        if not rpi:
            continue

        print(f"Processing Raspberry Pi: {rpi}")

        os.system(f"ssh {rpi} 'mkdir -p /home/pi/wcl'")
        for program in program_list:
            program = program.strip()
            if not program:
                continue

            print(f"Enabling {program} on {rpi}")
            os.system(f"ssh {rpi} 'cd /home/pi/wcl/{program} && source setup'")

        print(f"Finished processing {rpi}")


if __name__ == "__main__":
    main()
