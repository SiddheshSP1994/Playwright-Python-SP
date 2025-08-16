import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8821", "title": "Checkout scenario 8821", "data": {"sku": "SKU8821", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8821@example.com", "threshold": 210}},
    {"id": "CHECKOUT-8822", "title": "Checkout scenario 8822", "data": {"sku": "SKU8822", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8822@example.com", "threshold": 220}},
    {"id": "CHECKOUT-8823", "title": "Checkout scenario 8823", "data": {"sku": "SKU8823", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8823@example.com", "threshold": 230}},
    {"id": "CHECKOUT-8824", "title": "Checkout scenario 8824", "data": {"sku": "SKU8824", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8824@example.com", "threshold": 240}},
    {"id": "CHECKOUT-8825", "title": "Checkout scenario 8825", "data": {"sku": "SKU8825", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8825@example.com", "threshold": 250}},
    {"id": "CHECKOUT-8826", "title": "Checkout scenario 8826", "data": {"sku": "SKU8826", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8826@example.com", "threshold": 260}},
    {"id": "CHECKOUT-8827", "title": "Checkout scenario 8827", "data": {"sku": "SKU8827", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8827@example.com", "threshold": 270}},
    {"id": "CHECKOUT-8828", "title": "Checkout scenario 8828", "data": {"sku": "SKU8828", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8828@example.com", "threshold": 280}},
    {"id": "CHECKOUT-8829", "title": "Checkout scenario 8829", "data": {"sku": "SKU8829", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8829@example.com", "threshold": 290}},
    {"id": "CHECKOUT-8830", "title": "Checkout scenario 8830", "data": {"sku": "SKU8830", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8830@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
