import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path, replace=False):
        res = requests.get(f'{URL}/upload?path={file_path}&overwrite={replace}', headers=headers).json()

if __name__ == '__main__':
    file_path = 'C:\myfiles\com.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(file_path=file_path)