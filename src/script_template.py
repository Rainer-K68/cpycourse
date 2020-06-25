import sys


def parse_args(args=None):
    """Parse arguments from sys.argv if args is None (the default) or from args
    sequence otherwise.
    """
    import argparse
    parser = argparse.ArgumentParser()
    # Add arguments here

    args = parser.parse_args(args)
    return args


def main(args=None):
    """Main module function.
    
    Exposes this modules' executable functionality for use as a module
    function. 
    Parses arguments from sys.argv if args is None (the default) or from args
    sequence otherwise.
    """
    args = parse_args(args)
    # Add main code here


if __name__ == "__main__":
    sys.exit(main())


