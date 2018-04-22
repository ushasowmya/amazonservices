#Please use python3 to execute this code

import json
import requests
#import lxml.etree

# function definitions
def update_product_xml(id, Sku, Title,  Color, Style_Name, Item_type):

	f = open('product1.xml', 'a')

	product_xml = """
		<Message>
	        <MessageID>%s</MessageID>
		    <OperationType>Update</OperationType>
		    <Product>
				<SKU>%s</SKU>
				<ProductTaxCode>A_GEN_NOTAX</ProductTaxCode>
				<DescriptionData>
					<Title>%s</Title>
					<Brand>Weavesmart</Brand>
					<Description>Excellent quality of products</Description>
					<BulletPoint>Nice fabric</BulletPoint>
					<BulletPoint>good quality and Colors</BulletPoint>
					<Manufacturer>Weavesmart</Manufacturer>
					<MfrPartNumber>%s</MfrPartNumber>
					<ItemType>%s</ItemType>
				</DescriptionData>
				<ProductData>
					<Clothing>
						<VariationData>
							<Size>Free Size</Size>
							<Color>%s</Color>
						</VariationData>
						<ClassificationData>
						    <ClothingType>EthnicWear</ClothingType>
						    <Department>Women</Department>
						    <ColorMap>%s</ColorMap>
						    <StyleName>%s</StyleName>
						    <SizeMap>Free Size</SizeMap>
						    <MaterialType>%s</MaterialType>
						    <CollectionDescription>Traditional</CollectionDescription>
						</ClassificationData>
					</Clothing>
				</ProductData>
			</Product>
		</Message>""" % (id, Sku, Title, Sku, Item_type, Color, Color, Style_Name, Item_type)
	product_xml = "" + "\n" + product_xml
	f.write(product_xml)
	f.close()



def update_image_xml(id,Sku,Image1):

	f2 = open('image1.xml', 'a')
	image_xml = """
    	<Message>
            <MessageID>%s</MessageID>
            <OperationType>Update</OperationType>
            <ProductImage>
                <SKU>%s</SKU>
                <ImageType>Main</ImageType><ImageLocation>%s</ImageLocation>
            </ProductImage>
        </Message>
    """ % (id, Sku, Image1)
	image_xml = "" + "\n" + image_xml
	f2.write(image_xml)
	f2.close()


def update_price_xml(id,Sku,Price):
    price_xml = """
        <Message>
            <MessageID>%s</MessageID>
            <Price>
                <SKU>%s</SKU>
                <StandardPrice currency="USD">%s</StandardPrice>
            </Price>
        </Message>""" % (id, Sku, Price)

    f1=open("price1.xml","a")
    price_xml = "" + "\n" + price_xml
    f1.write(price_xml)
    f1.close()


# main program starts here

#Creating xml files
f = open('product1.xml', 'w')
f.write('<?xml version="1.0" encoding="utf-8"?>\n'
		'\t<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
		'xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">\n'

            '<Header>\n'

                    '<DocumentVersion>1.01</DocumentVersion>\n'

                    '<MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>\n'

             '</Header>\n'

             '<MessageType>Product</MessageType>\n'

            '<PurgeAndReplace>false</PurgeAndReplace>\n')
f.close()

f1 =open('price1.xml','w')
f1.write('<?xml version="1.0" encoding="utf-8"?>\n'
		'\t<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
		'xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">\n'

              '<Header>\n'

                    '<DocumentVersion>1.01</DocumentVersion>\n'

                    '<MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>\n'

              '</Header>\n'
        '<MessageType>Price</MessageType>\n')
f1.close()

f2 =open('image1.xml','w')
f2.write('<?xml version="1.0" encoding="utf-8"?>\n'
		'\t<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
		'xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">\n'

              '<Header>\n'

                  '<DocumentVersion>1.01</DocumentVersion>\n'

                      '<MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>\n'

              '</Header>\n'
        '<MessageType>ProductImage</MessageType>\n')
f2.close()


#CollectionId =input('Enter Collection Id : \n')
CollectionId ="58351108"
#CollectionId = ['58351108','78165572',423120392']
#for r in range(len(CollectionId)):
id =1
for i in range(1,6):
	print("for")
	url = 'https://weavesmart-com.myshopify.com/admin/collects.json?collection_id=%s&fields=product_id&limit=250&page=%s'%(CollectionId,i)
	#url = 'https://weavesmart-com.myshopify.com/admin/collects.json?collection_id=%s&fields=product_id&limit=250&page=%s'%(r,i)
	username = 'fd69d4dcab33a3c382c2ebec9d51c324'
	password = '2bf4f50b42266b527e9c875bc421afe0'

	r = requests.get(url, auth=(username, password))

	print(str(r.text))
	collectsload = json.loads(str(r.text))

    #id = 1
	for j in range (len(collectsload["collects"])):
		product_id = collectsload["collects"][j]["product_id"]
		print(product_id)
		url1 = 'https://weavesmart-com.myshopify.com/admin/products/%s.json'%product_id
		username = 'fd69d4dcab33a3c382c2ebec9d51c324'
		password = '2bf4f50b42266b527e9c875bc421afe0'

		r = requests.get(url1, auth=(username, password))
		print(str(r.text))
		productload = json.loads(str(r.text))

		#sku = productload['product']['variants'][0]['sku']
		#Skuc =sku[0:3]
		#print(Skuc)
		
		#if Skuc == 'wps'

		if productload['product']['variants'][0]['inventory_quantity'] == 1:

			Sku = productload['product']['variants'][0]['sku']
			print(Sku)
			
			Title = productload['product']['product_type']
			print(Title)
			
			Tags = productload['product']['tags']
			print(Tags)
			
			Types =[ 'cotton', 'silk','sico']
			for t in Types:
				if t in Tags:
					Item_type = t
			print(Item_type)
			
			colrs =['red-colour', 'green-colour','sky-blue-colour','grey-colour','purple-colour','orange-colour','blue-colour','peach-colour','cream-colour','white-colour','mustartd-colour','brown-colour','black-colour','yellow-colour','pink-colour','multi-colour']
			for c in colrs:
				if c in Tags:
					Color = c.replace('-colour', '')
					if Color == 'multi':
						Color = 'multi coloured' 
						print(Color)
			
			Styles =[ 'saree', 'dress-material']
			for s in Styles:
				if s in Tags:
					Style_Name = s
			print(Style_Name)
			
			Price = productload['product']['variants'][0]['price']
			print(Price)
			
			Image1 = productload['product']['images'][0]['src']
			#Image2 = productload['product']['images'][1]['src']
			#Image3 = productload['product']['images'][2]['src']
			#Image4 = productload['product']['images'][3]['src']

			print("ok")
			update_product_xml(id, Sku, Title,  Color, Style_Name, Item_type)
			update_price_xml(id,Sku,Price)
			update_image_xml(id,Sku,Image1)

			id = id + 1
			
			
print("ok2")	
f.write('\n</AmazonEnvelope>')
f1.write('\n</AmazonEnvelope>')
f2.write('\n</AmazonEnvelope>')
print("ok3")
