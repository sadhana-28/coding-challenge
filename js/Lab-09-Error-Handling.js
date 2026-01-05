// Lab 9: Error Handling

class ValidationError extends Error {}

try {
  let quantity = 2;
  let price = 100;

  if (quantity <= 0 || price <= 0) {
    throw new ValidationError("Quantity and price must be greater than zero");
  }

  console.log("Inputs are valid");
} catch (error) {
  console.log("Error:", error.message);
} finally {
  console.log("Execution completed");
}
