Model Card

Summary (For Non-Technical Readers)

This model predicts whether someone earns more than $50K per year based on U.S. Census data. It looks at things like work type, education, marital status, and other demographic information. The model is for educational and research purposes only and should not be used for real-world decisions like hiring or lending, because it may reflect biases present in the data.

Model Details

This model is a Random Forest Classifier trained to predict whether an individual earns more than $50K per year based on U.S. Census data. The model uses both categorical and continuous features, including workclass, education, marital status, occupation, relationship, race, sex, and native country.

Intended Use

The model is intended for educational and research purposes to explore classification techniques on census data. It should not be used for real-world decision-making such as employment, lending, or other high-stakes scenarios without further evaluation, validation, and bias mitigation.

Training Data

The training data comes from the U.S. Census Bureau dataset (census.csv). It contains demographic and employment-related information for individuals. The categorical features were encoded using one-hot encoding, and the label was binarized to indicate whether the income is >50K or <=50K.

Evaluation Data

The evaluation data was taken from a test split of the census dataset. Performance metrics were computed on this set, as well as on slices of the data for each unique value of the categorical features to analyze model behavior across different groups.

Metrics

The model was evaluated using precision, recall, and F1-score.
Overall performance on the test set:

Precision: 0.742

Recall: 0.638

F1-score: 0.686

Performance was also measured on slices of categorical features. For example:

Workclass = Private (4,595 samples): Precision 0.738 | Recall 0.625 | F1 0.677

Workclass = Self-emp-inc (201 samples): Precision 0.750 | Recall 0.818 | F1 0.783

Education = Bachelors (1,500 samples): Precision 0.710 | Recall 0.680 | F1 0.695

These metrics show the model performs reasonably well across most categories but may vary for smaller groups due to limited data.

Ethical Considerations

This model was trained on historical census data and may reflect societal biases present in that data. There is a risk that the model could reproduce or amplify biases based on race, sex, or other protected attributes if applied in real-world decision-making. Use with caution, and consider fairness and bias mitigation techniques if deploying in production environments.

Caveats and Recommendations

The model is not suitable for high-stakes decisions.

Performance may vary significantly on populations or features not well represented in the training data.

Always evaluate fairness across sensitive attributes before using the model operationally.

Consider additional preprocessing, feature selection, and model tuning for improved performance.
