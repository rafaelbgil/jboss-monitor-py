#!/usr/bin/python3
from jbossMonitor import JbossMonitor
from sys import argv

if (len(argv) < 7):
    print("Comando executado de forma incorreta, utilize o formato abaixo:")
    print("./jbossCmdApi.py UrlJboss Usuario Senha HostControlle Server opcao [argumentos]\n")
    print("Exemplo de comando para verificar informacoes do de um node")
    print('./jbossMonitorCmd.py "http://127.0.0.1:9990/management" monitor monitor@123 master servidor1 getNodeInformation\n')
    exit(1)


urlJboss=argv[1]
usuario=argv[2]
senha=argv[3]
controller=argv[4]
servidor=argv[5]
opcao=argv[6]

objetoJboss = JbossMonitor(urlJboss=urlJboss,usuarioJboss=usuario,senhaJboss=senha,hostController=controller,jbossServer=servidor)

if (opcao == "getListHostsControllers"):
    retorno=objetoJboss.getListHostsControllers()
elif(opcao == "getJvmMemoryServer"):
    retorno=objetoJboss.getJvmMemoryServer()
elif(opcao == "getListEjbPools"):
    retorno=objetoJboss.getListEjbPools()


print(retorno)