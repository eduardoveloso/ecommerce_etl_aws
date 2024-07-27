from dotenv import load_dotenv
import os
from utils.upload_into_s3 import upload_files_into_s3
from utils.fake_generator import (
    generate_customers,
    generate_products,
    generate_order_items,
)
import json
import pytz
import datetime

load_dotenv()
AWS_ACCESS_KEY_ID=os.environ['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['SECRET_ACCESS_KEY']
AWS_REGION_NAME='us-east-1'
AWS_BUCKET_NAME='edus3bucket'
BUCKET_FOLDER_NAME='ecommerce_files'

timezone_br = pytz.timezone("America/Sao_Paulo")
date_br = datetime.datetime.now(timezone_br)
unix_timestamp = int(date_br.timestamp())

# Generate curstomers data
custormers_generated = generate_customers(100)
json_data = json.dumps(custormers_generated, ensure_ascii=False, indent=4).encode("utf-8")
custormers_filename = f"customers_{unix_timestamp}.json"

upload_files_into_s3(
    file_name=custormers_filename,
    json_data=json_data,
    bucket_file_path=BUCKET_FOLDER_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME,
    bucket_name=AWS_BUCKET_NAME,
)

# Generate Products data
