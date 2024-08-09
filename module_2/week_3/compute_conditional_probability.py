import numpy as np
from create_train_dataset import create_train_data


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

        for j in range(len(y_unique)):
            for k in range(len(x_unique)):
                count_x_and_y = np.sum((train_data[:, i] == x_unique[k]) & (train_data[:, -1] == y_unique[j]))
                count_y = np.sum(train_data[:, -1] == y_unique[j])
                x_conditional_probability[j, k] = count_x_and_y / count_y if count_y > 0 else 0

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


if __name__ == "__main__":
    train_data = create_train_data()
    _, list_x_name = compute_conditional_probability(train_data)
    print("Feature names: ")
    print("x1 = ", list_x_name[0])
    print("x2 = ", list_x_name[1])
    print("x3 = ", list_x_name[2])
    print("x4 = ", list_x_name[3])
    print()
