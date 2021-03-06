import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import BernoulliNB
from evaluate_model import evaluate_model

dataset = sys.argv[1]
num_param_combinations = int(sys.argv[2])
random_seed = int(sys.argv[3])

np.random.seed(random_seed)

pipeline_components = [MinMaxScaler, BernoulliNB]
pipeline_parameters = {}

alpha_values = np.random.uniform(low=0., high=50., size=num_param_combinations)
fit_prior_values = np.random.choice([True, False], size=num_param_combinations)
binarize_values = np.random.uniform(low=0., high=1., size=num_param_combinations)

all_param_combinations = zip(alpha_values, fit_prior_values, binarize_values)
pipeline_parameters[BernoulliNB] = [{'alpha': alpha, 'fit_prior': fit_prior, 'binarize': binarize}
                                    for (alpha, fit_prior, binarize) in all_param_combinations]

evaluate_model(dataset, pipeline_components, pipeline_parameters)
