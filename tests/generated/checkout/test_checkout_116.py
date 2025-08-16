import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6901", "title": "Checkout scenario 6901", "data": {"sku": "SKU6901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6901@example.com", "threshold": 10}},
    {"id": "CHECKOUT-6902", "title": "Checkout scenario 6902", "data": {"sku": "SKU6902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6902@example.com", "threshold": 20}},
    {"id": "CHECKOUT-6903", "title": "Checkout scenario 6903", "data": {"sku": "SKU6903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6903@example.com", "threshold": 30}},
    {"id": "CHECKOUT-6904", "title": "Checkout scenario 6904", "data": {"sku": "SKU6904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6904@example.com", "threshold": 40}},
    {"id": "CHECKOUT-6905", "title": "Checkout scenario 6905", "data": {"sku": "SKU6905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6905@example.com", "threshold": 50}},
    {"id": "CHECKOUT-6906", "title": "Checkout scenario 6906", "data": {"sku": "SKU6906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6906@example.com", "threshold": 60}},
    {"id": "CHECKOUT-6907", "title": "Checkout scenario 6907", "data": {"sku": "SKU6907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6907@example.com", "threshold": 70}},
    {"id": "CHECKOUT-6908", "title": "Checkout scenario 6908", "data": {"sku": "SKU6908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6908@example.com", "threshold": 80}},
    {"id": "CHECKOUT-6909", "title": "Checkout scenario 6909", "data": {"sku": "SKU6909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6909@example.com", "threshold": 90}},
    {"id": "CHECKOUT-6910", "title": "Checkout scenario 6910", "data": {"sku": "SKU6910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6910@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
