import  pyAesCrypt 
bufferSize  =  64  *  1024 
contraseña = "nolose"
opc= input ("Desea encriptar s/n  ")
if (opc == 's'):
	print ("se realizara un cifrado del documneto")
	contraseña1 = input ("INGRESE LA CONTRASEÑA:  ")
	if(contraseña1 == contraseña):
		pyAesCrypt . encryptFile ( "hola a todos.txt" ,  "hola.aes" ,  contraseña ,  bufferSize )
		print ("Documento cifrado con exito") 
		exit(0)
if(opc == 'n'):
	opc2= input ("Desea desencriptar s/n:  ")
	if (opc2 == 's'):
		print ("se realizara un desifrado del documento")
		contraseña1 = input ("INGRESE LA CONTRASEÑA:  ")
		if (contraseña1 == contraseña): 
			pyAesCrypt . decryptFile ( "hola.aes" ,  "hola_desifrado.txt" ,  contraseña ,  bufferSize )
			print ("Documento desencriptado exitosamente")
			exit(0)
		else:
			print("contraseña incorrecta")
			exit(1)
	if (opc2 == 'n'):
		print("Programa terminado")
		exit(1)