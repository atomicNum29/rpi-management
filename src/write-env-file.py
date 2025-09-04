import os
import sys
import requests
import argparse
import csv


def extract_keywords(env_lines):
    keywords = []
    for line in env_lines:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key = line.split("=", 1)[0].strip()
            keywords.append(key)
    return keywords

def main():
    print("Writing environment file...")
    # Code to write the environment file goes here

    data_dir = os.path.dirname(os.path.abspath(__file__).replace("src", "data"))

    csv_path = os.path.join(data_dir, "list-of-rpis-env.csv")
    with open(csv_path, "r", encoding="utf-8") as f:
        csv_content = f.readlines()
    csv_reader = csv.DictReader(csv_content)
    csv_rows = [row for row in csv_reader]

    with open(f"{data_dir}/list-of-programs", "r") as file:
        program_list = file.readlines()

    # 각 행 별로 라즈베리파이 별 정보가 적혀있음
    for row in csv_rows:
        print(f"Processing Raspberry Pi: {row['raspberry pi']}")

        # 각 프로그램 별로 .env 파일 작성
        for program in program_list:
            program = program.strip()
            print(f" - {program}")
            env_example_path = os.path.join(data_dir, program, "env", ".env.example")
            if os.path.exists(env_example_path):
                with open(env_example_path, "r", encoding="utf-8") as env_file:
                    env_lines = env_file.readlines()
                keywords = extract_keywords(env_lines)
                print(f"   Keywords: {keywords}")
            else:
                print(f"   .env.example not found for {program}")

            if keywords:
                env_contents = "\n".join(
                    f"{key}={row[key]}" for key in keywords if key in row
                )
                print(f"   Writing .env with contents:\n{env_contents}\n")
                os.system(
                    f"ssh {row['raspberry pi']} 'mkdir -p /home/pi/wcl/{program}/env'"
                )
                os.system(
                    f"ssh {row['raspberry pi']} 'echo \"{env_contents}\" > /home/pi/wcl/{program}/env/.env'"
                )
            else:
                print(f"   No keywords found for {program}")

    print("Finished writing environment files.")

if __name__ == "__main__":
    main()
