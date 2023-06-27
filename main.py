__author__ = 'https://github.com/password123456/'
__version__ = '1.0.0-20230627'

import os
import sys
import boto3
import datetime
import requests
import json

class Bcolors:
    # 터미널 출력에 사용할 색상 코드를 정의하는 클래스
    Black = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Magenta = '\033[35m'
    Cyan = '\033[36m'
    White = '\033[37m'
    Endc = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def start():
    s3_bucket_name = f'##Your S3 Bucket##'
    s3_client = boto3.client('s3')

    try:
        # S3 연결 가능 여부 확인
        response = s3_client.head_bucket(Bucket=s3_bucket_name)
    except Exception as e:
        # S3 연결 실패 시 오류 메시지 출력 후 프로그램 종료
        print(f'{Bcolors.Red}- Failed to connect to the "security.system.log.backup" bucket. '
              f'Check your AWS credentials and configuration.{Bcolors.Endc}')
        print(f'{Bcolors.Red}- Error: {str(e)}{Bcolors.Endc}')
        sys.exit(1)

    find_target_files(s3_bucket_name)


def find_target_files(s3_bucket_name):
    # S3에서 파일 조회
    s3_client = boto3.client('s3')

    # get datetime 90 days before from current
    check_days = 90
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=check_days)
    cleanup_candidates = []
    count_condidates = 0

    # S3에서 파일 목록 조회
    response = s3_client.list_objects_v2(Bucket=s3_bucket_name)
    if 'Contents' in response:
        objects = response['Contents']
        for obj in objects:
            file_key = obj['Key']
            last_modified = obj['LastModified'].replace(tzinfo=None)
            if last_modified < cutoff_date:
                count_condidates += 1
                cleanup_candidates.append(file_key)

    if cleanup_candidates:
        # 대상 파일이 존재하는 경우 정리 함수 호출
        cleanup_files_in_s3(s3_bucket_name, cleanup_candidates, cutoff_date, check_days, count_condidates)
    else:
        # 대상 파일이 없는 경우 메시지 출력
        print(f'{Bcolors.Yellow}>> cleaning up {check_days} days ago{Bcolors.Endc}')
        print(f'{Bcolors.Yellow}>> No file to clean up{Bcolors.Endc}')
        message = f'*** s3_file_clean_up ***\n\n- {os.uname()[1]}\n- {datetime.datetime.now()}'
        message = f'{message}\n\n[+] run date: {datetime.datetime.now().strftime("%Y-%m-%d")}\n[+] cut off : {cutoff_date.strftime("%Y-%m-%d")}\n\n---> cleaning up {check_days} days ago\n\n[+] result\n---> No file to clean up'
        send_to_slack(message)


def cleanup_files_in_s3(s3_bucket_name, cleanup_candidates, cutoff_date, check_days, count_condidates):
    # S3에서 파일 삭제
    s3_client = boto3.client('s3')

    # 삭제 대상 파일과 삭제 결과를 저장할 리스트
    cleanup_success = []
    cleanup_failures = []
    i = 0
    n = 0

    # 파일 삭제
    if cleanup_candidates:
        for file_path in cleanup_candidates:
            try:
                i += 1
                # 파일 삭제
                s3_client.delete_object(Bucket=s3_bucket_name, Key=file_path)
                cleanup_success.append(f'{i}, [success], s3://{s3_bucket_name}/{file_path}')
            except Exception as e:
                n += 1
                # 삭제 실패한 파일을 저장
                cleanup_failures.append(f'{n}, [failure], s3://{s3_bucket_name}/{file_path} ({str(e)})')
    else:
        print(f'{Bcolors.Yellow}>> cleaning up {check_days} days ago{Bcolors.Endc}')
        print(f'{Bcolors.Yellow}>> No file to clean up{Bcolors.Endc}')
        sys.exit(0)

    # 삭제 결과 출력
    success_list = ''
    failure_list = ''

    if cleanup_success:
        for file in cleanup_success:
            success_list += f'\n{file}'

    if cleanup_failures:
        for file in cleanup_failures:
            failure_list += f'\n{file}'

    print(f'\n>> Clean Up Result')
    if success_list:
        print(f'{success_list}\n')
    if failure_list:
        print(f'{failure_list}\n')

    print(f'{Bcolors.Green}------------------------------------->{Bcolors.Endc}')

    # 삭제 결과를 Slack으로 전송
    message_header = f'*** s3_file_clean_up ***\n\n- {os.uname()[1]}\n- {datetime.datetime.now()}'
    message_body = f'[+] result\n---> clean up success: {i} files\n---> clean up failure: {n} files\n---> total files: {i+n} files\n\n{success_list}{failure_list}'

    message = f'{message_header}\n\n[+] run date: {datetime.datetime.now().strftime("%Y-%m-%d")}\n[+] cut off : {cutoff_date.strftime("%Y-%m-%d")}\n\n---> cleaning up {check_days} days ago\n---> scanned ({count_condidates}) files\n\n{message_body}'
    send_to_slack(message)


def send_to_slack(message):
    webhook_url = f'##Your SLACK_WEB_HOOKS##'
    header = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    }

    params = { 'text': message }

    try:
        # Slack 웹훅으로 메시지 전송
        r = requests.post(webhook_url, headers=header, data=json.dumps(params), verify=True)
        print(f'{Bcolors.Green}>> Send to Slack: {r.status_code} {r.text} { Bcolors.Endc}')
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}>> Exception: Func:[{send_to_slack.__name__}] Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
    else:
        r.close()


def main():
    banner = """
=======================================================
    [python] clean up old files in s3.
=======================================================
"""
    print(f'\n')
    print(f'{Bcolors.Cyan}{banner}{Bcolors.Endc}')

    start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f'{Bcolors.Yellow}- ::Exception:: Func:[{__name__.__name__}] '
              f'Line:[{sys.exc_info()[-1].tb_lineno}] [{type(e).__name__}] {e}{Bcolors.Endc}')
