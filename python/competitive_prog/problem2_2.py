import argparse

def main(args):
    print(f'a*b= {args.a * args.b}') 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=float, help="First number") 
    parser.add_argument('b', type=float, help="Second number") 
    args = parser.parse_args()
    
    main(args)