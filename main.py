from src.simulation import generate_data
from src.model import train_model
from src.detection import hybrid_detection

import pandas as pd

# Data generate
normal = generate_data(500, False)
attack = generate_data(200, True)
df = pd.concat([normal, attack])

# Train model
model = train_model(df)

# Test
sample = [50, 0.5, 0.2]
result = hybrid_detection(model, sample)

print("Result:", result)
