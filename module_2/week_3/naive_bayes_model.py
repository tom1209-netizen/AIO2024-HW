from train_naive_bayes import train_naive_bayes, prediction_play_tennis
from create_train_dataset import create_train_data


if __name__ == "__main__":
    train_data = create_train_data()
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)

    X = ['Sunny', 'Cool', 'High', 'Strong']
    y_pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

    if y_pred:
        print("Ad should go")
    else:
        print("Ad should not go")
    print()