#!/usr/bin/env python3
import sys
import argparse
from app_ctl.math_ops_def import *

def main():
    """Main entry point for the calcctl command line interface."""
    parser = argparse.ArgumentParser(description='Command line calculator utility')
    
    # Create subparsers for different operations
    subparsers = parser.add_subparsers(dest='operation', help='Operation to perform')
    subparsers.required = True
    
    # Add parser
    add_parser = subparsers.add_parser('add', help='Add two numbers')
    add_parser.add_argument('a', type=float, help='First number')
    add_parser.add_argument('b', type=float, help='Second number')
    
    # Subtract parser
    sub_parser = subparsers.add_parser('subtract', help='Subtract second number from first')
    sub_parser.add_argument('a', type=float, help='First number')
    sub_parser.add_argument('b', type=float, help='Second number')
    
    # Multiply parser
    mul_parser = subparsers.add_parser('multiply', help='Multiply two numbers')
    mul_parser.add_argument('a', type=float, help='First number')
    mul_parser.add_argument('b', type=float, help='Second number')
    
    # Divide parser
    div_parser = subparsers.add_parser('divide', help='Divide first number by second')
    div_parser.add_argument('a', type=float, help='First number')
    div_parser.add_argument('b', type=float, help='Second number')
    
    args = parser.parse_args()
    
    try:
        if args.operation == 'add':
            result = add(args.a, args.b)
        elif args.operation == 'subtract':
            result = subtract(args.a, args.b)
        elif args.operation == 'multiply':
            result = multiply(args.a, args.b)
        elif args.operation == 'divide':
            result = divide(args.a, args.b)
        
        # Print result
        print(result)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
#version 1
if __name__ == '__main__':
    main()