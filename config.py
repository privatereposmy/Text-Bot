import os

class Config(object):

      BOT_TOKEN = os.environ.get("5302212624:AAFgg9qi_J4iKXxrFGfjx_RM3uq5Kb-s1k0", "")
      API_ID = int(os.environ.get("840611",))
      API_HASH = os.environ.get("5820bc24605e0ff60af5391d649f9a6")
      OWNER_ID = int(os.environ.get("167649219"))

