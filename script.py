
class Catalog:
    """Define o modelo catalogo"""

    def __init__(self, title, products, is_active):
        self.title = title
        self.products = products
        self.is_active = is_active


    def __eq__(self, obj):
        return isinstance(
            obj, Catalog
        ) and obj.title == self.title and obj.products == self.products and obj.is_active == self.is_active


    def __str__(self):
        return super().__str__()

    
    def remove_product(self, index):
        del self.products[index]

    def add_new_product(self, product):
        self.products.append(product)

    def uṕdate_product(self, index, updated_product):
        self.products[index] = updated_product


class Product:
    """Define o modelo dos produtos que vão no catalogo"""

    def __init__(self, title, description, price, stock, is_available = True):
        self.title = title
        self.description = description
        self.price = price
        self.stock = stock 
        self.is_available = is_available

    def set_availability_status(self):
        self.is_available = False

        
    def __repr__(self):
        return self.title

    def __str__(self):
        return f'{self.title}, {self.price}'


    


def main():
    """Ponto de entrada do aplicativo"""

    produtos = [Product('Mesa', 'Uma bela mesa', 250, 10),Product('Mesa', 'Uma bela mesa', 250, 10), Product('Cadeira', 'Uma cadeira sentavel', 50.50, 10),Product('Guarda-roupas', 'Um guarda-roupas, de por roupas, se quiser', 1500, 10) ]



    catalogo = Catalog('Um catalogo', produtos, True)

    catalogo.add_new_product(Product('Quadro', 'Formulas tops', 99, 1, True))

    catalogo.uṕdate_product(1, Product('Mesa em L', 'Muito boa inclusive recomendo', 450, 1, True))
    

    print(catalogo.products)


if __name__ == "__main__":
    main()