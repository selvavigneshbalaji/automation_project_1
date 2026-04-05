from src.utilities.loggers import get_logger
import json
import csv

logger= get_logger(__name__)
class FileReader:
    @staticmethod
    def read_json(file_path) :

        try:
            logger.info(f"Reading JSON file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"Successfully read JSON file with {len(data)} items")
            return data["valid_users"]
        except FileNotFoundError:
            logger.error(f"JSON file not found: {file_path}")
            raise "error"
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {file_path}")
            raise "error"
    @staticmethod
    def read_csv(file_path):

        try:
            logger.info(f"Reading CSV file: {file_path}")
            data = []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            logger.info(f"Successfully read CSV file with {len(data)} rows")
            return data
        except FileNotFoundError:
            logger.error(f"CSV file not found: {file_path}")
            raise "error"
        except Exception as e:
            logger.error(f"Error reading CSV file: {str(e)}")
            raise "error"
