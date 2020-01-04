import pytest
from diot import Diot
from pyppl import config
import pyppl_context

def test_setup():
	pyppl_context.setup(config)
	assert config.config.context_callback is None
	assert config.config.context_callfront is None

def test_run(tmp_path):
	proc = Diot(
		channel = [1,2,3],
		workdir = tmp_path,
		config = Diot(
			context_callfront = lambda p: setattr(p, 'a', 1),
			context_callback = lambda p: setattr(p, 'b', 2))
	)
	pyppl_context.proc_postrun(proc, 'succeeded')
	assert tmp_path.joinpath('proc.channel').is_file()
	assert proc.b == 2
	assert 'a' not in proc

	proc.channel = None
	pyppl_context.proc_postrun(proc, 'cached')
	assert proc.channel == [1,2,3]
	assert proc.b == 2
	assert 'a' not in proc

	pyppl_context.proc_prerun(proc)
	assert proc.a == 1
