import os
from datetime import datetime

PDF_STOTRAGE = os.path.join("storage", "pdfs")

class FileManager:

    def save_file(self, uploaded_file):
        # Generate Unique Filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{uploaded_file.name}"
        file_path = os.path.join(PDF_STOTRAGE, filename)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        return file_path