from dm_control import suite

from ostrichrl.tasks.cassie import SUITE as cassie_suite
from ostrichrl.tasks.ostrich import SUITE as ostrich_suite

from ostrichrl.tasks import cassie
from ostrichrl.tasks import ostrich

suite._DOMAINS['cassie'] = cassie
suite._DOMAINS['ostrich'] = ostrich


def make_cassie(task, task_kwargs=None, environment_kwargs=None, visualize_reward=None):
    task_kwargs = task_kwargs or {}
    if environment_kwargs is not None:
        task_kwargs = task_kwargs.copy()
        task_kwargs["environment_kwargs"] = environment_kwargs
    env = cassie_suite[task](**task_kwargs)
    env.task.visualize_reward = visualize_reward
    return env

def make_ostrich(task, task_kwargs=None, environment_kwargs=None, visualize_reward=None):
    task_kwargs = task_kwargs or {}
    if environment_kwargs is not None:
        task_kwargs = task_kwargs.copy()
        task_kwargs["environment_kwargs"] = environment_kwargs
    env = ostrich_suite[task](**task_kwargs)
    env.task.visualize_reward = visualize_reward
    return env
