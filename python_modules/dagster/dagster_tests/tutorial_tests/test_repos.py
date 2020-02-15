from dagster.tutorial.repos import define_repo
from dagster.tutorial.scheduler import cereal_repository

from dagster import execute_pipeline
from dagster.utils import pushd, file_relative_path


def test_define_repo():
    repo = define_repo()
    assert repo.name == 'hello_cereal_repository'
    assert repo.has_pipeline('hello_cereal_pipeline')
    with pushd(file_relative_path(__file__, '../../dagster/tutorial/')):
        result = execute_pipeline(repo.get_pipeline('hello_cereal_pipeline'))
    assert result.success


def test_define_scheduler_repo():
    repo = cereal_repository()
    assert repo.name == 'hello_cereal_repository'
    assert repo.has_pipeline('hello_cereal_pipeline')
    with pushd(file_relative_path(__file__, '../../dagster/tutorial/')):
        result = execute_pipeline(repo.get_pipeline('hello_cereal_pipeline'))
    assert result.success
