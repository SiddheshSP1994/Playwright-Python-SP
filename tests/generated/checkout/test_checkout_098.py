import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5821", "title": "Checkout scenario 5821", "data": {"sku": "SKU5821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5821@example.com", "threshold": 210}},
    {"id": "CHECKOUT-5822", "title": "Checkout scenario 5822", "data": {"sku": "SKU5822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5822@example.com", "threshold": 220}},
    {"id": "CHECKOUT-5823", "title": "Checkout scenario 5823", "data": {"sku": "SKU5823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5823@example.com", "threshold": 230}},
    {"id": "CHECKOUT-5824", "title": "Checkout scenario 5824", "data": {"sku": "SKU5824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5824@example.com", "threshold": 240}},
    {"id": "CHECKOUT-5825", "title": "Checkout scenario 5825", "data": {"sku": "SKU5825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5825@example.com", "threshold": 250}},
    {"id": "CHECKOUT-5826", "title": "Checkout scenario 5826", "data": {"sku": "SKU5826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5826@example.com", "threshold": 260}},
    {"id": "CHECKOUT-5827", "title": "Checkout scenario 5827", "data": {"sku": "SKU5827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5827@example.com", "threshold": 270}},
    {"id": "CHECKOUT-5828", "title": "Checkout scenario 5828", "data": {"sku": "SKU5828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5828@example.com", "threshold": 280}},
    {"id": "CHECKOUT-5829", "title": "Checkout scenario 5829", "data": {"sku": "SKU5829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5829@example.com", "threshold": 290}},
    {"id": "CHECKOUT-5830", "title": "Checkout scenario 5830", "data": {"sku": "SKU5830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5830@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
