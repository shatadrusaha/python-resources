''' Resources:

https://scikit-learn.org/stable/api/sklearn.compose.html
https://scikit-learn.org/stable/api/sklearn.preprocessing.html

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html

https://towardsdatascience.com/one-hot-encoding-scikit-vs-pandas-2133775567b8
https://harshal-soni.medium.com/onehotencoding-vs-labelencoder-vs-pandas-get-dummies-how-and-why-b190dff7a86f


'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
# from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin

# It is always good to have an explicit list of categories
categories = [('Type', ['Cat', 'Dog', 'Parrot', 'Whale']), ('Color', ['Brown', 'Black', 'Mixed'])]

# Let's create some mock data
X_train = pd.DataFrame(columns=['Type','Color','Age'],
                       data=[['Cat','Brown',4.2],['Dog','Brown',3.2],['Parrot','Mixed',21]])
X_input = pd.DataFrame(columns=['Type','Color','Age'],
                         data = [['Parrot', 'Black', 32]])

display(X_train, X_input)

ohe_columns = [x[0] for x in categories]
ohe_categories = [x[1] for x in categories]
enc = OneHotEncoder(sparse_output=False, categories=ohe_categories)

# We create a column transformer telling it to replace the columns which hold the categories and leave the rest untouched.
# The column transformer does not crea`te the pandas DataFrame, but it selects the appropriate columns, converts them and appends the converted columns to the other ones.
transformer = make_column_transformer((enc, ohe_columns), remainder='passthrough')

# We convert the resulting arrays to DataFrames
transformed=transformer.fit_transform(X_train)
display(pd.DataFrame(
    transformed, 
    columns=transformer.get_feature_names_out(),
    index=X_train.index
))
pd.DataFrame(
    transformer.transform(X_input),
    columns=transformer.get_feature_names_out(),
    index=X_input.index
)

transformed_df = pd.DataFrame(
    enc.fit_transform(X_train[ohe_columns]),
    columns = enc.get_feature_names_out(),
    index = X_train.index)
display(transformed_df)
transformed_df = pd.concat([X_train.drop(ohe_columns,axis=1),transformed_df],axis=1)
display(transformed_df)

T_input = pd.DataFrame(
    enc.transform(X_input[ohe_columns]),
    columns = enc.get_feature_names_out(),
    index = X_input.index)
T_input = pd.concat([X_input.drop(ohe_columns,axis=1),T_input],axis=1)
T_input

X_train[ohe_columns] = X_train[ohe_columns].astype('category')
X_input[ohe_columns] = X_input[ohe_columns].astype('category')
for column_name, l in categories:
    X_train[column_name] = X_train[column_name].cat.set_categories(l)
    X_input[column_name] = X_input[column_name].cat.set_categories(l)

display(pd.get_dummies(X_train))
display(pd.get_dummies(X_input))

pd.get_dummies(X_train, columns=ohe_columns[:1])


class GetDummiesTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, *args, pandas_params={}, **kwargs):
        super().__init__(*args, **kwargs)
        self._pandas_params = pandas_params
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return pd.get_dummies(X, **self._pandas_params)

GetDummiesTransformer(pandas_params={'columns':['Type']}).transform(X_train)
