# profit and loss

costprice =  int(input("Enter Cost Price :"))
sellingprice =  int(input("Enter Selling Price :"))

if sellingprice > costprice :
    print("The seller has made profit of :",sellingprice -  costprice);
elif sellingprice < costprice :
    print("The seller has made a loss of :",costprice - sellingprice)
elif sellingprice == costprice :
    print("THe seller didn't make ant profit or loss")