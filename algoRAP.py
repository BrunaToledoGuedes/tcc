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
#            with open('/Users/jguedes/Downloads/exported.html', 'r') as self.arq:
#            with open('d:/Users/jose.guedes/Downloads/exported.html', 'r') as self.arq:
               self.texto = self.arq.readlines()
        except IOError:
            print ("<p style='margin-left: 80'><strong>Não encontrei o arquivo exported.html</strong></p>")
            print ("                     <p style='margin-left: 80' align=""justify"">Antes de executar o algoritmo, é necessário gerar a árvore sintática da frase que se deseja resolver a anáfora pronominal. <br>Clique no item de menu Executando o Algoritmo.<p>")
            rodape()
            sys.exit(0)
          
    def obterFrase(self, fraseNumero):
        # objetivo: a função retornará a linha do arquivo exported.html 
        # que contém a frase do arquivo da árvore sintática.
        resultado = "N&atilde;o encontrado" 
        encontrou = -1
        for linha in self.texto :
            if encontrou <> -1:
               if linha.split(" ")[0] == str(fraseNumero)+"." :
                  resultado = linha
            encontrou = string.find(linha,"SOURCE: Running text")
        return resultado
          
    def obterTermo(self, tag, fraseNumero, tipo):
        # objetivo: a função retornará a linha do arquivo exported.html 
        #           que contém o termo que se quer obter.
        # parametros:
        # tag: é o parametro que contém a parte do texto que queremos 
        #            tag no arquivo exported.html
        resultado = "N&atilde;o encontrado" 
        encontrou = -1
        fraseSelecionada = 0
        linhaNivel = ' '
        linhaAnterior = ' '
        linhaNivelAnterior = ' '
        nivel = 1
        nivelAnterior = 1
        nivelLinhaAnterior = 1
        encontrouMesmoTipo = 0
        for linha in self.texto :
           if linha.split(" ")[0] == str(fraseNumero+1)+"." :
              fraseSelecionada = 0  
           if linha.split(" ")[0] == str(fraseNumero)+"." :
              fraseSelecionada = 1  
           if fraseSelecionada == 1:
              nivel = linha.find("-")  #linha.count('|')
              linhaNivel = linhaAnterior
              encontrou = string.find(linha,tag)
              if encontrou <> -1:
                 encontrouMesmoTipo = string.find(linhaNivelAnterior,tipo)
                 palavraReservada1  = string.find(linha,'pronome') 
                 if encontrouMesmoTipo <> -1 and palavraReservada1 == -1:
                    resultado = linha  
                 else:
                    encontrouMesmoTipo = string.find(linha,tipo)
                    if encontrouMesmoTipo <> -1:
                       resultado = linha  
              if nivel > nivelLinhaAnterior :
                 linhaNivelAnterior = linhaAnterior
                 nivelAnterior = nivelLinhaAnterior
              nivelLinhaAnterior = nivel
              linhaAnterior = linha
        return resultado
          
    def obterQtdeTermo(self, tag, fraseNumero, tipo):
        # objetivo: a função retornará a linha do arquivo exported.html 
        #           que contém o termo que se quer obter.
        # parametros:
        # tag: é o parametro que contém a parte do texto que queremos 
        #            tag no arquivo exported.html
        # fraseNumero é o numero da frase dentro do texto
        # tipo é o tipo do termo - sujeito, complemento, etc
        #      tipos: Adjunto  "ADVL"
        #             Sujeito  "SUBJ"
        #             ComplOD  "ACC"
        #             ComplOI  "PIV"
        #             PronomePessoal       "pp"
        #             PronomeDemonstrativo "pd"
        resultado = "N&atilde;o encontrado" 
        encontrou = -1
        qtde = 0
        fraseSelecionada = 0
        encontrouMesmoTipo = 0
        linhaNivel = ' '
        linhaAnterior = ' '
        linhaNivelAnterior = ' '
        nivel = 1
        nivelAnterior = 1
        nivelLinhaAnterior = 1
        for linha in self.texto :
           # trabalhando somente com a frase enviada como parametro
           if linha.split(" ")[0] == str(fraseNumero+1)+"." :
              fraseSelecionada = 0  
           if linha.split(" ")[0] == str(fraseNumero)+"." :
              fraseSelecionada = 1  
           if fraseSelecionada == 1:
              nivel = linha.find("-")  #linha.count('|')
              linhaNivel = linhaAnterior
              encontrou = string.find(linha,tag)
              if encontrou <> -1:
                 if tipo == "pron":
                    encontrouMesmoTipo = string.find(linha, '"ela"')
                    if encontrouMesmoTipo <> -1:
                       qtde = qtde + 1   
                    encontrouMesmoTipo = string.find(linha, '"ele"')
                    if encontrouMesmoTipo <> -1:
                       qtde = qtde + 1   
                    encontrouMesmoTipo = string.find(linha, '"seu"')
                    if encontrouMesmoTipo <> -1:
                       qtde = qtde + 1   
                    encontrouMesmoTipo = string.find(linha, '"sua"')
                    if encontrouMesmoTipo <> -1:
                       qtde = qtde + 1   
                 else:
                    encontrouMesmoTipo = string.find(linhaNivelAnterior,tipo)
                    palavraReservada1  = string.find(linha,'pronome') 
                    if encontrouMesmoTipo <> -1 and palavraReservada1 == -1:
                       qtde = qtde + 1   
                    else:
                       encontrouMesmoTipo = string.find(linha,tipo)
                       if encontrouMesmoTipo <> -1:
                          qtde = qtde + 1   
              if nivel > nivelLinhaAnterior :
                 linhaNivelAnterior = linhaAnterior
                 nivelAnterior = nivelLinhaAnterior
              nivelLinhaAnterior = nivel
              linhaAnterior = linha

        return qtde
    
    def fecharArquivo(self):
        self.arq.close()
        self.arqNomes.close()
        #renomear arquivo
        #/Users/bruna/Downloads/exported.html
        #os.remove('/Users/bruna/Downloads/_exported.html')
        #os.rename('/Users/bruna/Downloads/exported.html', '/Users/bruna/Downloads/_exported.html')		

class Corpora:
    def __init__(self):
        self.arvoreGerada = ArvoreSintatica()          
        self.calcularQtdeFrases()
    # obter numero total de frases do texto
    def calcularQtdeFrases(self):
        # objetivo: a função retornará a quantidade de frases do arquivo exported.html 
        self.quantidadeFrases = 0 
        encontrou = -1
        for linha in self.arvoreGerada.texto :
            #print(linha+"<br>")
            #print(encontrou)
            if encontrou <> -1:
               self.quantidadeFrases = self.quantidadeFrases + 1
            encontrou = string.find(linha,"SOURCE: Running text")
        return self.quantidadeFrases
class Frase:
    def __init__(self, fraseNumero):
        self.arvoreGerada = ArvoreSintatica()          
        self.conteudo = self.arvoreGerada.obterFrase(fraseNumero)   # pegando a frase da árvore sintática
        self.ambiguidade = True  # colocar formula aqui
        #self.ambiguidade = True   #criar logica para verificar se a frase tem ambiguidade
        #self.antecedente = ""   # soluçao
        #print fraseNumero
        try:
            #with open('Nomes_Proprios.txt', 'r') as self.arqNomes:
            with open('Nomes_Proprios.txt', 'r') as self.arqNomes:
               self.nomes = self.arqNomes.readlines()
        except IOError:
            print ("<p style='margin-left: 80'><strong>Não encontrei o arquivo Nomes_Proprios.txt</strong></p>")
            rodape()
            sys.exit(0)
 
    def contaTermos(self, param1, fraseNumero, param2):
        linhaSujeito = self.arvoreGerada.obterTermo(param1, fraseNumero, param2)
        s = linhaSujeito.split("\t")
        self.sujeito=s[len(s)-1]
        #sujeitosEcomplementos = self.sujeito
        result = 0
        if linhaSujeito <> "N&atilde;o encontrado" and self.nomeValido(self.sujeito) == True:
           result = 1  
        return result
     
    # obter ambiguidade
    def obterAmbiguidade(self, fraseNumero):
 
        obterQtdeSujeitoProprio       = self.contaTermos(":prop", fraseNumero, "SUBJ")
        obterQtdeSujeitoProprio1      = self.contaTermos("SUBJ:prop", fraseNumero, "SUBJ:prop")
        obterQtdeSujeitoPredicado     = self.contaTermos(":prop", fraseNumero, "P&amp;lt;")
        obterQtdeSujeito2Proprio      = self.contaTermos("SUBJ:n(", fraseNumero, "SUBJ")
        obterQtdeSujeitoSubstantivo   = self.contaTermos("H:n", fraseNumero, "SUBJ")
        obterQtdeComplODProprio       = self.contaTermos(":prop", fraseNumero, "ACC")
        obterQtdeComplODSubstantivo   = self.contaTermos("H:n", fraseNumero, "ACC")
        obterQtdeComplOD2Proprio      = self.contaTermos(":prop", fraseNumero, ":pp")
        obterQtdeComplOD2Substantivo  = self.contaTermos("H:n", fraseNumero, "PASS:pp")
        obterQtdeComplOD3Proprio      = self.contaTermos("N&amp;lt;:prop", fraseNumero, "N&amp;lt;:prop")
        obterQtdeComplOIProprio       = self.contaTermos(":prop", fraseNumero, "PIV")
        obterQtdeComplOISubstantivo   = self.contaTermos("H:n", fraseNumero, "PIV")
        obterQtdeComplAdverbio        = self.contaTermos("H:n", fraseNumero, "P&amp;lt;")
        obterQtdePronomePessoal       = 0
        obterQtdePronomeDemonstrativo = 0

        obterQtdePronomePessoal       = self.arvoreGerada.obterQtdeTermo("pers", fraseNumero, "pron")
        obterQtdePronomeDemonstrativo = self.arvoreGerada.obterQtdeTermo("det", fraseNumero, "pron")
        obterQtdeSujeito = obterQtdeSujeitoProprio1 + obterQtdeComplAdverbio + obterQtdeComplOIProprio + obterQtdeComplOD3Proprio + obterQtdeSujeito2Proprio + obterQtdeSujeitoPredicado + obterQtdeComplOD2Proprio + obterQtdeComplOD2Substantivo + obterQtdeSujeitoProprio + obterQtdeSujeitoSubstantivo + obterQtdeComplODProprio + obterQtdeComplODSubstantivo + obterQtdeComplOISubstantivo
        obterQtdePronome = obterQtdePronomePessoal + obterQtdePronomeDemonstrativo
        print ("obterQtdeSujeitoPredicado")
        print obterQtdeSujeitoPredicado
        print "<br>"
        print ("obterQtdeSujeitoProprio")
        print obterQtdeSujeitoProprio
        print "<br>"
        print ("obterQtdeSujeito2Proprio")
        print obterQtdeSujeito2Proprio
        print "<br>"
        print ("obterQtdeSujeitoSubstantivo")
        print obterQtdeSujeitoSubstantivo
        print "<br>"
        print ("obterQtdeComplODProprio")
        print obterQtdeComplODProprio
        print "<br>"
        print ("obterQtdeComplODSubstantivo")
        print obterQtdeComplODSubstantivo
        print "<br>"
        print ("obterQtdeComplOD2Proprio")
        print obterQtdeComplOD2Proprio
        print "<br>"
        print ("obterQtdeComplOD2Substantivo")
        print obterQtdeComplOD2Substantivo
        print "<br>"
        print ("obterQtdeComplOD3Proprio")
        print obterQtdeComplOD3Proprio
        print "<br>"
        print ("obterQtdeComplOIProprio")
        print obterQtdeComplOIProprio
        print "<br>"
        print ("obterQtdeComplOISubstantivo")
        print obterQtdeComplOISubstantivo
        print "<br>"
        print ("obterQtdeComplAdverbio")
        print obterQtdeComplAdverbio
        print "<br>"
        print ("obterQtdeSujeito")
        print obterQtdeSujeito
        print "<br>"
        print ("obterQtdePronome")
        print obterQtdePronome
        print "---------------------------------------------------------------------------------"
        if obterQtdeSujeito > 1 and obterQtdePronome > 0:
           self.ambiguidade = True
        else:
           self.ambiguidade = False
           
        return self.ambiguidade

    # obter antecedente
    def obterAntecedente(self, fraseNumero):
        # analisar    obterVerboAuxiliar = arvoreGerada.obterTermo("-VAUX:v*fin")
        #s = obterVerboAuxiliar.split("\t")
        self.antecedente = " "
        self.termoSelecionado = " "
        if (self.verboAuxiliar=="N&atilde;o encontrado" or self.verboParticipio == "N&atilde;o encontrado") :
           self.antecedente = self.obterComplementoVerbal(fraseNumero)
           self.termoSelecionado = "Complemento Verbal"
        else:
           self.antecedente = self.obterSujeito(fraseNumero)
           self.termoSelecionado = "Sujeito"
        return self.antecedente
          
    # obter o verbo auxiliar
    def obterVerboAuxiliar(self, fraseNumero):
        obterVerboAuxiliar = self.arvoreGerada.obterTermo("-VAUX:v*fin", fraseNumero,"-VAUX:v*fin")
        s = obterVerboAuxiliar.split("\t")
        self.verboAuxiliar=s[len(s)-1]
        if obterVerboAuxiliar == "N&atilde;o encontrado":
           obterVerboAuxiliar = self.arvoreGerada.obterTermo("-P:v*fin", fraseNumero, "-P:v*fin")
           s = obterVerboAuxiliar.split("\t")
           self.verboAuxiliar=s[len(s)-1]
        return self.verboAuxiliar
        
    # obter o verbo no particípio
    def obterVerboParticipio(self, fraseNumero):
        obterVerboParticipio = self.arvoreGerada.obterTermo("-MV:v*pcp", fraseNumero, "-MV:v*pcp")
        s = obterVerboParticipio.split("\t") 
        self.verboParticipio=s[len(s)-1] 
        return self.verboParticipio

    # obter o sujeito
    def obterSujeito(self, fraseNumero):
        linhaSujeito = self.arvoreGerada.obterTermo(":prop", fraseNumero, "SUBJ")
        s = linhaSujeito.split("\t")
        self.sujeito=s[len(s)-1]
        if linhaSujeito == "N&atilde;o encontrado" or self.nomeValido(self.sujeito) == False:
           linhaSujeito = self.arvoreGerada.obterTermo("SUBJ:prop", fraseNumero, "SUBJ:prop")
           s = linhaSujeito.split("\t")
           self.sujeito=s[len(s)-1]
           if linhaSujeito <> "N&atilde;o encontrado" or self.nomeValido(self.sujeito) == False:
              linhaSujeito = self.arvoreGerada.obterTermo("SUBJ:n(", fraseNumero, "SUBJ")
              s = linhaSujeito.split("\t")
              self.sujeito=s[len(s)-1]
              if linhaSujeito == "N&atilde;o encontrado" or self.nomeValido(self.sujeito) == False:
                 linhaSujeito = self.arvoreGerada.obterTermo("H:n", fraseNumero, "SUBJ")
                 s = linhaSujeito.split("\t")
                 self.sujeito=s[len(s)-1]
                 if linhaSujeito == "N&atilde;o encontrado" or self.nomeValido(self.sujeito) == False:
                    linhaSujeito = self.arvoreGerada.obterTermo(":prop", fraseNumero, "P&amp;lt;")
                    s = linhaSujeito.split("\t")
                    self.sujeito=s[len(s)-1]
                    if self.nomeValido(self.sujeito) == False:
                       self.sujeito = "N&atilde;o encontrado"

        return self.sujeito
          
    # obter o complemento verbal
    def obterComplementoVerbal(self, fraseNumero):
        linhaCompl = self.arvoreGerada.obterTermo(":prop", fraseNumero, "ACC")
        s = linhaCompl.split("\t")
        self.complementoVerbal=s[len(s)-1]
        #if self.nomeValido(self.complementoVerbal) == False:
        #to do :  
        #1) colocar todos os ifs iguais a esse da linha abaixo
        #2) montar rotina para ler um arquivo texto com todas as palavras que podem representar nome proprio
        #3) procurar um texto adequado para realizar testes

        if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
           linhaCompl = self.arvoreGerada.obterTermo(":prop", fraseNumero, "ACC")
           s = linhaCompl.split("\t")
           self.complementoVerbal=s[len(s)-1]
           if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
              linhaCompl = self.arvoreGerada.obterTermo("H:n", fraseNumero, "ACC")
              s = linhaCompl.split("\t")
              self.complementoVerbal=s[len(s)-1]
              if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                 linhaCompl = self.arvoreGerada.obterTermo(":prop", fraseNumero, ":pp")
                 s = linhaCompl.split("\t")
                 self.complementoVerbal=s[len(s)-1]
                 if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                    linhaCompl = self.arvoreGerada.obterTermo("H:n", fraseNumero, "PASS:pp")
                    s = linhaCompl.split("\t")
                    self.complementoVerbal=s[len(s)-1]
                    if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                       linhaCompl = self.arvoreGerada.obterTermo(":prop", fraseNumero, "PIV")
                       s = linhaCompl.split("\t")
                       self.complementoVerbal=s[len(s)-1]
                       if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                          linhaCompl = self.arvoreGerada.obterTermo("H:n", fraseNumero, "PIV")
                          s = linhaCompl.split("\t")
                          self.complementoVerbal=s[len(s)-1]
                          if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                             linhaCompl = self.arvoreGerada.obterTermo("N&amp;lt;:prop", fraseNumero, "N&amp;lt;:prop")
                             s = linhaCompl.split("\t")
                             self.complementoVerbal=s[len(s)-1]
                             if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                                linhaCompl = self.arvoreGerada.obterTermo("H:n", fraseNumero, "P&amp;lt;")
                                s = linhaCompl.split("\t")
                                self.complementoVerbal=s[len(s)-1]
                                if linhaCompl == "N&atilde;o encontrado" or self.nomeValido(self.complementoVerbal) == False:
                                   linhaCompl = self.arvoreGerada.obterTermo("P&amp;lt;:prop", fraseNumero, "PIV")
                                   s = linhaCompl.split("\t")
                                   self.complementoVerbal=s[len(s)-1]
                                   if self.nomeValido(self.complementoVerbal) == False:
                                      self.complementoVerbal = "N&atilde;o encontrado"
        return self.complementoVerbal

    def nomeValido(self, texto):
        resultado = True
        if texto.lower() == texto:
           resultado = False
        if sentencaAnalisada.nomesProprios(texto) == True:
           resultado = True
        return resultado
        
    def nomesProprios(self, nome):
        retorno = False
        
        for linhaN in self.nomes :
            resultado = string.find(linhaN.lower(),nome.lower()) 
            if resultado <> -1:
               retorno = True
        return retorno

    def finalizarFrase(self):
        self.arvoreGerada.fecharArquivo()

# Main
# abrindo o arquivo que contém a árvore sintática da frase
# o arquivo for gerado através do link http://visl.sdu.dk/visl/pt/parsing/automatic/trees.php

# imprimindo cabeçalhos
cabecalho()
corpora = Corpora()

print ("<p><strong>Ambiguidades encontradas no texto serão marcadas em vermelho</strong></p>")
for counter in range(1,corpora.quantidadeFrases+1):
    #print counter
    sentencaAnalisada = Frase(counter)
    #print sentencaAnalisada.obterAmbiguidade(counter)
    if sentencaAnalisada.obterAmbiguidade(counter) == True:
       print ("<br><p style='background-color: #ff0000; color: #fff'>"+sentencaAnalisada.conteudo+"</p>")
    else:
       print ("<br><p >"+sentencaAnalisada.conteudo+"</p>")
for counter in range(1,corpora.quantidadeFrases+1):
    if sentencaAnalisada.obterAmbiguidade(counter) == True:
       sentencaAnalisada = Frase(counter)
       # mostrar resultados em tela
       existeVerboAuxiliar = "N&atilde;o encontrado"
       if sentencaAnalisada.obterVerboAuxiliar(counter) <> "N&atilde;o encontrado":
          existeVerboAuxiliar = "Encontrado"
       existeVerboParticipio = "N&atilde;o encontrado"
       if sentencaAnalisada.obterVerboParticipio(counter) <> "N&atilde;o encontrado":
          existeVerboParticipio = "Encontrado"
       print ("<br><p style='margin-left: 80'><strong> Frase em An&aacute;lise: "+sentencaAnalisada.conteudo+"</strong></p>")
       sentencaAnalisada.obterAntecedente(counter)
       print ("<p style='margin-left: 80'>Verbo Auxiliar: "+str(existeVerboAuxiliar))   
       if existeVerboAuxiliar=="Encontrado":
          print (" => "+sentencaAnalisada.verboAuxiliar+"</p>")
       print ("<p style='margin-left: 80'>Verbo no Partic&iacute;pio: "+str(existeVerboParticipio))
       if existeVerboParticipio=="Encontrado":
          print (" => "+sentencaAnalisada.verboParticipio+"</p>")
       if sentencaAnalisada.termoSelecionado == "Sujeito" :
          sentencaAnalisada.obterSujeito(counter)
          #print ("<br> Linha onde o Sujeito foi localizado: "+linhaSujeito+" <br>")
          print ("<p style='margin-left: 80'>Sujeito localizado: "+sentencaAnalisada.sujeito+"</p>")
       else:
          sentencaAnalisada.obterComplementoVerbal(counter)
          print ("<p style='margin-left: 80'>Complemento Verbal localizado: "+sentencaAnalisada.complementoVerbal+"</p>")
       if sentencaAnalisada.antecedente == "N&atilde;o encontrado":
          print ("<p style='margin-left: 80'><strong> Entendo que a solu&ccedil;&atilde;o seria o " +sentencaAnalisada.termoSelecionado+ ", mas não fui capaz de identificá-lo para resolver a ambiguidade <br></strong></p>")
       else:
          print ("<p style='margin-left: 80'><strong> Escolhi como solu&ccedil;&atilde;o para o antecedente o " +sentencaAnalisada.termoSelecionado+ " => "+sentencaAnalisada.antecedente+" <br></strong></p>")
    #else:
    #   print "<br> Frase não possui ambiguidade anaforica pronominal <br>"
   
rodape()
print ("</body></html>")
sentencaAnalisada.finalizarFrase()

