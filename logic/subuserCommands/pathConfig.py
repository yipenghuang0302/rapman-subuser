import sys,os,inspect,site

def getSubuserDir():
  """ Get the toplevel directory for subuser. """
  return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))) # BLEGH!

oldSubuserlibLocation = os.path.join(getSubuserDir(),"logic","subuserCommands","subuserlib")
if os.path.exists(oldSubuserlibLocation):
  sys.exit("It looks like you recently did a git pull.  We recently moved one of our source directories.  Unfortunately, git isn't capable of dealing with directory renaming so you'll have to help us out.  Please delete the directory:\n\n"+oldSubuserlibLocation)

site.addsitedir(os.path.join(getSubuserDir(),"logic"))

