import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7081", "title": "Checkout scenario 7081", "data": {"sku": "SKU7081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7081@example.com", "threshold": 810}},
    {"id": "CHECKOUT-7082", "title": "Checkout scenario 7082", "data": {"sku": "SKU7082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7082@example.com", "threshold": 820}},
    {"id": "CHECKOUT-7083", "title": "Checkout scenario 7083", "data": {"sku": "SKU7083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7083@example.com", "threshold": 830}},
    {"id": "CHECKOUT-7084", "title": "Checkout scenario 7084", "data": {"sku": "SKU7084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7084@example.com", "threshold": 840}},
    {"id": "CHECKOUT-7085", "title": "Checkout scenario 7085", "data": {"sku": "SKU7085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7085@example.com", "threshold": 850}},
    {"id": "CHECKOUT-7086", "title": "Checkout scenario 7086", "data": {"sku": "SKU7086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7086@example.com", "threshold": 860}},
    {"id": "CHECKOUT-7087", "title": "Checkout scenario 7087", "data": {"sku": "SKU7087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7087@example.com", "threshold": 870}},
    {"id": "CHECKOUT-7088", "title": "Checkout scenario 7088", "data": {"sku": "SKU7088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7088@example.com", "threshold": 880}},
    {"id": "CHECKOUT-7089", "title": "Checkout scenario 7089", "data": {"sku": "SKU7089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7089@example.com", "threshold": 890}},
    {"id": "CHECKOUT-7090", "title": "Checkout scenario 7090", "data": {"sku": "SKU7090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7090@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
