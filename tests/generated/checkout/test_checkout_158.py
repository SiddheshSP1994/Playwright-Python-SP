import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9421", "title": "Checkout scenario 9421", "data": {"sku": "SKU9421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9421@example.com", "threshold": 210}},
    {"id": "CHECKOUT-9422", "title": "Checkout scenario 9422", "data": {"sku": "SKU9422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9422@example.com", "threshold": 220}},
    {"id": "CHECKOUT-9423", "title": "Checkout scenario 9423", "data": {"sku": "SKU9423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9423@example.com", "threshold": 230}},
    {"id": "CHECKOUT-9424", "title": "Checkout scenario 9424", "data": {"sku": "SKU9424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9424@example.com", "threshold": 240}},
    {"id": "CHECKOUT-9425", "title": "Checkout scenario 9425", "data": {"sku": "SKU9425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9425@example.com", "threshold": 250}},
    {"id": "CHECKOUT-9426", "title": "Checkout scenario 9426", "data": {"sku": "SKU9426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9426@example.com", "threshold": 260}},
    {"id": "CHECKOUT-9427", "title": "Checkout scenario 9427", "data": {"sku": "SKU9427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9427@example.com", "threshold": 270}},
    {"id": "CHECKOUT-9428", "title": "Checkout scenario 9428", "data": {"sku": "SKU9428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9428@example.com", "threshold": 280}},
    {"id": "CHECKOUT-9429", "title": "Checkout scenario 9429", "data": {"sku": "SKU9429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9429@example.com", "threshold": 290}},
    {"id": "CHECKOUT-9430", "title": "Checkout scenario 9430", "data": {"sku": "SKU9430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9430@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
