import numpy as np
from create_train_dataset import create_train_data
from compute_conditional_probability import compute_conditional_probability


def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]


if __name__ == "__main__":
    train_data = create_train_data()
    _, list_x_name = compute_conditional_probability(train_data)
    outlook = list_x_name[0]

    print("Index of Outlook:")
    i1 = get_index_from_value('Overcast', outlook)
    i2 = get_index_from_value('Rain', outlook)
    i3 = get_index_from_value('Sunny', outlook)
    print(i1, i2, i3)
    print()
