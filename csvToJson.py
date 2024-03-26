import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # CSV 파일을 읽어 들임
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # JSON으로 변환
    json_data = {}
    for item in data:
        keys = item['Key'].split('.')
        current_level = json_data
        for key in keys[:-1]:
            if key not in current_level:
                current_level[key] = {}
            current_level = current_level[key]
        current_level[keys[-1]] = item['Value']

    # JSON 파일로 저장
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

# CSV 파일 경로 (이전에 생성된 CSV 파일 경로)
csv_file_path = '/Users/mac/Documents/workspace/jsonToCsv/new.csv'

# JSON 파일 경로
json_output_path = '/Users/mac/Documents/workspace/jsonToCsv/en-new.json'

# CSV를 JSON으로 변환
csv_to_json(csv_file_path, json_output_path)

json_output_path