import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5701", "title": "Checkout scenario 5701", "data": {"sku": "SKU5701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5701@example.com", "threshold": 10}},
    {"id": "CHECKOUT-5702", "title": "Checkout scenario 5702", "data": {"sku": "SKU5702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5702@example.com", "threshold": 20}},
    {"id": "CHECKOUT-5703", "title": "Checkout scenario 5703", "data": {"sku": "SKU5703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5703@example.com", "threshold": 30}},
    {"id": "CHECKOUT-5704", "title": "Checkout scenario 5704", "data": {"sku": "SKU5704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5704@example.com", "threshold": 40}},
    {"id": "CHECKOUT-5705", "title": "Checkout scenario 5705", "data": {"sku": "SKU5705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5705@example.com", "threshold": 50}},
    {"id": "CHECKOUT-5706", "title": "Checkout scenario 5706", "data": {"sku": "SKU5706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5706@example.com", "threshold": 60}},
    {"id": "CHECKOUT-5707", "title": "Checkout scenario 5707", "data": {"sku": "SKU5707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5707@example.com", "threshold": 70}},
    {"id": "CHECKOUT-5708", "title": "Checkout scenario 5708", "data": {"sku": "SKU5708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5708@example.com", "threshold": 80}},
    {"id": "CHECKOUT-5709", "title": "Checkout scenario 5709", "data": {"sku": "SKU5709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5709@example.com", "threshold": 90}},
    {"id": "CHECKOUT-5710", "title": "Checkout scenario 5710", "data": {"sku": "SKU5710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5710@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
