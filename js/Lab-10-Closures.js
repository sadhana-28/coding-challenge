// Lab 10: Closures

function getDiscountFunction(type) {
  let rate = type === "Gold" ? 0.10 : 0;

  return function (amount) {
    return amount * rate;
  };
}

let discountFn = getDiscountFunction("Gold");
console.log("Discount:", discountFn(5000));
