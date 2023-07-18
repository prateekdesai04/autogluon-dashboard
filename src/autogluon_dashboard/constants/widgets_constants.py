from autogluon_dashboard.constants.df_constants import (
    BESTDIFF,
    LOSS_RESCALED,
    TIME_INFER_S_RESCALED,
    TIME_TRAIN_S_RESCALED,
)

METRICS_TO_PLOT = [
    LOSS_RESCALED,
    TIME_TRAIN_S_RESCALED,
    TIME_INFER_S_RESCALED,
    BESTDIFF,
]
GRAPH_TYPES = ["bar", "line", "hist", "scatter"]