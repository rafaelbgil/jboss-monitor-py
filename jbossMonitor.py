from requests.auth import HTTPDigestAuth
import requests 
import json

class JbossMonitor:
    def __init__(self,urlJboss,usuarioJboss,senhaJboss):
        self.urlJboss = urlJboss
        self.usuarioJboss = usuarioJboss
        self.usuarioSenha = senhaJboss
                
    #Default method to consume manager api
    def callJbossApi(self,payload):
        #Url for manager interface and api jboss EAP 7 or Wildfly 10
        urlApi = self.urlJboss 
        #Authentication information about administrative interface and api
        jbossUser=self.usuarioJboss
        jbossPassword=self.usuarioSenha
        return (requests.post(urlApi,auth=HTTPDigestAuth(jbossUser,jbossPassword),json=payload))
    
    
    #general informations
    def getListHostsControllers(self):
        payload = {"operation" : "read-children-names", "child-type" : "host", "address" : []}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getJvmMemoryServer(self,jbossHostController,jbossServer):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "core-service" : "platform-mbean" },{ "type" : "memory" }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    #ejb informations
    def getListEjbPools(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "thread-pool", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "ejb3" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getEjbPoolInformations(self,poolEjb,jbossHostController,jbossServer):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "ejb3" },{ "thread-pool" : poolEjb }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getEjbInformations(self,jbossHostController,jbossServer):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "ejb3" }], "operation" : "read-resource", "include-runtime" : "true", "recursive" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    #Datasource informations
    def getListDatasources(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "data-source", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getJdbcDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "data-source" : datasource },{ "statistics" : "jdbc" }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getPoolDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "data-source" : datasource },{ "statistics" : "pool" }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    #XA Datasource informations 
    def getListXaDatasources(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "xa-data-source", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getJdbcXaDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "xa-data-source" : datasource },{ "statistics" : "jdbc" }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getPoolXaDatasourceStatistics(self,jbossHostController,jbossServer,datasource):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "datasources" },{ "xa-data-source" : datasource },{ "statistics" : "pool" }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    # Queue and Topic informations
    
    def getListQueues(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "jms-queue", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getListTopics(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "jms-topic", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getQueueInformations(self,jbossHostController,jbossServer,queue):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" },{ "jms-queue" : queue }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getTopicInformations(self,jbossHostController,jbossServer,topic):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "messaging-activemq" },{ "server" : "default" },{ "jms-topic" : topic }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    #Undertow http/https information
    #http listener
    def getListHttpListener(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "http-listener", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getHttpListenerInformations(self,jbossHostController,jbossServer,httpListener):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" },{ "http-listener" : httpListener }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    #https listener
    def getListHttpsListener(self,jbossHostController,jbossServer):
        payload = {"operation" : "read-children-names", "child-type" : "https-listener", "address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" }]}
        return json.loads(self.callJbossApi(payload=payload).text)
    
    def getHttpsListenerInformations(self,jbossHostController,jbossServer,httpsListener):
        payload = {"address" : [{ "host" : jbossHostController },{ "server" : jbossServer },{ "subsystem" : "undertow" },{ "server" : "default-server" },{ "https-listener" : httpsListener }], "operation" : "read-resource", "include-runtime" : "true"}
        return json.loads(self.callJbossApi(payload=payload).text)