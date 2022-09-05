#
#
from sys import * 
from time import sleep
from os import system 
import os
#
#
'''
Name : Lucas R .
Kelas : X /Rpl
					Program Kasir 
		 Warung Makanan Indonesia
'''
def _textAnimation(_text:str) :
  ssys = stdout
  for i in _text :
    ssys.write(i)
    ssys.flush()
    sleep(0.009)
  return '\n'
    
def listToString(s:list):  
    str1 = ""  
    for ele in s:  
        str1 += ele
    return str1  
    
def readfileMenu():
  while True :
    try:   
  	  with open('Menu.txt','r') as listMenu:
    		menus= listMenu
    		return menus.readlines()
    		menus.close()
    		break 
    except:
	    with open('Menu.txt','x') as Cfile :  
	    	Cfile.write('Gulai ;Harga : 10.000')
	    	Cfile.close()
	    continue
def display():
	 jum = 0 
	 for i in readfileMenu():
	   jum += 1
	   Harga = i.split(";")[1]
	   menu = i.split(";")[0]
	   print('='*40)
	   sleep(0.1)
	   _textAnimation(f'''\n{jum}. {menu}
			\t{Harga}\n''')
	 
def menuHarga() -> list :
	jum = 1
	arr = {}
	for i in readfileMenu():
		jum += 1
		Harga = i.split(";")[1]
		arr.update({jum -1 : {Harga}})
	return arr
def menuList() -> list:
	jum = 0 
	arr = {}
	for i in readfileMenu():
		jum += 1
		men = i.split(";")[0].rstrip()
		arr.update({jum :{men}})
	return arr 
def Main():
  system('clear')
  sleep(1)
  display()
  arr = menuHarga()
  arr2 = menuList()
  Lanjut = False
  brr = False
  while True : 
  	ulang =  False
  	while True:
	  	try:
	  		pesanan = int(input(_textAnimation('Ingin memesan apa? : ').rstrip()))
	  	except:
	  		print('Masukan Angka Mass!!!')
	  		continue
	  	if pesanan >= len(arr) + 1 or pesanan <= 0 :
	  		print('Nomor yang ada masukan tidak ada ')
	  	else:
	  		Lanjut = True
	  	if Lanjut:
	  		try:
		  		with open('struct.txt','xb+') as f:
		  			f.write(f'{listToString(arr2[pesanan])} {listToString(arr[pesanan])}'.encode())
		  			f.close()
		  	except:
		  		with open('struct.txt','ab') as f:
		  			f.write(f'{listToString(arr2[pesanan])} |{listToString(arr[pesanan])}'.encode())
		  			f.close()	
		  	Lanjut = False
	  		break
  	while True :
	  	try:
		  	lagi = str(input(_textAnimation('Ingin memesan lagi ? y/n  : ').rstrip()))
	  	except:
	  		continue
	  	if lagi == 'y' or lagi == 'Y':
	  		ulang = True
	  		break 
	  	elif lagi == 'n' or lagi == 'N':
	  		brr = True
	  		break
	  	else:
	  		continue
  	if ulang == True:
	    continue
  	elif brr:
	  	break 
  system('clear')
  with open('struct.txt','r') as R:
	  print('='*13,'<STRUCT>','='*13)
	  print('Terimakasih Telah membeli :')
	  for i in R.readlines():
	    print(f'\n\t{listToString(i.strip().split("|"))}')
  
  if os.path.exists('struct.txt'):
   os.unlink('struct.txt')	
if __name__ == '__main__':
  Main()
  
  
																				
																							
																							
														
												
												
												
												
												
												
												
						
						
						
						
						
						
						
		
						
						