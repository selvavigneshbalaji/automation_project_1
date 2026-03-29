import os
import yaml
from pathlib import Path



class ConfigManager:
    _instance = None
    _config={}


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._initialized=False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._load_config()
            self._initialized=True

    @staticmethod
    def _load_config():
        env = os.getenv('ENVIRONMENT', 'dev').lower()
        config_path = Path(__file__).parent / 'config.yaml'

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, 'r') as f:
            all_config = yaml.safe_load(f)

        if env not in all_config.get('environments', {}):
            raise ValueError(f"Environment '{env}' not found in config file")

        ConfigManager._config = all_config['environments'][env]
        ConfigManager._config['env'] = env
        ConfigManager._config['all_config'] = all_config

    def get(self, key, default = None):

        return self._config.get(key, default)

    def get_env_config(self) :
        return self._config.copy()
    @property
    def base_url(self):
        return self.get('base_url')

    @property
    def get_browser(self):
        return self.get('browser')
    @property
    def logging_config(self) :

        all_config = self.get('all_config', {})
        return all_config.get('logging', {})



config = ConfigManager()

if __name__ == "__main__":
    # Test configuration loading
    cfg = ConfigManager()

    print(f"Base URL: {cfg.base_url}")
