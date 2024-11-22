#Basic Flask Server Implementation


To get all products, just leave of the specific product ID
curl http://localhost:5000/products

To add a product:

curl -X POST -H "Content-Type: application/json" \
    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
    http://localhost:5000/products

To fetch a specific product, like the one may hae added with the command above.
HINT: No need to specify "-X GET" as it is the default method: 

curl http://localhost:5000/products/145