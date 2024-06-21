import os

# Define the project structure
project_structure = {
    'src': ['__init__.py', 'chat_interface.py', 'task_extraction.py', 'task_management.py', 'notifications.py', 'app.py'],
    'models': ['gpt_neo_model.py', 'config.json'],
    'data': ['sample_chats/', 'processed_data/'],
    'scripts': ['preprocess_data.py', 'train_model.py'],
    'config': ['settings.py', 'logging.conf'],
    'logs': ['app.log'],
    'tests': ['test_chat_interface.py', 'test_task_extraction.py', 'test_task_management.py'],
    'docs': ['README.md', 'project_plan.md']
}

# Create the project structure
def create_project_structure(base_path):
    for folder, files in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if file.endswith('/'):
                os.makedirs(file_path, exist_ok=True)
            else:
                open(file_path, 'a').close()

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    create_project_structure(base_path)
    print("Project structure created successfully.")
