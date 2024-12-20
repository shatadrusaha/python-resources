''' Resources:

https://towardsdatascience.com/one-hot-encoding-scikit-vs-pandas-2133775567b8
https://scikit-learn.org/stable/api/sklearn.compose.html
https://scikit-learn.org/stable/api/sklearn.preprocessing.html

'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

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
# The column transformer does not create the pandas DataFrame, but it selects the appropriate columns, converts them and appends the converted columns to the other ones.
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
