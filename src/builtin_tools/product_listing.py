class ProductListingTool:
    """
    A class used to represent a Product Listing Tool.
    Handles operations related to listing products in the ecommerce platform.
    """

    def __init__(self, product_data):
        """
        Initializes the ProductListingTool with product data.
        :param product_data: List of products to be managed.
        """
        self.product_data = product_data

    def list_products(self):
        """
        Lists all the products in the product data.
        """
        return self.product_data

    def add_product(self, product):
        """
        Adds a new product to the product data.
        :param product: The product to be added.
        """
        self.product_data.append(product)

    def remove_product(self, product_id):
        """
        Removes a product from the product data using its ID.
        :param product_id: The ID of the product to remove.
        """
        self.product_data = [product for product in self.product_data if product['id'] != product_id]

    def update_product(self, product_id, updated_product):
        """
        Updates the details of a product based on the product ID.
        :param product_id: The ID of the product to update.
        :param updated_product: Dictionary containing updated product details.
        """
        for index, product in enumerate(self.product_data):
            if product['id'] == product_id:
                self.product_data[index] = updated_product
                break
