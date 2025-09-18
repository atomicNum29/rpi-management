import os
import sys
import concurrent.futures


def main():
    print("Enabling programs to Raspberry Pi devices...")

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

    def process_rpi(rpi):
        rpi = rpi.strip()
        if not rpi:
            return

        print(f"Processing Raspberry Pi: {rpi}")
        os.system(f"ssh {rpi} 'mkdir -p /home/pi/wcl'")
        for program in program_list:
            program_name = program.strip()
            if not program_name:
                continue

            print(f"Enabling {program_name} on {rpi}")
            os.system(f"ssh {rpi} 'cd /home/pi/wcl/{program_name} && source setup'")

        print(f"Finished processing {rpi}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_rpi, rpi_list)


if __name__ == "__main__":
    main()
