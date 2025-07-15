import pandas as pd
import requests

def process_file(input_path="input.xlsx", output_path="ket_qua_uid.xlsx"):
    df = pd.read_excel(input_path, header=None)
    df.columns = ['Facebook Link']

    uids = []
    for link in df['Facebook Link']:
        try:
            response = requests.get(f'https://alolike.vn/api/v1/tools/get-uidv2?link={link}')
            data = response.json()
            uid = data['layid'] if data.get('status') == 'success' and data.get('layid') else None
            uids.append(uid)
        except:
            uids.append(None)

    df['UID'] = uids
    df_valid = df[df['UID'].notnull()]
    df_valid.to_excel(output_path, index=False)
    print(f"✅ Xuất kết quả: {output_path}")

# Chạy khi service khởi động
process_file()
