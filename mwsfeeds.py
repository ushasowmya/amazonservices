import mws

access_key = 'AKIAJNW2GEYO2PX2PQUQ'  # replace with your access key
merchant_id = 'A3EM5T09FVM4CD'  # replace with your merchant id
secret_key = 'UpmT6tAHn2ZD1Co+ixQwPMocGLrEgsl+nUwFjAyq'  # replace with your secret key
# reportid = '123456' #replace with report id

feed = """<?xml version="1.0" encoding="utf-8"?>

<AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

    xsi:noNamespaceSchemaLocation="amzn-envelope.xsd">

              <Header>

                             <DocumentVersion>1.01</DocumentVersion>

                            <MerchantIdentifier>A3EM5T09FVM4CD</MerchantIdentifier>

  </Header>

  <MessageType>Product</MessageType>

  <PurgeAndReplace>false</PurgeAndReplace>

  <Message>

    <MessageID>1</MessageID>

    <OperationType>Update</OperationType>

    <Product>

      <SKU>gdl0500</SKU>



      <ProductTaxCode>A_GEN_NOTAX</ProductTaxCode>

                <DescriptionData>

        <Title>Gadwal Dress Material</Title>

                             <Brand>Weavesmart</Brand>

        <Description>Excellent quality of products</Description>

        <BulletPoint>Nice fabric</BulletPoint>

        <BulletPoint>good quality and Colors</BulletPoint>

               <Manufacturer>Pochamplaly</Manufacturer>

                             <MfrPartNumber>gdl0500</MfrPartNumber>


        <ItemType>Cotton</ItemType>





      </DescriptionData>

                <ProductData>

                                           <Clothing>

                                 <VariationData>

                                           <Size>Free SIze</Size>

                                           <Color>Red</Color>





                                           </VariationData>

                                 <ClassificationData>

                                           <ClothingType>EthnicWear</ClothingType>

                                           <Department>Women</Department>



                                             <ColorMap>Red</ColorMap>

                                              <StyleName>Lehenga Saree</StyleName>

                                             <SizeMap>Free Size</SizeMap>

                                             <MaterialType>Cotton</MaterialType>

                                             <CollectionDescription>Traditional</CollectionDescription>





                                           </ClassificationData>

                                           </Clothing>

      </ProductData>

    </Product>

  </Message>

</AmazonEnvelope>"""

# x = mws.Reports(access_key=access_key, secret_key=secret_key, account_id=merchant_id)
# report = x.get_report(report_id=reportid)
# response_data = report.original
# print(response_data)


x1 = mws.mws.MWS(access_key=access_key, secret_key=secret_key, account_id=merchant_id, region='IN')
x = mws.Feeds.submit_feed(x1, feed=feed.encode('utf-8'), feed_type="_POST_PRODUCT_DATA_",
                          marketplaceids="A21TJRUUN4KGV", content_type="text/xml", purge='false')
print(x._response_dict)