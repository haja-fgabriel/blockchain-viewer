import os
from config import ConfigurationSet, config_from_dotenv, config_from_env, config_from_yaml

from cosmos_client import ROOT_PATH


def config():
    env = os.getenv("COSMOS_CLIENT_ENV", "local")
    return ConfigurationSet(
        config_from_env(prefix="COSMOS_CLIENT"),
        config_from_yaml(f"{ROOT_PATH}/src/cosmos_client/config/{env}.yml"),
    )
