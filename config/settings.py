from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    ai_enabled: int = Field(default=1, env="AI_ENABLED")
    ai_provider: str = Field(default="stub", env="AI_PROVIDER")  # stub | openai
    ai_model: str = Field(default="gpt-4o-mini", env="AI_MODEL")
    ai_max_tokens: int = Field(default=512, env="AI_MAX_TOKENS")
    ai_timeout_sec: int = Field(default=20, env="AI_TIMEOUT_SEC")

    pay_port: int = Field(default=8081, env="PAY_PORT")
    mail_port: int = Field(default=8082, env="MAIL_PORT")

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
