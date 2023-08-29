const express = require('express');
const redis = require('redis');
const util = require('util');


const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
];


const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);
const app = express();
const port = 1245;

function getItemById(id) {
    return listProducts[id];
}

function reserveStockById(itemId, stock) {
   client.set(itemId, stock , redis.print); 
}

async function getCurrentReservedStockById(itemId) {
    let value;
    value = await getAsync(itemId); 
    return value;
}



app.get('/list_products', (req, res) => {
    const data = []
    for (const prod of listProducts) {
        const obj = {}
        obj.itemId = prod.id;
        obj.itemName = prod.name;
        obj.price = prod.price;
        obj.initialAvailableQuantity = prod.stock;
        data.push(obj);
    }
    res.setHeader('Content-Type', 'application/json');
    res.statusCode = 200;
    res.send(JSON.stringify(data));
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const obj = listProducts.filter(prod => prod.id === +itemId)[0];
    res.setHeader('Content-Type', 'application/json');
    if (!obj) {
        res.statusCode = 404;
        res.send(JSON.stringify({"status":"Product not found"}));
    } else {
        const data = {};
        data.itemId = obj.id;
        data.itemName = obj.name;
        data.price = obj.price;
        data.initialAvailableQuantity = obj.stock;
        const reserved = await getCurrentReservedStockById(itemId)
        data.currentQuantity = obj.stock - +reserved;
        res.statusCode = 200;
        res.send(JSON.stringify(data));
    }
});


app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const obj = listProducts.filter(prod => prod.id === +itemId)[0];
    const reserved = await getCurrentReservedStockById(itemId);
    res.setHeader('Content-Type', 'application/json');
    if (!obj) {
        res.statusCode = 404;
        res.send(JSON.stringify({"status":"Product not found"}))
    } else if ((obj.stock - +reserved) <= 0) {
        res.statusCode = 200;
        res.send(JSON.stringify({"status": "Not enough stock available", "itemId": itemId}));
    } else {
        res.statusCode = 200;
        reserveStockById(itemId, reserved + 1);
        res.send(JSON.stringify({"status": "Reservation confirmed", "itemId": itemId}));
    }
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`)
})
