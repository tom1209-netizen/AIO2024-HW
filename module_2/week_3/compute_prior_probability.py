import numpy as np
from create_train_dataset import create_train_data


def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    num_of_samples = train_data.shape[0]
    num_of_class_no = np.sum(train_data[:, -1] == 'no')
    num_of_class_yes = np.sum(train_data[:, -1] == 'yes')

    prior_probability[0] = num_of_class_no / num_of_samples
    prior_probability[1] = num_of_class_yes / num_of_samples

    return prior_probability


if __name__ == "__main__":
    train_data = create_train_data()
    prior_probability = compute_prior_probability(train_data)
    print("Prior Probability: ")
    print("P(play tennis = No)", prior_probability[0])
    print("P(play tennis = Yes)", prior_probability[1])
    print()
