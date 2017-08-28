import numpy as np


def log_loss(y_true, y_pred, epsilon=10e-7):
    """ Compute log-loss. """
    return -np.mean(y_true * np.log(y_pred  + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))


def mse(y_true, y_pred):
    """ Compute MSE metric.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    """
    return np.mean((y_pred - y_true) ** 2)


def rmse(y_true, y_pred):
    """ Compute RMSE metric.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    """
    return np.sqrt(np.mean(y_pred - y_true) ** 2)


def mae(y_true, y_pred):
    """ Compute MAE metric.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    """
    return np.mean(np.abs(y_pred - y_true))


def dice(y_true, y_pred, epsilon=10e-7):
    """ Compute Dice coefficient.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    """
    return 2 * np.sum(y_pred * y_true) / (np.sum(y_pred) + np.sum(y_true) + epsilon)


def sym_dice(y_true, y_pred, alpha, epsilon=10e-7):
    """ Symmetric dice coefficient.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    """
    return (1 - alpha) * dice(y_pred, y_true, epsilon) + alpha * dice(1 - y_pred, 1 - y_true, epsilon)


def tp(y_true, y_pred, threshold=0.5):
    """ Get number of True Positive values.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;

    Returns:
    - float, number of true positive predictions;
    """
    return float(np.sum(np.asarray(y_pred > threshold, dtype=np.int) * y_true))


def fp(y_true, y_pred, threshold=0.5):
    """ Get number of False Positive values.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;

    Returns:
    - float, number of false positive predictions;
    """
    return float(np.sum(np.asarray(y_pred > threshold, dtype=np.int) * (1. - y_true)))


def tn(y_true, y_pred, threshold=0.5):
    """ Get number of True Negative values.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;

    Returns:
    - float, number of true negative predictions;
    """
    return float(np.sum(np.asarray(y_pred <= threshold, dtype=np.int) * (1. - y_true)))


def fn(y_true, y_pred, threshold=0.5):
    """ Get number of False Negative values.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;

    Returns:
    - float, number of false negative predictions;
    """
    return float(np.sum(np.asarray(y_pred <= threshold, dtype=np.int) * y_true))


def tpr(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ True positive rate.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, tpr metric value;
    """
    tp_value = tp(y_pred, y_true, threshold)
    fn_value = fn(y_pred, y_true, threshold)
    return tp_value / (tp_value + fn_value + epsilon)


def tnr(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ True negative rate.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, tnr metric value;
    """
    tn_value = tn(y_pred, y_true, threshold)
    fp_value = fp(y_pred, y_true, threshold)
    return tn_value / (tn_value + fp_value + epsilon)


def fpr(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ False positive rate.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, fpr metric value;
    """
    return 1. - tpr(y_pred, y_true, threshold, epsilon)


def fnr(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ False negative rate.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, fnr metric value;
    """
    return 1. - tnr(y_pred, y_true, threshold, epsilon)


def precision(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ Compute precision metric.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, precision metric value;
    """
    tp_value = tp(y_pred, y_true, threshold)
    fp_value = fp(y_pred, y_true, threshold)
    return tp_value / (tp_value + fp_value + epsilon)

def recall(y_true, y_pred, threshold=0.5, epsilon=10e-7):
    """ Compute recall metric.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;
    - epsilon: small float for avoiding division by zero error;

    Returns:
    - float, recall metric value;
    """
    return tpr(y_pred, y_true, threshold=threshold, epsilon=epsilon)

def accuracy(y_true, y_pred, threshold=0.5):
    """ Compute accuracy on input batched y_pred and y_true.

    Args:
    - y_pred: np.ndarray(batch_size, ...)
    numpy array containing predictions of model;
    - y_true: np.ndarray(batch_size, ...)
    numpy array containing true target values;
    - threshold: float, threshold for mapping probabilities into class;

    Returns:
    - float, accuracy metric value;
    """
    result = np.mean(np.abs(np.asarray(y_pred > threshold, dtype=np.int) - y_true))
    return 1. - result


ALL_METRICS = {'mse': mse,
               'rmse': rmse,
               'mae': mae,
               'dice': dice,
               'sym_dice': sym_dice,
               'tpr': tpr,
               'fpr': fpr,
               'tnr': tnr,
               'fnr': fnr,
               'precision': precision,
               'recall': recall,
               'accuracy': accuracy,
               'log_loss': log_loss}
