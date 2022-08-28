Usage
=====

.. _installation:
    :noindex:

Example Usage
-------------

.. code-block:: console
    
    import sys
    utils_path = '/path_to/ja-utils'
    import ja-utils

    # reload this module in Jupyter notebook
    %load_ext autoreload
    %autoreload 2


>>> import sys
>>> utils_path = '/path_to/ja-utils'
>>> sys.path.append(utils_path)
>>> import ja-utils