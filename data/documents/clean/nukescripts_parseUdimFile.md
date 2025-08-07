# nukescripts.parseUdimFile
nukescripts.parseUdimFile(_f_)

Parsing a filename string in search of the udim number. The function returns the udim number, and None if it is not able to decode the udim value.
The udim value is a unique number that defines the tile coordinate. If u,v are the real tile coordinates the equivalent udim number is calculated with the following formula: udim = 1001 + u + 10 * v (Note: u >=0 && u < 10 && udim > 1000 && udim < 2000)
Redefine this function if the parsing function is not appropriate with your filename syntax.