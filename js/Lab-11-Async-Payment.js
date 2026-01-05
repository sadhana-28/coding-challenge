// Lab 11: Async Payment

async function processPayment() {
  console.log("Processing payment...");
  await new Promise(resolve => setTimeout(resolve, 2000));
  console.log("Payment Successful");
}

processPayment();
