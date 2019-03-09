# triforce
No-bullshit n-triples encoder/decoder

## Getting Started

### Installing from Github

```
pip install git+https://github.com/StationA/triforce.git#egg=triforce
```

### Installing from source

```
git clone https://github.com/StationA/triforce.git
cd triforce
pip install .
```

## Usage

### Encoding a subject, predicate, value as an n-triple

```bash
triforce encode 'http://stationa.xyz' 'http://schema.org/name' 'Station A'
# <http://stationa.xyz> <http://schema.org/name> "Station A" .
```

## Contributing

When contributing to this repository, please follow the steps below:

1. Fork the repository
1. Submit your patch in one commit, or a series of well-defined commits
1. Submit your pull request and make sure you reference the issue you are addressing

### Running tests

```
tox -e dev
```

