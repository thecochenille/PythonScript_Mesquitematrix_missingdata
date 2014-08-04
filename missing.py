import re
import sys

def hw(): # function to print a text
    print 'This is the proportion of non applicable characters and missing data for each taxon'

def lines(fp): #fonction to count 
    print str(len(fp.readlines()))


def datatype( datafile ):
    datat = "STANDARD"
            
    datafilecopy = datafile

    if datat in datafilecopy.read():
      print "This is a morphological matrix"
      matrix()
    else:
      print "This is not a morphological matrix"
                


def formatcheck( datafile ): 
  first_line = datafile.readline()
  print first_line
  nexus = "#NEXUS"
  if nexus in first_line:
      datatype( datafile )
  else:
      print "This is not a Nexus file"


def ncharnumb( datafile ):

  charnumb = 0

  for line in datafile:
    match = re.search('NCHAR=(\d+);', line)

    if match:
      charnumb = match.group(1)
      return charnumb

def matrix():

  datafile = open(sys.argv[1])
  matrix_started = 0

  nchar = ncharnumb( datafile )

  dictionnary = {}

  characters = 0

  for line in datafile:
    if matrix_started:
      if ';' in line:
        break
      else:
        match = re.search( '^\t?(.*)\s{2,}([\?\d-]+)', line )
        if match:
          key = match.group(1)
          sequence = match.group(2)

          na = float( sequence.count( '-' ) ) / float( nchar ) * 100
          missing = float( sequence.count( '?' ) ) / float( nchar ) * 100

          # buidling the species dictionnary
          dictionnary[ key ] = [ na, missing ]

          # character number with missing data

          # initialize the list length to the number of characters
          if( 0 == characters ):
            characters = range(1, len( sequence )+1)
            characters = dict.fromkeys( characters, 0 )


          for i, c in enumerate( sequence ):
            if "?"==c:
              characters[ i + 1 ] += 1


    else:
      if 'MATRIX' in line:
        matrix_started = 1

  sortedDictionnary = sorted( dictionnary.items(), key=lambda t: t[1][1] )
  hw()
  print "Species data"

  for key, value in sortedDictionnary:
    print str( key ) + ' has ' + str( value[ 1 ] ) + '%% missing characters and ' + str( value[ 0 ] ) + '%% n/a characters'

  taxonCount = len( sortedDictionnary )

  print "Character data"

  sortedCharacters = sorted( characters.items(), key=lambda t: t[1] )

  for key, value in sortedCharacters:
    print "Character" + str( key ) + ' is missing in ' + str( float( characters[ key ] ) / float( taxonCount ) * 100 ) + '%% of species'


	
def main():
  datafile = open(sys.argv[1])
  
  formatcheck( datafile )
  
    



if __name__ == '__main__':
    main()
