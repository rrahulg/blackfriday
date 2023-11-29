import re
import numpy as np
import pandas as pd

class ExtractNumeric:
    """A class for extracting numeric values from a pandas DataFrame.

    This class provides methods to fit and transform a DataFrame by extracting
    numeric values from each element of the DataFrame.

    Parameters:
    None

    Methods:
    - fit(x): Save a copy of the input DataFrame.
    - transform(x): Extract numeric values from each element of the DataFrame.
    - fit_transform(x): Equivalent to calling fit(x) followed by transform(x).

    Example:
    ```python
    # Instantiate the ExtractNumeric class
    extractor = ExtractNumeric()

    # Fit the extractor on a DataFrame
    extractor.fit(df)

    # Transform the DataFrame to extract numeric values
    numeric_df = extractor.transform(df)
    ```

    Note: This class assumes the input DataFrame is a pandas DataFrame.
    """

    def __init__(self):
        pass

    def fit(self, x):
        """Fit the ExtractNumeric instance on a DataFrame.

        Parameters:
        - x (pandas.DataFrame): The input DataFrame to fit on.

        Returns:
        pandas.DataFrame: A copy of the input DataFrame.
        """
        self.x_op = x.copy()
        return self.x_op

    def transform(self, x):
        """Transform the DataFrame by extracting numeric values.

        Parameters:
        - x (pandas.DataFrame): The input DataFrame to transform.

        Returns:
        pandas.DataFrame: A DataFrame with numeric values extracted from each element.
        """
        self.x_op = x.copy()
        return self.x_op.apply(lambda x: ''.join(re.findall(r'\d', str(x)))).astype(int)

    def fit_transform(self, x):
        """Fit and transform the DataFrame in a single step.

        Parameters:
        - x (pandas.DataFrame): The input DataFrame to fit and transform.

        Returns:
        pandas.DataFrame: A DataFrame with numeric values extracted from each element.
        """
        return self.transform(x)




