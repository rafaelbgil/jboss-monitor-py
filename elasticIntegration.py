from elasticsearch import Elasticsearch

class ElasticMonitor:
    def __init__(self,elasticUrl,elasticIndex):
        self.elasticUrl=elasticUrl
        self.elasticIndex=elasticIndex
        self.elasticObject = Elasticsearch(self.elasticUrl)
        self.docType="doc"
        
    def adicionarDocumento(self,objeto,id=None):
        if (self.elasticObject.index(self.elasticIndex, doc_type=self.docType, body=objeto, id=None)):
            print("Objeto adicionado com sucesso no indice")
            return True
        else:
            print("Nao foi possivel adicionar o documento")
            return False

        
    def listarIndice(self):
        print(self.elasticObject.cat.indices(self.elasticIndex))
        return True
        