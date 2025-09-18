import os
import sys


def main():
    print("Updating programs on Raspberry Pi devices...")

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

        for program in program_list:
            program = program.strip()
            if not program:
                continue

            # 해당 라즈베리파이에서 서비스 동작 중지
            os.system(f"ssh {rpi} 'sudo systemctl stop {program}'")
            print(f"Copying {program} on {rpi}")
            os.system(
                f"rsync -a --exclude='.git' {data_dir}/{program} {rpi}:/home/pi/wcl/"
            )
            # 해당 라즈베리파이에서 서비스 재시작
            os.system(f"ssh {rpi} 'sudo systemctl start {program}'")

        print(f"Finished processing {rpi}")


if __name__ == "__main__":
    main()
