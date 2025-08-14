import os
import sys
import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="지역 정보와 벌통 정보를 받아 .env 파일의 내용 생성"
    )
    parser.add_argument(
        "-H", "--hive",
        help="벌통 고유 이름(문자열)",
        required=True
    )
    parser.add_argument(
        "-R", "--region",
        help="지역 ID(정수) 또는 지역 이름(문자열)"
    )
    return parser.parse_args()

def main():
    print("Writing environment file...")
    # Code to write the environment file goes here

    args = parse_args()
    print(f"Received hive: {args.hive}, region: {args.region}")

    # 입력된 이름의 벌통이 존재하는지 확인
    response = requests.get(f"http://localhost:8000/hives/{args.hive}")

if __name__ == "__main__":
    main()