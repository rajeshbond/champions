from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  sheet_id : str
  google_cloud_champion: dict

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"

# settings = Setting() 
