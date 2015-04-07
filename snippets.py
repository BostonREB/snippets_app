import logging

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