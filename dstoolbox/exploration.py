import pandas as pd
import numpy as np
import spacy
from sklearn.metrics.pairwise import cosine_similarity


def placeholder_and_null_summary(df, placeholder):
  """
  Identifies placeholder and null values in a dataframe.

  Parameters:
    df (DataFrame): This should be a pandas DataFrame.
    placeholder (str or int): Placeholder value which is constant across multiple columns.

  Returns:
    dict: Dictionary containing the number of placeholders and number of missing values respectively, in the column.
  """
  col_dict = {}
  for col in df.columns:
    null_count = df[col].isnull().sum()
    if isinstance(placeholder, str):
      placeholder_count = df[df[col].astype(str).isin([str(placeholder)])].shape[0]
    else:
      placeholder_count = df[df[col].astype(str).isin([str(placeholder)])].shape[0]
    col_dict[col] = [placeholder_count, null_count]
  return col_dict


def categoric_summary(df):
  """
    Generates a summary of categorical columns in the provided dataframe.

    Parameters:
      df (pandas.DataFrame): The input dataframe containing categorical columns.

    Returns:
      pandas.DataFrame: A dataframe with summary statistics for each categorical column.

    Examples:
      >>> data = pd.DataFrame({'Category': ['A', 'B', 'A', 'B', 'C'],
      ...                      'Status': ['Active', 'Inactive', 'Active', 'Active', 'Inactive']})
      >>> summary = categoric_summary(data)
      >>> print(summary)
                unique_values suggested_encoding  missing_values top_value
      Category              3            One-Hot               0         A
      Status                2             Binary               0    Active
    """

  nlp = spacy.load('en_core_web_sm')
  
  categorical_cols = df.select_dtypes(include='object').columns
  summary = pd.DataFrame(index=categorical_cols)
  summary['unique_values'] = df[categorical_cols].nunique()
  
  for col in categorical_cols:
    unique_values = df[col].nunique()
    if unique_values == 2:
      summary.loc[col, 'suggested_encoding'] = 'Binary'
    else:
      # Convert column values to strings
      values = df[col].astype(str)
      
      # Calculate cosine similarity between values
      embeddings = [nlp(value).vector for value in values.unique()]
      similarity_matrix = cosine_similarity(embeddings)
      similarity_score = similarity_matrix.mean()
      
      if similarity_score >= 0.7:
        summary.loc[col, 'suggested_encoding'] = 'Ordinal'
      else:
        summary.loc[col, 'suggested_encoding'] = 'One-Hot'
          
          
  summary['missing_values'] = df[categorical_cols].isnull().sum()
  value_counts = {}
  for column in categorical_cols:
    value_counts[column] = df[column].value_counts()
  
  summary['top_value'] = [value_counts[column].idxmax() for column in categorical_cols]
  
  return summary