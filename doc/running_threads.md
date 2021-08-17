### This is the way to execute tests in multiple threads

``` 
python -m pytest -n 4 
```

where -n takes a number of threads to use

to run those tests in parallel pytest-xdist package needs to be installed