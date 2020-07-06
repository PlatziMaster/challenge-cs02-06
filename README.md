# PS06: Designing a set

Complete the implementation of the `Set` data structure without using built-in set or dict.

The `Set` class must expose the following methods.
* `Set()` constructor that takes no arguments.
* `add(k)` inserts value `k` into the set.
* `contains(k)` returns a boolean indicating whether `k` is part of the set or not.
* `remove(k)` removes the value `k` from the set if exist, else do nothing.

Remember that set operations must be *efficient* in space and time and that sets don't contain
duplicates.

The following is a usage example of the `Set` class:

```python
data = Set()
data.add(1)
data.add(2)
data.add(3)
data.contains(4)  # Returns False
data.contains(1)  # Returns True
data.add(4)
data.contains(4)  # Returns True
data.remove(6)  # Does nothing
data.contains(2)  # Returns True
data.remove(2)
data.contains(2)  # Returns False (previously deleted)
```

**Constraints**

Your set is expected to:
* Support up to 10^5 operations
* Store integers values in the range [0, 10^9]

# How to submit.

* Implement the methods listed above under `solution.py`.
* All code will be checked for readability using [**pylint**](https://www.pylint.org/).
* A grader is included, and all test cases must pass.
* ***DO NOT** modify the grader!*
* ***DO NOT** use built-in set or dict!*

# Debugging

* You can run the grader with the command `python3 grader.py < test_cases/a.txt` where `a` is the test case you want to run.
* Yo can run all test cases with the command: `for f in test_cases/*.txt; do python3 grader.py < "$f"; done`