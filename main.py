#!/usr/bin/env python3
"""
Simple calculator module + CLI.

Usage:
  python main.py add 1 2
  python main.py div 4 2
"""
import argparse
from typing import Callable


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def main() -> None:
    parser = argparse.ArgumentParser(prog="calculator", description="Simple calculator")
    parser.add_argument("op", choices=["add", "sub", "mul", "div"], help="operation")
    parser.add_argument("a", type=float, help="first number")
    parser.add_argument("b", type=float, help="second number")
    args = parser.parse_args()

    ops: dict[str, Callable[[float, float], float]] = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }

    try:
        result = ops[args.op](args.a, args.b)
    except Exception as e:
        print("Error:", e)
        raise SystemExit(1)

    # print as integer when it's an exact int
    if result.is_integer():
        print(int(result))
    else:
        print(result)


if __name__ == "__main__":
    main()
