import os

def verify_project_structure():
    """Verify that all required files have been created."""
    required_files = [
        # Backend files
        "backend/database.py",
        "backend/models.py",
        "backend/scraper.py",
        "backend/llm_quiz_generator.py",
        "backend/main.py",
        "backend/requirements.txt",
        "backend/.env",
        "backend/test_api.py",
        
        # Frontend files
        "frontend/package.json",
        "frontend/index.html",
        "frontend/src/main.jsx",
        "frontend/src/App.jsx",
        "frontend/src/index.css",
        "frontend/src/services/api.js",
        "frontend/src/services/test.js",
        "frontend/src/components/QuizDisplay.jsx",
        "frontend/src/components/Modal.jsx",
        "frontend/src/tabs/GenerateQuizTab.jsx",
        "frontend/src/tabs/HistoryTab.jsx",
        "frontend/tailwind.config.js",
        "frontend/postcss.config.js",
        "frontend/vite.config.js",
        
        # Sample data
        "sample_data/sample_output.json",
        "sample_data/sample_urls.txt",
        
        # Documentation
        "README.md",
        "SETUP.md",
        "prompt_templates.md",
        "screenshots/README.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = os.path.join("c:\\Users\\91939\\Desktop\\AI Wiki Quiz", file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("Missing files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
        return False
    else:
        print("All required files are present!")
        return True

if __name__ == "__main__":
    verify_project_structure()