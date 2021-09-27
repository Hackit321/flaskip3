import os
from dotenv import load_dotenv
load_dotenv()

class Config:


class ProdConfig(Config):



class DevConfig(Config):



config_options = {
    'development':DevConfig,
    'production':ProdConfig
}