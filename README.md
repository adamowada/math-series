# 401 Lab 02 - Math Series
### Adam Owada

https://github.com/adamowada/math-series/pull/1

## Functionality

series.py is a module with 3 functions: fibonacci, lucas, and sum_series. The fibonacci and lucas functions each have one parameter, n, and return the nth value of the fibonacci series or the lucas series respectively. The sum_series function has one mandatory parameter, n, and two optional parameters, first and second. The sum_series function then returns the nth value of an arbitrarily defined sum series. If no optional arguments are given, sum_series defaults to acting like the fibonacci series (first = 0, second = 1).

## Testing

There are 17 tests defined in test_series.py. The tests pass when each of the functions return the correct value in their series. Currently all tests pass.


## Attribution

https://linux.die.net/diveintopython/html/power_of_introspection/optional_arguments.html helped me with optional parameters.

https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python  helped me with line continuation.
