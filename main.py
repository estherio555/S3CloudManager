
#################################################
# Created: Esther Ezekiel

from s3manager.s3_operations import *

from s3manager.s3_operations import download_file

create_bucket("esther2026")

upload_file("/Users/john_eze4u/Downloads/Loss.png", "esther2024")

delete_bucket("Esther2026")

upload_file(file_path="Loss.png", bucket_name="esther2026", object_name="projects/dev/esther2026.png")

