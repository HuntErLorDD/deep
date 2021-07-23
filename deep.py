import colorama
import os
spam = ("""                                                           
  __| | ___  ___ _ __   _ __  _   _ 
 / _` |/ _    _   '_   | '_  | | | |
| (_| |  __/  __/ |_) || |_) | |_| |
  __,_| ___| ___| .__(_) .__/  __, |
                |_|    |_|    |___/  2.0
""")
line_a = ("|-----------------------------------------------------")
print(chr(27)+"[1;33m"+spam)
print("\033[;36m"+line_a)
#variables spam(1)
spam_a = ("\n|http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page")
spam_b = ("\n|The Hidden Wiki es la versión de Wikipedia de la dark web.")
spam_c = ("\n|Se trata de un directorio que indexa enlaces de páginas .onion para ayudarte")
spam_d = ("\n|a navegar por la red Tor. Los directorios como este son importantes porque las")
spam_e = ("\n|URLs .onion no son tan informativas como las utilizadas en la web superficial.")

#variables eggs(2)
eggs_a = ("|\n|https://protonirockerxow.onion/")
eggs_b = ("|\n|Si quieres comunicarte de forma segura utilizando la red Tor, puede que ProtonMail sea lo que necesites. ")
eggs_c = ("|\n|Es uno de los servicios de correo electrónico más populares disponibles en la dark web.")
eggs_d = ("|\n|Garantiza el anonimato de los usuarios al mismo tiempo que les da acceso a un servicio de correo electrónico de calidad.")

#variables Duck(3)
duck_a = ("\n|http://3g2upl4pq6kufc4m.onion")
duck_b = ("\n|Este motor de búsqueda funciona en la web superficial (así que es una buena alternativa a Google) y también en la dark web.")

#variables Inter(4)
inter_a = ("\n|http://xpxduj55x2j27l2qytu2tcetykyfxbjbafin3x4i3ywddzphkbrd3jyd.onion/")
inter_b = ("\n|es una fuente de noticias que tiene como objetivo publicar periodismo crítico y valiente. ")
inter_c = ("\n|Se enorgullece de dar a los periodistas la libertad editorial y el apoyo legal que necesitan\n para investigar la corrupción y otras injusticias")

#variables to(5)
to_a = ("\n|http://xmh57jrzrnw6insl.onion/")
to_b = ("\n|Como el motor de búsqueda más antiguo de la red Tor, Torch tiene acceso a la mayor\n base de datos de enlaces .onion disponible. Afirma haber indexado \nmás de mil millones de páginas .onion.")
to_c = ("\n|Ten cuidado porque, como muchas otras herramientas de la dark web, Torch no bloquea los resultados de búsqueda.\n Eso quiere decir que deberías intentar ceñirte a categorías seguras para evitar\n contenido ilegal, estafas y malware.")

#variables tor
tor_a = ("\n|https://www.torproject.org/download/://www.torproject.org/download/")
tor_b = ("\n|Pega este url en tu navegador por defecto, y descarga el navegador tor, puedes elegir")
tor_c = ("|\nEntre la version para android, linux, Windows o Mac")
tor_d = ("\n|No recomiendo navegar por la darkweb desde un sistema operativo windows.")

creator_a =("| >--Creator--<\n| <--HunterLord-->")
creator_c = ("\n|(1)The Hidden Wiki\n|(2)ProtonMail\n|(3)DuckDuckGo<\n|(4)The Intercept\n|(5)Torch Search Engine\n|(6)Como instalo Tor? \n|(7)Exit")
print("\033[;36m"+creator_a + creator_c)
user_a = int(input("| ===> "))
#funciones de hIDDENWIKI
if user_a==1:
	print("\x1b[1;33m"+spam_a)
	print("\033[4;35m"+spam_b + spam_c + spam_d + spam_e)
	print("\033[;36m""(1)Volver al menu-----(2)Exit")
	user_b = int(input("|===> "))
	if user_b==1:
		print(chr(27)+"[1;33m"+spam)
		print("\033[;36m"+creator_a + creator_c)
		os.system("python3 deep.py")	
   
#FuncionProtonMail
if user_a==2:
	print("\x1b[1;33m"+eggs_a)
	print("\033[4;35m"+ eggs_b + eggs_c + eggs_d)
	print("\033[;36m""(1)Volver al menu-----(2)Exit")
	user_c = int(input("| ===> "))
	if user_c==1:
		os.system('python3 deep.py')

if user_a==3:
	print("\x1b[1;33m"+duck_a)
	print("\033[4;35m"+duck_b)
	print("\033[;36m""(1)Volver al menu-----(2)Exit")
	user_d = int(input("| ===> "))
	if user_d==1:
		os.system('python3 deep.py')

if user_a==4:
    print("\x1b[1;33m"+inter_a)
    print("\033[4;35m"+inter_b + inter_c)
    print("\033[;36m""(1)Volver al menu-----(2)Exit")
    user_e = int(input("| ===> "))
    if user_e==1:
        os.system('python3 deep.py')   

if user_a==5:
    print("\x1b[1;33m"+to_a)
    print("\033[4;35m"+to_b + to_c)        
    print("\033[;36m""(1)Volver al menu-----(2)Exit")
    user_f = int(input("| ===> "))
    if user_f==1:
    	os.system('python3 deep.py')

if user_a==6:
    print("\x1b[1;33m"+tor_a)
    print("\033[4;35m"+tor_b + tor_c + tor_d)
    print("\033[;36m""(1)Volver al menu-----(2)Exit")
    user_f = int(input("| ===> "))
    if user_f==1:
    	os.system('python3 deep.py')

else:
	print("\033[1;33m"+"ERROR, INTERNTELO DENUEVO"+'\033[0;m') 



		

