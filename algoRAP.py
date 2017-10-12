#!C:\Program Files (x86)\EasyPHP-Devserver-17\eds-binaries\python\default\python.exe
# -*- coding: utf-8 -*-
import sys
import string
import os
def cabecalho():
   print ("Content-type: text/html")
   print ("")
   print ("<html><head>")
   print ("<title>TCC - Bruna Toledo Guedes</title>")  
   print ("<meta charset=""utf-8"" />")
   print ("          <meta name=""viewport"" content=""width=device-width, initial-scale=1, user-scalable=no"" />")
   print ("          <link rel=""stylesheet"" href=""assets/css/main.css"" />")
   print ("     </head>")
   print ("     <body>")
   print ("          <!-- Wrapper -->")
   print ("               <div id=""wrapper"">")
   print ("                    <!-- Main -->")
   print ("                         <div id=""main"">")
   print ("                              <div class=""inner"">")
   print ("                                   <!-- Header -->")
   print ("                                        <header id=""header"">")
   print ("                                             <a href=""index.html"" class=""logo""><strong>TCC-Trabalho de Conclusão de Curso - </strong> Bruna Toledo Guedes</a>")
   print ("                                             <ul class=""icons"">")
   print ("                                                  <li><a href=""#"" class=""icon fa-twitter""><span class=""label"">Twitter</span></a></li>")
   print ("                                                  <li><a href=""#"" class=""icon fa-facebook""><span class=""label"">Facebook</span></a></li>")
   print ("                                                  <li><a href=""#"" class=""icon fa-snapchat-ghost""><span class=""label"">Snapchat</span></a></li>")
   print ("                                                  <li><a href=""#"" class=""icon fa-instagram""><span class=""label"">Instagram</span></a></li>")
   print ("                                                  <li><a href=""#"" class=""icon fa-medium""><span class=""label"">Medium</span></a></li>")
   print ("                                             </ul>")
   print ("                                        </header>")
   print ("                                       <!-- Content -->")
   print ("                                        <section>")
   print ("                                             <header class=""main"">")
   print ("                                                  <h1>Resultado</h1>")
   print ("                                             </header>")
   return

def rodape():
   print ("                                        </section>")
   print ("                              </div>")
   print ("                         </div>")
   print ("                    <!-- Sidebar -->")
   print ("                         <div id=""sidebar"">")
   print ("                              <div class=""inner"">")
   print ("                                   <!-- Search -->")
   print ("                                        <section id=""search"" class=""alt"">")
   print ("                                             <form method=""post"" action=""#"">")
   print ("                                                  <input type=""text"" name=""query"" id=""query"" placeholder=""Search"" />")
   print ("                                             </form>")
   print ("                                        </section>")
   print ("                                        <nav id=""menu"">")
   print ("                                             <header class=""major"">")
   print ("                                                  <h2>Menu</h2>")
   print ("                                             </header>")
   print ("                                             <ul>")
   print ("                                                  <li><a href=""index.html"">Página Inicial</a></li>")
   print ("                                                  <li><a href=""apresentacao.html"">Apresentação</a></li>")
   print ("                                                  <li><a href=""trabalhos.html"">Trabalhos Relacionados</a></li>")
   print ("                                                  <li><a href=""ferramentas.html"">Ferramentas Testadas</a></li>")
   print ("                                                  <li><a href=""executando.html"">Executando o Algoritmo</a></li>")
   print ("                                                  <li><a href=""analise.html"">Análise dos Resultados</a></li>")
   print ("                                             </ul>")
   print ("                                        </nav>")
   print ("                                        <section>")
   print ("                                             <header >")
   print ("                                                  <h2>Entre em Contato</h2>")
   print ("                                             </header>")
   print ("                                             <ul class=""contact"">")
   print ("                                                  <li class=""fa-home"">brunatoledo30@gmail.com     </li>")
   print ("                                             </ul>")
   print ("                                        </section>")
   print ("                              </div>")
   print ("                         </div>")
   print ("               </div>")
   print ("          <!-- Scripts -->")
   print ("               <script src=""assets/js/jquery.min.js""></script>")
   print ("               <script src=""assets/js/skel.min.js""></script>")
   print ("               <script src=""assets/js/util.js""></script>")
   print ("               <!--[if lte IE 8]><script src=""assets/js/ie/respond.min.js""></script><![endif]-->")
   print ("               <script src=""assets/js/main.js""></script>")
   return

class ArvoreSintatica:
    def __init__(self):
        try:
            with open('/Users/bruna/Downloads/exported.html', 'r') as self.arq:
               self.texto = self.arq.readlines()
        except IOError:
            print ("<p style='margin-left: 80'><strong>Não encontrei o arquivo exported.html</strong></p>")
            print ("                     <p style='margin-left: 80' align=""justify"">Antes de executar o algoritmo, é necessário gerar a árvore sintática da frase que se deseja resolver a anáfora pronominal. <br>Clique no item de menu Executando o Algoritmo.<p>")
            rodape()
            sys.exit(0)
          
    def obterFrase(self):
        # objetivo: a função retornará a linha do arquivo exported.html 
        # que contém a frase do arquivo da árvore sintática.
        resultado = "N&atilde;o encontrado" 
        encontrou = -1
        for linha in self.texto :
            #print(linha+"<br>")
            #print(encontrou)
            if encontrou <> -1:
               resultado = linha
            encontrou = string.find(linha,"SOURCE: Running text")
        return resultado
          
    def obterTermo(self, tag):
        # objetivo: a função retornará a linha do arquivo exported.html 
        #           que contém o termo que se quer obter.
        # parametros:
        # tag: é o parametro que contém a parte do texto que queremos 
        #            tag no arquivo exported.html
        resultado = "N&atilde;o encontrado" 
        encontrou = -1
        for linha in self.texto :
           #print(linha+"<br>")
           #print(encontrou)
           encontrou = string.find(linha,tag)
           if encontrou <> -1:
              resultado = linha
        return resultado
	
    def fecharArquivo(self):
        self.arq.close()
        #renomear arquivo
        #/Users/bruna/Downloads/exported.html
        #os.remove('/Users/bruna/Downloads/_exported.html')
        #os.rename('/Users/bruna/Downloads/exported.html', '/Users/bruna/Downloads/_exported.html')		
          
class Frase:
    def __init__(self):
        self.arvoreGerada = ArvoreSintatica()          
        self.conteudo = self.arvoreGerada.obterFrase()   # pegando a frase da árvore sintática
        #print "<br>"
        #print "arvore gerada"
        #print self.arvoreGerada
        #print "<br>"
        #print self.conteudo
        #print "<br>"
        self.ambiguidade = True   #criar logica para verificar se a frase tem ambiguidade
        self.antecedente = ""   # soluçao
        #self.sujeito = ""
        #self.complementoVerbal = ""
        #self.verboAuxiliar = ""
        #self.verboParticipio = ""

    # obter ambiguidade
    def obterAmbiguidade(self):
        # analisar    obterVerboAuxiliar = arvoreGerada.obterTermo("-VAUX:v*fin")
        #s = obterVerboAuxiliar.split("\t")
        ambiguidade = True
        return ambiguidade
          
    # obter antecedente
    def obterAntecedente(self):
        # analisar    obterVerboAuxiliar = arvoreGerada.obterTermo("-VAUX:v*fin")
        #s = obterVerboAuxiliar.split("\t")
        antecedente = ""
        if (verboAuxiliar=="N&atilde;o encontrado" or verboParticipio == "N&atilde;o encontrado") :
           antecedente = self.obterCompementoVerbal()
        else:
           antecedente = self.obterSujeito()
        return antecedente
          
    # obter o verbo auxiliar
    def obterVerboAuxiliar(self):
        obterVerboAuxiliar = self.arvoreGerada.obterTermo("-VAUX:v*fin")
        s = obterVerboAuxiliar.split("\t")
        verboAuxiliar=s[len(s)-1]
        return verboAuxiliar
          
    # obter o verbo no particípio
    def obterVerboParticipio(self):
        obterVerboParticipio = self.arvoreGerada.obterTermo("-MV:v*pcp")
        s = obterVerboParticipio.split("\t") 
        verboParticipio=s[len(s)-1] 
        return verboParticipio
        
    # obter o sujeito
    def obterSujeito(self):
        linhaSujeito = self.arvoreGerada.obterTermo("-SUBJ:prop")
        s = linhaSujeito.split("\t")
        self.sujeito=s[len(s)-1]
        return self.sujeito
          
    # obter o complemento verbal
    def obterComplementoVerbal(self):
        linhaCompl = self.arvoreGerada.obterTermo("-ACC :prop")
        s = linhaCompl.split("\t")
        self.complementoVerbal=s[len(s)-1]
        return self.complementoVerbal
		
    def finalizarFrase(self):
        self.arvoreGerada.fecharArquivo()

# Main
# abrindo o arquivo que contém a árvore sintática da frase
# o arquivo for gerado através do link http://visl.sdu.dk/visl/pt/parsing/automatic/trees.php

# imprimindo cabeçalhos
cabecalho()

sentencaAnalisada = Frase()

# mostrar resultados em tela

existeVerboAuxiliar = "N&atilde;o encontrado"
if sentencaAnalisada.obterVerboAuxiliar() <> "N&atilde;o encontrado":
   existeVerboAuxiliar = "Encontrado"
   
existeVerboParticipio = "N&atilde;o encontrado"
if sentencaAnalisada.obterVerboParticipio() <> "N&atilde;o encontrado":
   existeVerboParticipio = "Encontrado"

print ("<br><p style='margin-left: 80'><strong> Frase em An&aacute;lise: "+sentencaAnalisada.conteudo+"</strong></p>")

print ("<p style='margin-left: 80'>Verbo Auxiliar: "+str(existeVerboAuxiliar))
if existeVerboAuxiliar=="Encontrado":
   print (" => "+verboAuxiliar+"</p>")

print ("<p style='margin-left: 80'>Verbo no Partic&iacute;pio: "+str(existeVerboParticipio))
if existeVerboParticipio=="Encontrado":
   print (" => "+verboParticipio+"</p>")

#print ("<br> Linha onde o Sujeito foi localizado: "+linhaSujeito+" <br>")
print ("<p style='margin-left: 80'>Sujeito localizado: "+str(sentencaAnalisada.obterSujeito)+"</p>")

print ("<p style='margin-left: 80'>Complemento Verbal localizado: "+str(sentencaAnalisada.obterComplementoVerbal)+"</p>")

print ("<p style='margin-left: 80'><strong> Nesta frase, o algoritmo selecionou como solu&ccedil;&atilde;o o antecedente => "+str(sentencaAnalisada.obterAntecedente)+" <br></strong></p>")
        

rodape()
print ("</body></html>")
sentencaAnalisada.finalizarFrase()





