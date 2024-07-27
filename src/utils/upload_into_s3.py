import boto3
from botocore.exceptions import NoCredentialsError

def upload_files_into_s3(file_name:str,
                         json_data:str,
                         bucket_file_path:str,
                         aws_access_key_id:str,
                         aws_secret_access_key:str,
                         region_name:str,
                         bucket_name:str) -> None:
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=bucket_file_path + "/" + file_name,
            Body=json_data,
            ContentType="application/json",
        )
        print(f"Dados enviados diretamente para o bucket {bucket_name} como {file_name}")
    except NoCredentialsError:
        print("Credenciais não disponíveis")
