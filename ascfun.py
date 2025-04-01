# File: ascfun.py
# Functions for conversion between ASCII and bits
from pylab import *
import numpy as np

def asc2bin(txt, bits=8):
    """
    ASCII message to serial binary conversion
    >>>>> dn = asc2bin(txt, bits) <<<<<
    where txt ASCII message (text string)
        abs(bits) bits per character, default: 8
        bits > 0 LSB first parallel to serial conv
        bits < 0 MSB first parallel to serial conv
        dn binary output DT sequence
    """
    txtnum = np.array([ord(c) for c in txt], np.int16)
    if bits > 0:
        # powers of 2: 2**0, 2**-1, 2**-2, ..., 2**-(bits-1)
        p2 = np.array(np.power(2.0, -np.arange(bits)), np.float32)
    else:
        # powers of 2: 2**(bits+1), ..., 2**-2, 2**-1, 2**0
        p2 = np.array(np.power(2.0, np.arange(bits+1,1)), np.float32)
    # 2-dim array of bits, one row per character in txt
    B = np.array(np.mod(np.floor(np.outer(txtnum,p2)),2),np.int8)
    # parallel to serial conversion
    return np.reshape(B, -1)

def bin2asc(dn, bits=8, flg=1):
    """
    Serial binary to ASCII text conversion
    >>>>> txt = bin2asc(dn, bits, flg) <<<<<
    where dn binary input sequence
        abs(bits) bits per char, default=8
        bits > 0 LSB first parallel to serial
        bits < 0 MSB first parallel to serial
        flg != 0 limit range to [0...127]
        txt output text string
    """
    
    no_of_char = int(np.floor(size(dn)/abs(bits)))
    #if(mod(len(dn),8)!=0): # If length of input data bits not a multiple of 8, add zeros to make it a multiple of 8  
        #no_of_zeros = len(dn) - 8*no_of_char
    #if bits > 0: #Append the zeros
          #np.lib.pad(dn,(0,no_of_zeros),'constant',constant_values = (0))
    dec =[0]*(no_of_char) #Initializing array for decimal values with zeros 
    if bits > 0: # Pos powers of 2, increasing exp
        p2 = np.power(2.0,arange(0,bits,1))
    else: # Pos powers of 2, decreasing exp
        p2 = np.power(2.0,-1+arange(-bits,0,-1))
    for index in np.arange(no_of_char):# loop for converting 8 binary bits to decimal value sequenctially from the input bit sequence
        dec[index] = int(inner(dn[abs(bits)*index+arange(0,abs(bits))],p2))
    data_string = ''.join(chr(c) for c in dec) # Converting decimal value to ASCII for each element in the array
    return data_string # string returned
