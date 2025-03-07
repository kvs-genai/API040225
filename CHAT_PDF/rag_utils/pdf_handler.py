import os

def handle_pdf_upload(uploaded_files, save_folder):
    """
    Handles the saving of uploaded files
    """
    saved_files = []
    for uploaded_file in uploaded_files:
        save_path = os.path.join(save_folder, uploaded_file.name)
        with open(save_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        saved_files.append(save_path)
    return saved_files