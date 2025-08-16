import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6481", "title": "Checkout scenario 6481", "data": {"sku": "SKU6481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6481@example.com", "threshold": 810}},
    {"id": "CHECKOUT-6482", "title": "Checkout scenario 6482", "data": {"sku": "SKU6482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6482@example.com", "threshold": 820}},
    {"id": "CHECKOUT-6483", "title": "Checkout scenario 6483", "data": {"sku": "SKU6483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6483@example.com", "threshold": 830}},
    {"id": "CHECKOUT-6484", "title": "Checkout scenario 6484", "data": {"sku": "SKU6484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6484@example.com", "threshold": 840}},
    {"id": "CHECKOUT-6485", "title": "Checkout scenario 6485", "data": {"sku": "SKU6485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6485@example.com", "threshold": 850}},
    {"id": "CHECKOUT-6486", "title": "Checkout scenario 6486", "data": {"sku": "SKU6486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6486@example.com", "threshold": 860}},
    {"id": "CHECKOUT-6487", "title": "Checkout scenario 6487", "data": {"sku": "SKU6487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6487@example.com", "threshold": 870}},
    {"id": "CHECKOUT-6488", "title": "Checkout scenario 6488", "data": {"sku": "SKU6488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6488@example.com", "threshold": 880}},
    {"id": "CHECKOUT-6489", "title": "Checkout scenario 6489", "data": {"sku": "SKU6489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6489@example.com", "threshold": 890}},
    {"id": "CHECKOUT-6490", "title": "Checkout scenario 6490", "data": {"sku": "SKU6490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6490@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
