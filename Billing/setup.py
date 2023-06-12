import sys
import csv



def main():
    setup()

def setup(filename = None):
    if filename is None:
        filename = check()
    else:
        filename = filename
    try:
      try:
          with open(filename, 'r') as f:
              return filename
      except FileNotFoundError:    
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(("item_name","item_price"))
        f.close()
        return filename
    except FileNotFoundError:
        sys.exit("File not found")


def check():
    if len(sys.argv) > 2 or len(sys.argv) < 2:
      sys.exit("Invalid arguments\nTry running the program in the command line as 'python __init__.py items.csv'")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Invalid, The file is not a CSV file")
    else:
        return sys.argv[1]
     
        

if __name__ == "__main__":
    main()