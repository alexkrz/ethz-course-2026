"""
Hyperparameters for Exercise 2 (DQN).

You are encouraged to tune:
- lr
- epsilon
- target_update
- hidden_dim

Please keep the remaining parameters unchanged unless explicitly stated.
"""

DQN_PARAMETERS = {
    # NOTE: Tune the following hyperparameters
    # Replace the default values with your own choices.
    "lr": 3e-4,            # NOTE
    "epsilon": 0.10,       # NOTE
    "target_update": 100,   # NOTE
    "hidden_dim": 128,     # NOTE
    
    # Fixed parameters
    "gamma": 0.99,
    "num_episodes": 500,
    "buffer_size": 10000,
    "minimal_size": 500,
    "batch_size": 64,
    "seed": 0,
}