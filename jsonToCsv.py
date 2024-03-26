import csv
import json

# 재귀 함수로 중첩된 JSON 구조를 탐색하고 키-값 쌍을 추출하는 함수는 동일하게 유지
def extract_key_value_pairs(dictionary, parent_key='', path_separator='.'):
    pairs = []
    for key, value in dictionary.items():
        new_key = f"{parent_key}{path_separator}{key}" if parent_key else key
        if isinstance(value, dict):
            pairs.extend(extract_key_value_pairs(value, new_key, path_separator))
        else:
            pairs.append((new_key, value))
    return pairs

# JSON 파일을 읽어서 처리하는 함수
def process_large_json(json_file_path, csv_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    key_value_pairs = extract_key_value_pairs(json_data)

    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])  # 컬럼 헤더
        for pair in key_value_pairs:
            writer.writerow(pair)

# JSON 파일의 경로 (이 부분을 사용자의 실제 JSON 파일 경로로 수정)
large_json_file_path = '/Users/mac/Documents/workspace/jsonToCsv/en_old.json'
csv_output_path = '/Users/mac/Documents/workspace/jsonToCsv/en_ohmyappAdmin_old_csv.csv'

# JSON 파일 처리 및 CSV로 저장
process_large_json(large_json_file_path, csv_output_path)

csv_output_path
