import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

from dagster.utils import script_relative_path

notebook_paths_to_test = [
    # '../../../python_modules/libraries/dagster-pandas/dagster_pandas/examples/pandas_hello_world/scratch.ipynb',
    '../../../python_modules/libraries/dagster-pandas/dagster_pandas/examples/notebooks/papermill_pandas_hello_world.ipynb',
    '../../../python_modules/dagit/dagit_tests/render_uuid_notebook.ipynb',
    # '../../../python_modules/dagstermill/dagstermill/examples/notebooks/error_notebook.ipynb',
    # '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world_config.ipynb',
    # '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world_output.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/tutorial_LR.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/tutorial_RF.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/clean_data.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/add_two_numbers.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/mult_two_numbers.ipynb',
    # '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world_resource_with_exception.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_logging.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world_explicit_yield.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/bad_kernel.ipynb',
    '../../../python_modules/dagstermill/dagstermill/examples/notebooks/hello_world_resource.ipynb',
    '../../../python_modules/dagstermill/dagstermill_tests/notebooks/retroactive.ipynb',
    '../../../docs/sections/learn/guides/data_science/iris-kmeans.ipynb',
    '../../../docs/sections/learn/guides/data_science/iris-kmeans_2.ipynb',
    '../../../docs/sections/learn/guides/data_science/iris-kmeans_3.ipynb',
    # '../../../examples/dagster_examples/airline_demo/notebooks/Delays_by_Geography.ipynb',
    # '../../../examples/dagster_examples/airline_demo/notebooks/SFO_Delays_by_Destination.ipynb',
    # '../../../examples/dagster_examples/airline_demo/notebooks/Fares_vs_Delays.ipynb',
]


def test_notebooks():
    for notebook_path in notebook_paths_to_test:
        print('currently testing', notebook_path)
        notebook_filename = script_relative_path(notebook_path)

        with open(notebook_filename) as f:
            nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(
            nb,
            {
                'metadata': {
                    'path': script_relative_path(notebook_filename[: notebook_filename.rfind('/')])
                }
            },
        )


# def test_iris_ipynb():
#     notebook_filename = script_relative_path(
#         '../../../docs/sections/learn/guides/data_science/iris-kmeans_3.ipynb'
#     )

#     with open(notebook_filename) as f:
#         nb = nbformat.read(f, as_version=4)
#     ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
#     ep.preprocess(
#         nb,
#         {
#             'metadata': {
#                 'path': script_relative_path('../../../docs/sections/learn/guides/data_science/')
#             }
#         },
#     )
