#!C:\Program Files\EasyPHP-Devserver-17\eds-binaries\python\default\python.exe
# -*- coding: utf-8 -*-
import sys
import string
import os
def cabecalho():
   print ("Content-type: text/html")
   print ("")
   print ("<html><head>")
   print ("</head><body>")
   print ("<title>TCC - Bruna Toledo Guedes</title>")  
   print ("<meta charset=""utf-8"" />")
   print ("		<meta name=""viewport"" content=""width=device-width, initial-scale=1, user-scalable=no"" />")
   print ("		<link rel=""stylesheet"" href=""assets/css/main.css"" />")
   print ("	</head>")
   print ("	<body>")
   print ("		<!-- Wrapper -->")
   print ("			<div id=""wrapper"">")
   print ("				<!-- Main -->")
   print ("					<div id=""main"">")
   print ("						<div class=""inner"">")
   print ("							<!-- Header -->")
   print ("								<header id=""header"">")
   print ("									<a href=""index.html"" class=""logo""><strong>TCC-Trabalho de Conclusão de Curso - </strong> Bruna Toledo Guedes</a>")
   print ("									<ul class=""icons"">")
   print ("										<li><a href=""#"" class=""icon fa-twitter""><span class=""label"">Twitter</span></a></li>")
   print ("										<li><a href=""#"" class=""icon fa-facebook""><span class=""label"">Facebook</span></a></li>")
   print ("										<li><a href=""#"" class=""icon fa-snapchat-ghost""><span class=""label"">Snapchat</span></a></li>")
   print ("										<li><a href=""#"" class=""icon fa-instagram""><span class=""label"">Instagram</span></a></li>")
   print ("										<li><a href=""#"" class=""icon fa-medium""><span class=""label"">Medium</span></a></li>")
   print ("									</ul>")
   print ("								</header>")
   print ("							<!-- Content -->")
   print ("								<section>")
   print ("									<header class=""main"">")
   print ("										<h1>Resultado</h1>")
   print ("									</header>")
#   print ("									<p align=""justify"">O presente trabalho ")
   print ("				<!-- Sidebar -->")
   print ("					<div id=""sidebar"">")
   print ("						<div class=""inner"">")
   print ("							<!-- Search -->")
   print ("								<section id=""search"" class=""alt"">")
   print ("									<form method=""post"" action=""#"">")
   print ("										<input type=""text"" name=""query"" id=""query"" placeholder=""Search"" />")
   print ("									</form>")
   print ("								</section>")
   print ("								<nav id=""menu"">")
   print ("									<header class=""major"">")
   print ("										<h2>Menu</h2>")
   print ("									</header>")
   print ("									<ul>")
   print ("										<li><a href=""index.html"">Página Inicial</a></li>")
   print ("										<li><a href=""apresentacao.html"">Apresentação</a></li>")
   print ("										<li><a href=""trabalhos.html"">Trabalhos Relacionados</a></li>")
   print ("										<li><a href=""ferramentas.html"">Ferramentas Testadas</a></li>")
   print ("										<li><a href=""executando.html"">Executando o Algoritmo</a></li>")
   print ("										<li><a href=""analise.html"">Análise dos Resultados</a></li>")
   print ("									</ul>")
   print ("								</nav>")
   print ("								<section>")
   print ("									<header >")
   print ("										<h2>Entre em Contato</h2>")
   print ("									</header>")
   print ("									<ul class=""contact"">")
   print ("										<li class=""fa-home"">brunatoledo30@gmail.com	</li>")
   print ("									</ul>")
   print ("								</section>")
   print ("						</div>")
   print ("					</div>")
   print ("			</div>")
   print ("		<!-- Scripts -->")
   print ("			<script src=""assets/js/jquery.min.js""></script>")
   print ("			<script src=""assets/js/skel.min.js""></script>")
   print ("			<script src=""assets/js/util.js""></script>")
   print ("			<!--[if lte IE 8]><script src=""assets/js/ie/respond.min.js""></script><![endif]-->")
   print ("			<script src=""assets/js/main.js""></script>")
   return

def obterTermo(pesquisar,posicao):
    # objetivo: a função retornará a linha do arquivo exported.html 
    #           que contém o termo que se quer obter.
    # parametros:
    # pesquisar: é o parametro que contém a parte do texto que queremos 
    #            pesquisar no arquivo exported.html
    # posicao: é o parametro que indica se o resultado que queremos está 
    #          na mesma linha ou na linha imediatamente posterior a linha 
    #          do texto encontrado. 
    #          posicao=0 indica na mesma linha e 
    #          posicao=1 indica que o termo estará na linha imediatamente posterior
    resultado = "N&atilde;o encontrado" 
    encontrou = -1
    for linha in texto :
       #print(linha+"<br>")
       #print(encontrou)
       if posicao==1:
          if encontrou <> -1:
             resultado = linha
       encontrou = string.find(linha,pesquisar)
       if posicao==0:
          if encontrou <> -1:
             resultado = linha
    return resultado

# abrindo o arquivo que contém a árvore sintática da frase
# o arquivo for gerado através do link http://visl.sdu.dk/visl/pt/parsing/automatic/trees.php
arq = open('/Users/jguedes/Downloads/exported.html', 'r')
texto = arq.readlines()

# imprimindo cabeçalhos
cabecalho()

# obter a frase
frase = obterTermo("SOURCE: Running text",1)

# obter o verbo auxiliar
obterVerboAuxiliar = obterTermo("-VAUX:v*fin",0)
s = obterVerboAuxiliar.split("\t")
verboAuxiliar=s[len(s)-1]
existeVerboAuxiliar = "N&atilde;o encontrado"
if obterVerboAuxiliar <> "N&atilde;o encontrado":
    existeVerboAuxiliar = "Encontrado"
	
# obter o verbo no particípio
obterVerboParticipio = obterTermo("-MV:v*pcp",0)
s = obterVerboParticipio.split("\t") 
verboParticipio=s[len(s)-1] 
existeVerboParticipio = "N&atilde;o encontrado"
if verboParticipio <> "N&atilde;o encontrado":
    existeVerboParticipio = "Encontrado"

# obter o sujeito
linhaSujeito = obterTermo("-SUBJ:prop",0)
s = linhaSujeito.split("\t")
sujeito=s[len(s)-1]

# obter o complemento verbal
linhaCompl = obterTermo("-ACC:prop",0)
s = linhaCompl.split("\t")
complementoVerbal=s[len(s)-1]

# mostrar resultados em tela
print ("<br><p style='margin-left: 80'><strong> Frase em An&aacute;lise: "+frase+"</strong></p>")
print ("<p style='margin-left: 80'>Verbo Auxiliar: "+str(existeVerboAuxiliar))
if existeVerboAuxiliar=="Encontrado":
   print (" => "+verboAuxiliar+"</p>")
print ("<p style='margin-left: 80'>Verbo no Partic&iacute;pio: "+str(existeVerboParticipio))
if existeVerboParticipio=="Encontrado":
   print (" => "+verboParticipio+"</p>")
#print ("<br> Linha onde o Sujeito foi localizado: "+linhaSujeito+" <br>")
print ("<p style='margin-left: 80'>Sujeito localizado: "+str(sujeito)+"</p>")
print ("<p style='margin-left: 80'>Complemento Verbal localizado: "+str(complementoVerbal)+"</p>")

if (verboAuxiliar=="N&atilde;o encontrado" or verboParticipio == "N&atilde;o encontrado") :
    print ("<p style='margin-left: 80'><strong> Nesta frase, o algoritmo selecionou o complemento verbal como solu&ccedil;&atilde;o => "+str(complementoVerbal)+" <br></strong></p>")
else:
    print ("<p style='margin-left: 80'><strong> Nesta frase, o algoritmo selecionou o sujeito como solu&ccedil;&atilde;o => "+str(sujeito)+" <br></strong></p>")
	   

print ("</body></html>")
arq.close()

#renomear arquivo
#/Users/jguedes/Downloads/exported.html
os.rename(/Users/jguedes/Downloads/exported.html, /Users/jguedes/Downloads/exported.html)




