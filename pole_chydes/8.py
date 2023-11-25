def compares_content(sold_product, left_product):
    try:
        with open(sold_product, 'r') as sold, open(left_product, 'r') as left:
            sold_content = sold.readlines()
            left_content = left.readlines()

            for line in sold_content:
                if line not in left_content:
                    print(f"Strin thet is in '{sold_product}', but not in '{left_product}': ")
                    print(line.strip())

            for line in left_content:
                if line not in sold_content:
                    print(f"Strin thet is in '{left_product}', but not in '{sold_product}': ")
                    print(line.strip())


    except FileNotFoundError as e :
        print(f"error: {e}")
    except Exception as e:
        print(f"error occurred: {e}")

compares_content("sold_product.txt" , "left_product.txt")




