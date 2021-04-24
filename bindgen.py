
# MIT License
# 
# Copyright (c) 2020, 2021 magistermaks
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# import stuff
import argparse
import os.path
import re

# parse cl args
parser = argparse.ArgumentParser( description="Dynamic binding generator" )
parser.add_argument( "--source", help="select the source file", type=str, default="./src/api.cpp" )
parser.add_argument( "--output", help="select the output file", type=str, default="./java/src/main/java/net/darktree/libtile2d/binding/TileLibrary.java" )
parser.add_argument( "--verbose", help="print some garbage to console", action="store_true" )
args = parser.parse_args()
    
# load source file
try:
    ifile = open(args.source, mode='r')
except:
    print( "Error: Failed to open source file at '" + args.source + "'!" )
    print( " * Try changing source file location using '--source' flag" )
    exit()
    
#load output file
try:
    ofile = open(args.output, mode='w')
except:
    print( "Error: Failed to open output file at '" + args.output + "'!" )
    print( " * Try changing output file location using '--output' flag" )
    exit()

# get contents
lines = ifile.read().split('\n')
ifile.close()
api = []

# print status
if args.verbose:
    print( "Reading Source..." )

# parse file
for x in range( len(lines) ):
    line = lines[x]
    if line.startswith("FUNC"):

        obj = { "comment": lines[x-1][4:], "function": line[5:-2] }
        api.append(obj)
        
        if args.verbose:
            print( " * " + str(obj) )
      
# print status      
if args.verbose:
    print( "\nGenerating Binding..." )
    
output = ""
    
 # assume that the target is a java project
if "/main/java/" in args.output:
    parts = os.path.dirname(args.output).split("/main/java/")
    if len(parts) == 2:
        package = parts[1].replace("/", ".")
        output += "package " + package + ";\n"
        print( " * Deduced package is: '" + package + "'" )
    else:
        print( parts )
        print( " * Failed to deduce package!" )
    
output += "\n"
output += "import com.sun.jna.Callback;\n"
output += "import com.sun.jna.Library;\n"
output += "import com.sun.jna.Pointer;\n"
output += "\n"
output += "// Auto generated by bindgen.py \n"
output += "public interface TileLibrary extends Library {\n\n"
    
def get_interface( func ):
    str1 = func.replace("void*", "Pointer").replace("const char*", "String").replace("int*", "Pointer")
    return re.sub(r"\bbool\b", "boolean", str1) + ";"
    
for method in api:
    output += "    /// " + method["comment"] + "\n"
    output += "    " + get_interface( method["function"] ) + "\n\n"
        
output += "}\n"

ofile.write( output )
ofile.close()

if args.verbose:
    print( " * Done!" )





