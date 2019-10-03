from requests.auth import HTTPDigestAuth
import requests 
import json

class JbossMonitor:
    def __init__(self,urlJboss,usuarioJboss,senhaJboss,hostController=None,jbossServer=None):
        self.urlJboss = urlJboss
        self.usuarioJboss = usuarioJboss
        self.usuarioSenha = senhaJboss
        self.hostController= hostController
        self.jbossServer = jbossServer
                
    #Default method to consume manager api
    def callJbossApi(self,payload):
        #Url for manager interface and api jboss EAP 7 or Wildfly 10
        urlApi = self.urlJboss 
        #Authentication information about administrative interface and api
        jbossUser=self.usuarioJboss
        jbossPassword=self.usuarioSenha
        
        retornoRequest=requests.post(urlApi,auth=HTTPDigestAuth(jbossUser,jbossPassword),json=payload)
        retornoRequestJson= json.loads(retornoRequest.text)
        

        
        if (retornoRequestJson['outcome'] == 'success'):
            return(retornoRequestJson['result'])
        else:
            return(False)
        
    
    #general informations
    def getListHostsControllers(self):
        payload = {"operation" : "read-children-names", "child-type" : "host", "address" : []}
        return self.callJbossApi(payload=payload)
    
    def getJvmMemoryServer(self,jbossHostController=None,jbossServer=None):
        payload = {"address" : [{ "host" : self.hostController},{ "server" : self.jbossServer },{ "core-service" : "platform-mbean" },{ "type" : "memory" }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    #ejb informations
    def getListEjbPools(self,jbossHostController=None,jbossServer=None):
        payload = {"operation" : "read-children-names", "child-type" : "thread-pool", "address" : [{ "host" : self.hostController },{ "server" : self.jbossServer },{ "subsystem" : "ejb3" }]}
        return self.callJbossApi(payload=payload)
    
    def getEjbPoolInformations(self,poolEjb,jbossHostController,jbossServer):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "ejb3" },{ "thread-pool" : poolEjb }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    def getEjbInformations(self,jbossHostController,jbossServer):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "ejb3" }], "operation" : "read-resource", "include-runtime" : "true", "recursive" : "true"}
        return self.callJbossApi(payload=payload)
    
    #Datasource informations
    def getListDatasources(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "data-source", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" }]}
        return self.callJbossApi(payload=payload)
    
    def getJdbcDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "data-source" : datasource },{ "statistics" : "jdbc" }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    def getPoolDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "data-source" : datasource },{ "statistics" : "pool" }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    #XA Datasource informations 
    def getListXaDatasources(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "xa-data-source", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" }]}
        return self.callJbossApi(payload=payload)
    
    def getJdbcXaDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "xa-data-source" : datasource },{ "statistics" : "jdbc" }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    def getPoolXaDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "xa-data-source" : datasource },{ "statistics" : "pool" }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    # Queue and Topic informations
    
    def getListQueues(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "jms-queue", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" }]}
        return self.callJbossApi(payload=payload)
    
    def getListTopics(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "jms-topic", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" }]}
        return self.callJbossApi(payload=payload)
    
    def getQueueInformations(self,jbossHostController,jbossServer,queue):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" },{ "jms-queue" : queue }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    def getTopicInformations(self,jbossHostController,jbossServer,topic):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" },{ "jms-topic" : topic }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    #Undertow http/https information
    #http listener
    def getListHttpListener(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "http-listener", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" }]}
        return self.callJbossApi(payload=payload)
    
    def getHttpListenerInformations(self,jbossHostController,jbossServer,httpListener):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" },{ "http-listener" : httpListener }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)
    
    #https listener
    def getListHttpsListener(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "https-listener", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" }]}
        return self.callJbossApi(payload=payload)
    
    def getHttpsListenerInformations(self,jbossHostController,jbossServer,httpsListener):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" },{ "https-listener" : httpsListener }], "operation" : "read-resource", "include-runtime" : "true"}
        return self.callJbossApi(payload=payload)