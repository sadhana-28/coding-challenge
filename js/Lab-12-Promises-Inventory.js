// Lab 12: Promises - Inventory

function checkInventory(quantity) {
  return new Promise((resolve, reject) => {
    let stock = 10;
    if (quantity <= stock) resolve("Stock Available");
    else reject("Out of Stock");
  });
}

checkInventory(5)
  .then(msg => console.log(msg))
  .catch(err => console.log(err));
