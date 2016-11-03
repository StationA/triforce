# triforce
No-bullshit n-triples encoder/decoder

# Getting Started

### Installing latest (master) from Github

```
pip install git+https://github.com/StationA/triforce.git#egg=triforce
```

### Installing from source

```
git clone https://github.com/StationA/triforce.git
cd triforce
pip install .
```

# Usage

### Encoding a subject, predicate, value as an n-triple

```python
import triforce

nt = triforce.encode('http://stationa.xyz', 'http://schema.org/name', 'Station A')
print(nt)
# <http://stationa.xyz> <http://schema.org/name> "Station A" .
```

# Contributing

### Running tests

```
tox -e dev
```

