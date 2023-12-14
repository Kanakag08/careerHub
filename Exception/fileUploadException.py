class FileUploadException(Exception):
    pass

    def upload_cover_letter(Resume):
        try:
        # Check if the file exists
            with open(Resume,'rb') as file:
            # Check if the file size exceeds a certain limit (e.g., 5 MB)
                max_file_size = 5 * 1024 * 1024  # 5 MB
                if len(file.read()) > max_file_size:
                    raise FileUploadException("File size exceeds the allowed limit.")

            # Check if the file format is supported (you can add more supported formats)
                supported_formats = ['.pdf', '.doc', '.docx', '.txt']
                if not any(Resume.lower().endswith(format) for format in supported_formats):
                    raise FileUploadException("Unsupported file format.")

            print("File uploaded successfully.")

        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except FileUploadException as e:
            print(f"File upload error: {e}")
        except Exception as ex:
            print(f"Unexpected error:{ex}")