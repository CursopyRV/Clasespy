# from datetime import datetime, timedelta

# ahora = datetime.now()
# print(f"Ahora: {ahora}")
# print(f"Mañana: {ahora + timedelta(days=1)}")

# import random

# print(random.randint(1,100))
# print(random.choice(["piedra", "papel", "tijera"]))

# import math

# print(math.sqrt(16))
# print(math.pi)

# import os

# print("Archivos: ", os.listdir())

# from collections import Counter

# frutas = ["Manzana", "Banana", "Manzana"]
# print(Counter(frutas))

# import json

# persona = {'nombre' : "Juan", "edad" : 30}
# print(persona)
# json_str = json.dumps(persona)
# print(json_str)

# import re

# texto = "Mi email es example@example.com"
# print(re.findall(r'\S+@\S+', texto))

# import pandas as pd

# data = {
#     "nombre": ["juan", "jose", "ana"],
#     "edad": [30, 25, 35]
# }

# df = pd.DataFrame(data)

# print(df)

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
USUARIO = os.getenv("USUARIO")
PASSWORD = os.getenv("PASSWORD")

print(f"API_KEY : {API_KEY}\nUSUARIO: {USUARIO}\nPASSWORD:{PASSWORD}")