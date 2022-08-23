from pydantic import BaseSettings


class Settings(BaseSettings):
    S3_ACCESS_KEY: str
    S3_SECRET_ACCESS_KEY: str
    
    class Config:
        env_file = ".env"
