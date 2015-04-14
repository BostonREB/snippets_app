import sys
import logging
import argparse

#set the log output file, and the log fevel
logging.basicConfig(finename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
  """
  Store a snippet with an associated name.

  Returns the name of the snippet.
  """
  logging.error("FIXME: Unimplemented - put({!r}, {!r}".format(name, snippet))
  return name, snippet

def get(name):
  """
  Retrieve the snippet with the given name.

  If there is no snippet an error will be generated.

  Returns the snippet.
  """
  logging.error("FIXME: Unimplemented - get({!r})".format(name))
  return ""

# Main
def main():
  """Main function"""
  logging.info("Constructing parser")
  parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

  subparsers = parser.add_subparsers(dest="command", help="Available commands")

  #Subparser for the put command
  logging.debug("Constructing put subparser")
  put_parser = subparsers.add_parser("put", help="Store a snippet")
  put_parser.add_argument("name", help="The name of the snippet")
  put_parser.add_argument("snippet", help="The snippet text")

  #Subparser for the get command
  logging.debug("Contructing get subparser")
  get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
  get_parser.add_argument("name", help="The name of the snippet")

  arguments = parser.parse_args(sys.argv[1:])

  # Convert parsed arguments from Namespace to dictionary
  arguments = vars(arguments)
  command = arguments.pop("command")

  if command == "put":
    name, snippet = put(**arguments)
    print ("Stored {!r} as {!r}".format(snippet, name))
  elif command == "get":
    snippet = get(**arguments)
    print ("Retrieved snippet: {!r}".format(snippet))


if __name__ == "__main__":
    main()