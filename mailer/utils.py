import pandas as pd
import logging
from typing import List, Dict, Any

def load_template(file_path: str) -> str:
    """
    Read a template file (HTML or Text) and return its content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logging.error(f"Error loading template file {file_path}: {e}")
        return ""

def load_from_excel(file_path: str, sheet_name: str = 0) -> List[Dict[str, Any]]:
    """
    Load recipient data from an Excel file.
    Expects columns like 'Name', 'Email', etc.
    Returns a list of dictionaries.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Convert all column names to lowercase for easier template matching
        df.columns = [col.lower() for col in df.columns]
        
        if 'email' not in df.columns:
            raise ValueError(f"The file {file_path} must contain an 'Email' column.")
            
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error(f"Error loading Excel file: {e}")
        return []

def load_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Load recipient data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        df.columns = [col.lower() for col in df.columns]
        
        if 'email' not in df.columns:
            raise ValueError(f"The file {file_path} must contain an 'Email' column.")
            
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        return []
