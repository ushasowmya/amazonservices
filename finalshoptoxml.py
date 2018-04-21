import json
import simplejson as json
import os

import simplejson as json
import urllib.request as urllib2

import lxml.etree 

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
f1 =open('price1.xml','w')
f1.write('<?xml version="1.0" encoding="utf-8"?>\n'
		'\t<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
		'xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">\n'

              '<Header>\n'

                             '<DocumentVersion>1.01</DocumentVersion>\n'

                            '<MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>\n'

  '</Header>\n'
  '<MessageType>Price</MessageType>\n')
f2 =open('image1.xml','w')
f2.write('<?xml version="1.0" encoding="utf-8"?>\n'
		'\t<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
		'xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">\n'

              '<Header>\n'

                             '<DocumentVersion>1.01</DocumentVersion>\n'

                            '<MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>\n'

  '</Header>\n'
  '<MessageType>ProductImage</MessageType>\n')
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
	p = urllib2.HTTPPasswordMgrWithDefaultRealm()

	p.add_password(None, url, username, password)

	handler = urllib2.HTTPBasicAuthHandler(p)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)

	
	#print(url)
	collectspage = urllib2.urlopen(url).read()
	collectsload = json.loads(collectspage)
	collectsdump = json.dumps(collectsload, sort_keys=True, indent=4)
	#id = 1
	for j in range (len(collectsload["collects"])):
		product_id = collectsload["collects"][j]["product_id"]
		print(product_id)
		url1 = 'https://weavesmart-com.myshopify.com/admin/products/%s.json'%product_id
		username = 'fd69d4dcab33a3c382c2ebec9d51c324'
		password = '2bf4f50b42266b527e9c875bc421afe0'
		p = urllib2.HTTPPasswordMgrWithDefaultRealm()

		p.add_password(None, url1, username, password)

		handler = urllib2.HTTPBasicAuthHandler(p)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)

		productpage = urllib2.urlopen(url1).read()
		productload = json.loads(productpage)
		
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

  </Message>
"""% (id,Sku,Title,Sku,Item_type,Color,Color,Style_Name,Item_type)
		
			price_xml ="""
			<Message>
        <MessageID>%s</MessageID>
        <Price>
            <SKU>%s</SKU>
            <StandardPrice currency="USD">%s</StandardPrice>
        </Price>
    </Message>
"""%(id,Sku,Price)

			image_xml = """
			<Message>
<MessageID>%s</MessageID>
<OperationType>Update</OperationType>
<ProductImage>
<SKU>%s</SKU>
<ImageType>Main</ImageType><ImageLocation>%s</ImageLocation>


</ProductImage>
</Message>
</AmazonEnvelope>
"""%(id,Sku,Image1)
			print("ok")
			product_xml = "" +"\n"+ product_xml
			f.write(product_xml)
			price_xml = "" +"\n"+ price_xml
			f1.write(price_xml)
			image_xml = "" +"\n"+ image_xml
			f2.write(image_xml)
			id = id + 1
			
			
print("ok2")	
f.write('\n</AmazonEnvelope>')
f1.write('\n</AmazonEnvelope>')
f2.write('\n</AmazonEnvelope>')
print("ok3")
