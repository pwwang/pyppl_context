"""Upstream and downstream process reference for PyPPL"""
import pickle
from pyppl.plugin import hookimpl
from pyppl.config import config

__version__ = "0.0.2"

config.config.context_callback = None
config.config.context_callfront = None


# we have to make sure that channel can be referred if a process is skipped
# try to save it in a file (proc.channel)


@hookimpl
def proc_postrun(proc, status):
    """Post run"""
    chfile = proc.workdir / 'proc.channel'
    if status == 'succeeded':
        with open(chfile, 'wb') as fch:
            pickle.dump(proc.channel, fch)

        if callable(proc.config.context_callback):
            proc.config.context_callback(proc)

    elif status != 'failed':
        if not proc.channel and chfile.is_file():
            with open(chfile, 'rb') as fch:
                proc.channel = pickle.load(fch)

        if callable(proc.config.context_callback):
            proc.config.context_callback(proc)


@hookimpl
def proc_prerun(proc):
    """Pre run"""
    if callable(proc.config.context_callfront):
        proc.config.context_callfront(proc)
