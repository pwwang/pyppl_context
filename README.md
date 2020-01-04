# pyppl_context

Upstream and downstream process reference for PyPPL

## Installation
```shell
pip install pyppl_context
```

## Usage
```python
pXXX = Proc(...)
# ... other configurations for pXXX

pYYY.depends = pXXX
pYYY.config.context_callfront = lambda p: setattr(p.args, 'argument', pXXX.channel.get(0))
# pYYY.config.context_callback = ...
```
