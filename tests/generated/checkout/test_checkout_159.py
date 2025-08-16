import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9481", "title": "Checkout scenario 9481", "data": {"sku": "SKU9481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9481@example.com", "threshold": 810}},
    {"id": "CHECKOUT-9482", "title": "Checkout scenario 9482", "data": {"sku": "SKU9482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9482@example.com", "threshold": 820}},
    {"id": "CHECKOUT-9483", "title": "Checkout scenario 9483", "data": {"sku": "SKU9483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9483@example.com", "threshold": 830}},
    {"id": "CHECKOUT-9484", "title": "Checkout scenario 9484", "data": {"sku": "SKU9484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9484@example.com", "threshold": 840}},
    {"id": "CHECKOUT-9485", "title": "Checkout scenario 9485", "data": {"sku": "SKU9485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9485@example.com", "threshold": 850}},
    {"id": "CHECKOUT-9486", "title": "Checkout scenario 9486", "data": {"sku": "SKU9486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9486@example.com", "threshold": 860}},
    {"id": "CHECKOUT-9487", "title": "Checkout scenario 9487", "data": {"sku": "SKU9487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9487@example.com", "threshold": 870}},
    {"id": "CHECKOUT-9488", "title": "Checkout scenario 9488", "data": {"sku": "SKU9488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9488@example.com", "threshold": 880}},
    {"id": "CHECKOUT-9489", "title": "Checkout scenario 9489", "data": {"sku": "SKU9489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9489@example.com", "threshold": 890}},
    {"id": "CHECKOUT-9490", "title": "Checkout scenario 9490", "data": {"sku": "SKU9490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9490@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
