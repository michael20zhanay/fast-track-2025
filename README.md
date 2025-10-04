# dotdotdot: A Fast-Track Programming Project

> [!IMPORTANT]
> See [learning](learning.md) for learning goals, outcomes, and skills.

## Summary

`dotdotdot` is a REST API µservice for performing image analysis and manipulation.

## Development Guide

To develop `dotdotdot`, you will need a Linux environment and a Python virtual
environment.

Install dependencies:

```sh
python -m pip install -r requirements.txt
```

To run the µservice:

```sh
python dotdotdot.py
```

To query the µservice's test endpoint (first `pip install httpie`):

```sh
http get 127.0.0.1:8000/test
```
