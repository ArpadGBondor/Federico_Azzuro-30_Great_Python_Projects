from model import Prediction

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def make_prediction(
    inputs: list[float], outputs: list[float], input_value: float, plot: bool = False
) -> Prediction:
    if len(inputs) != len(outputs):
        raise ValueError('Length of "inputs" and "outputs" must match.')

    # Create a dataframe for our data
    df = pd.DataFrame({"inputs": inputs, "outputs": outputs})

    # Reshape the data using Numpy (X: inputs, y: outputs)
    X = np.array(df["inputs"]).reshape(-1, 1)  # [1, 2, 3]     => [[1],  [2],  [3]]
    y = np.array(df["outputs"]).reshape(-1, 1)  # [12, 23, 34]  => [[12], [23], [34]]

    # Split the data into training data to test our model
    train_X, test_X, train_y, test_y = train_test_split(
        X,
        y,
        random_state=0,  # fixed seed so the split is reproducible
        test_size=0.2,  # use 20% of the data for testing and 80% for training the model.
    )

    # X: [[1],  [2],  [3]]  =>
    #       split 80% to train: [[1],  [2]]
    #       and 20% to test: [[3]]
    # y: [[12], [23], [34]] =>
    #       split 80% to train: [[12], [23]]
    #       and 20% to test: [[34]]

    # Initialise the model and test it
    model = (
        LinearRegression()
    )  # Linear Regression tries to place data on a line f(x)=ax+b
    model.fit(train_X, train_y)

    # Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # Plot
    if plot:
        # raise NotImplementedError("Plot function has not been created yet")
        display_plot(inputs=X, outputs=y, y_line=y_line)

    return Prediction(
        value=y_prediction[0][0],  # <-- Prediction based on [[input_value]]
        r2_score=r2_score(
            test_y, y_test_prediction
        ),  # <-- How good the data fits the Linear Regression model f(x)=ax+b
        # <-- e.g.: if outputs are [60,110,160] then the generated line will be f(x)=50x+10
        slope=model.coef_[0][0],  # slope is a=50 (f(x)=ax+b)
        intercept=model.intercept_[0],  # intercept is b=10 (f(x)=ax+b)
        # (y axis is intercepted at f(0)=0*x+10=10)
        mean_absolute_error=mean_absolute_error(
            test_y, y_test_prediction
        ),  # <-- On average, predictions are off by about X units
    )


def display_plot(inputs: np.ndarray, outputs: np.ndarray, y_line: np.ndarray):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel("Inputs")
    plt.ylabel("Outputs")
    order = np.argsort(inputs[:, 0])
    plt.plot(inputs[order], y_line[order], color="r")
    plt.show()


def main():
    years: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    earnings: list[int] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]
    my_input: int = 20
    pred = make_prediction(years, earnings, my_input, plot=True)
    print(f"Input: {my_input}")
    print(pred)

    # Additional predictions can be made: (f(x)=ax+b)
    print(f"Year 30: {(pred.slope * 30 + pred.intercept):.2f}")
    print(f"Year 40: {(pred.slope * 40 + pred.intercept):.2f}")
    print(f"Year 50: {(pred.slope * 50 + pred.intercept):.2f}")


if __name__ == "__main__":
    main()
