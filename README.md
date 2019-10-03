<h1>Jboss Monitor Python</h1>

<p><b>Descrição:</b> Biblioteca desenvolvida em python para consumir a API do Jboss EAP / Wildfly e obter informações de monitoramento. Essa biblioteca server como uma alternativa ao monitoramento do jboss via jboss-cli que ao ser executado por ser baseado em java cria uma nova jvm para processar a requisição e também demora a retorna as inforamações </p>
<p>Essa lib ainda está em desenvolvimento beta e pode sofrer alterção em suas implementações de métodos.</p>

<h2>Requisitos</h2>
<ul>
  <li>Python3 ou superior</li>
  <li>Lib requests</li>
</ul>
  

<h2>Compatibilidade</h2>
<p>Está biblioteca é compatível com as versões informadas abaixo:</p>
<ul>
  <li>Red Hat JBoss Enterprise Application Platform 7 ou superior.</li>
  <li>Wildfly 10 ou superior.</li>
  <li>Modo de execução: <b>Domain</b> . Essa biblioteca suporte somente o modo domain.</li>
 </ul>
 
 <h2>Instalação</h2>
 <p>Clone o repositório para seu ambiente e import a biblioteca para seu projeto.</p>
        
        $ git clone https://github.com/rafaelbgil/jboss-monitor-py.git
 
 <h2>Tutorial de inicio rápido</h2>
       
       $ python3
       >>> from jbossMonitor import JbossMonitor
       >>> objetoJbossMonitor =  JbossMonitor(urlJboss='http://127.0.0.1:9200/management', usuarioJboss='usuario', senhaJboss='senha', hostController='host_controller', jbossServer='servidor')
       >>> print(objetoJbossMonitor.objetoJboss.getJvmMemoryServer()) # obtem o uso de memória da jvm e exibe na tela.
  
