import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    # 一つ上の階層にある .env を指定
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent / ".env"),
        env_file_encoding="utf-8",
    )

    # === API Keys ===
    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str = ""
    TAVILY_API_KEY: str = ""
    COHERE_API_KEY: str = ""

    # === LangSmith Configuration ===
    LANGSMITH_TRACING: str = "false"
    LANGSMITH_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = "default"

    # === for Application ===
    openai_smart_model: str = "gpt-4o"
    openai_embedding_model: str = "text-embedding-3-small"
    anthropic_smart_model: str = "claude-3-5-sonnet-20240620"
    temperature: float = 0.0
    default_reflection_db_path: str = "tmp/reflection_db.json"

    def __init__(self, **values):
        super().__init__(**values)
        self._set_env_variables()

    def _set_env_variables(self):
        for key in self.__annotations__.keys():
            if key.isupper():
                os.environ[key] = str(getattr(self, key))
