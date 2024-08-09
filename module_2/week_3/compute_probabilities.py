from create_train_dataset import create_train_data
from compute_conditional_probability import compute_conditional_probability
from get_index_from_value import get_index_from_value
import numpy as np


train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)

# Compute P("Outlook"="Sunny"|Play Tennis="Yes")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P(‘Outlook’=’Sunny’|Play Tennis=’Yes’) = ", np.round(conditional_probability[0][1, x1], 2))

# Compute P("Outlook"="Sunny"|Play Tennis="No")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P(‘Outlook’=’Sunny’|Play Tennis=’No’) = ", np.round(conditional_probability[0][0, x1], 2))