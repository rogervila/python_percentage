# Python Percentage

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rogervila_python_percentage&metric=alert_status)](https://sonarcloud.io/dashboard?id=rogervila_python_percentage)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=rogervila_python_percentage&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=rogervila_python_percentage)


Calculate percentages without worrying about ZeroDivision errors


## Install

```sh
pip install python_percentage
```

## Usage

`python_percentage` comes with different useful functions for different percentage calculations

### Calculate percentage between 2 floats

```py
from python_percentage import get_percentage

# I want to get the 20.0% of 200.0
result = get_percentage(20.0, 200.0)
# 200.0 * float(20.0) / float(100.0)

print(result) # 40.0
```

### Calculate which percentage represents a float based on another float

```py
from python_percentage import percentage_of

# I want to get which percentage is 1.0 of 2.0
result = percentage_of(1.0, 2.0)
# 100.0 * float(1.0) / float(2.0)

print(result) # 50.0
```

### Increment percentage of a float

```py
from python_percentage import increment

# I want to increment a 10.0% the float 20.0
result = increment(10.0, 20.0)
# 20.0 + get_percentage(10.0, 20.0)

print(result) # 22.0
```

### Decrement percentage of a float

```py
from python_percentage import decrement

# I want to decrement a 10.0% the float 20.0
result = decrement(10.0, 20.0)
# 20.0 - get_percentage(10.0, 20.0)

print(result) # 18.0
```
