class Node:
    def __init__(self,data):
        self.data = data
        #Cuando digo qué self.next = proximo None , en la verdad no estoy criando nuevo objeto pero si
        #referenciar el mismo en la memoria , es decir solo tengo su referencia guardado .
        self.next = None

    def __str__(self):
        return str(self.data)